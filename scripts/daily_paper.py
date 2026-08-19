#!/usr/bin/env python3
"""일일 논문 요약 파이프라인.

세 개의 서브커맨드로 나뉜다. 기본 경로(GitHub Actions)는 select → (Claude Code) → write 이며,
Claude Code가 요약을 담당하므로 Anthropic API 과금이 발생하지 않는다.

  select   논문을 고르고 전문을 추출해 data/candidate.json 을 만든다. (API 불필요)
  write    data/summary.json 을 검증해 포스트로 렌더링하고 게시 이력을 갱신한다. (API 불필요)
  run      선정부터 요약까지 한 번에 수행한다. Anthropic API 키가 필요하다. (로컬 테스트용)

사용 예:
    python scripts/daily_paper.py select --dry-run
    python scripts/daily_paper.py select --topic geoai
    python scripts/daily_paper.py write
    python scripts/daily_paper.py run                  # ANTHROPIC_API_KEY 필요
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import (STATE_PATH, already_posted, load_state, record, save_state,
                    write_post)
from sources import (TOPICS, TOPICS_BY_KEY, Paper, collect_candidates,
                     find_arxiv_pdf, rotation_from)

KST = timezone(timedelta(hours=9))
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CANDIDATE_PATH = DATA_DIR / "candidate.json"
SUMMARY_PATH = DATA_DIR / "summary.json"


def today_kst() -> date:
    return datetime.now(KST).date()


# --------------------------------------------------------------------------
# 공통: 논문 선정
# --------------------------------------------------------------------------

# 한 주제에서 전문 확보를 시도할 최대 후보 수.
# 상용 출판사의 차단률이 높아(실측 상위 15건 중 3~4건만 성공) 넉넉히 둔다.
# 차단 응답은 즉시 오므로 시간 비용은 크지 않다.
MAX_FULLTEXT_ATTEMPTS = 15


def iter_topic_candidates(day: date, state: dict, topic_key: str | None,
                          window_days: int):
    """주제를 순회하며 (주제, 미게시 후보 목록)을 차례로 내놓는다."""
    if topic_key:
        topic = TOPICS_BY_KEY.get(topic_key)
        if topic is None:
            raise SystemExit(
                f"알 수 없는 주제: {topic_key}\n"
                f"가능한 값: {', '.join(t.key for t in TOPICS)}"
            )
        order = [topic]
    else:
        order = rotation_from(day)

    for idx, topic in enumerate(order):
        print(f"[{idx + 1}/{len(order)}] 주제 '{topic.label}' 후보 수집")
        candidates = collect_candidates(topic, day, window_days=window_days)
        fresh = [p for p in candidates if not already_posted(state, p)]
        print(f"    후보 {len(candidates)}건 / 미게시 {len(fresh)}건")

        if fresh:
            yield topic, fresh
        else:
            print("    게시 가능한 신규 논문 없음 — 다음 주제로 넘어간다")


# --------------------------------------------------------------------------
# select
# --------------------------------------------------------------------------

def cmd_select(args: argparse.Namespace) -> int:
    day = date.fromisoformat(args.date) if args.date else today_kst()
    print(f"=== select {day.isoformat()} ===\n")

    # 이전 실행의 잔여 파일을 반드시 제거한다. 남아 있으면 워크플로가
    # 오늘 후보를 찾지 못했는데도 어제 것으로 포스트를 만들 수 있다.
    for path in (CANDIDATE_PATH, SUMMARY_PATH):
        path.unlink(missing_ok=True)

    state = load_state()
    print(f"기존 게시글 {len(state.get('posted', []))}건\n")

    # pypdf만 사용, anthropic 불필요
    from fulltext import extract_author_keywords, extract_pdf_text

    paper: Paper | None = None
    full_text = ""

    for topic, fresh in iter_topic_candidates(day, state, args.topic, args.window_days):
        if args.no_fulltext:
            paper = fresh[0]
            break

        # 전문을 실제로 확보한 논문만 게시한다. OA 논문이라도 상용 출판사가
        # PDF를 막는 일이 잦으므로, 링크 유무가 아니라 실제 확보로 판정한다.
        for idx, cand in enumerate(fresh[:MAX_FULLTEXT_ATTEMPTS]):
            print(f"\n[{idx + 1}] 전문 확보 시도({cand.score:.1f}점, {cand.venue[:30]}): "
                  f"{cand.title[:60]}")
            urls = [cand.pdf_url, *cand.alt_pdf_urls]
            for url in urls:
                if not url:
                    continue
                print(f"    {url}")
                full_text = extract_pdf_text(url)
                if full_text:
                    break

            # 출판사가 막았으면 같은 논문의 arXiv 사본을 찾는다.
            # 저널 등급을 낮추지 않고 전문을 얻을 수 있는 유일한 경로다.
            if not full_text and cand.source != "arxiv":
                arxiv_pdf = find_arxiv_pdf(cand.title)
                if arxiv_pdf and arxiv_pdf not in urls:
                    print(f"    arXiv 사본: {arxiv_pdf}")
                    full_text = extract_pdf_text(arxiv_pdf)

            if full_text:
                paper = cand
                break

        if paper:
            break
        print(f"\n'{topic.label}'에서 전문을 확보한 논문이 없다 — 다음 주제로 넘어간다")

    if paper is None:
        print("\n전문을 확보한 논문을 찾지 못했다. 오늘은 게시를 건너뛴다.")
        return 0

    topic = TOPICS_BY_KEY[paper.topic_key]
    print(f"\n선정: {paper.title}")
    print(f"  주제={topic.label}  저널={paper.venue}  소스={paper.source}  "
          f"발행={paper.published}  점수={paper.score:.1f}")
    print(f"  전문 {len(full_text):,}자" if full_text else "  전문 없음(--no-fulltext)")

    if full_text:
        # 저자가 원문에 적은 키워드. 없으면 OpenAlex의 자동 생성 키워드로
        # 채우지 않는다. 오류가 섞여 있어 "원문 키워드"라고 할 수 없다.
        paper.paper_keywords = extract_author_keywords(full_text)
        if paper.paper_keywords:
            print(f"  원문 키워드: {', '.join(paper.paper_keywords)}")

    if args.dry_run:
        print("\n[dry-run] candidate.json을 쓰지 않는다.")
        return 0

    topic = TOPICS_BY_KEY[paper.topic_key]
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CANDIDATE_PATH.write_text(json.dumps({
        "date": day.isoformat(),
        "topic_key": topic.key,
        "topic_label": topic.label,
        "basis": "full_text" if full_text else "abstract_only",
        "paper": paper.to_dict(),
        "full_text": full_text,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\ncandidate.json 작성 완료 ({CANDIDATE_PATH.stat().st_size:,} bytes)")
    return 0


# --------------------------------------------------------------------------
# write
# --------------------------------------------------------------------------

def cmd_write(args: argparse.Namespace) -> int:
    from schema import SummaryValidationError, validate_summary

    if not CANDIDATE_PATH.exists():
        print(f"candidate.json이 없다: {CANDIDATE_PATH}", file=sys.stderr)
        return 1
    if not SUMMARY_PATH.exists():
        print(f"summary.json이 없다: {SUMMARY_PATH}", file=sys.stderr)
        print("Claude Code 요약 단계가 실패했을 가능성이 높다.", file=sys.stderr)
        return 1

    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    day = date.fromisoformat(candidate["date"])
    paper = Paper(**candidate["paper"])

    raw = SUMMARY_PATH.read_text(encoding="utf-8").strip()
    # 모델이 코드펜스로 감싸는 경우가 있어 벗겨낸다.
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    try:
        summary = validate_summary(json.loads(raw))
    except json.JSONDecodeError as exc:
        print(f"summary.json이 올바른 JSON이 아니다: {exc}", file=sys.stderr)
        return 1
    except SummaryValidationError as exc:
        print(f"summary.json이 스키마를 만족하지 않는다:\n{exc}", file=sys.stderr)
        return 1

    # 근거는 실제로 전문을 넘겼는지로 판정한다. 모델의 자기보고를 신뢰하지 않는다.
    summary.basis = candidate["basis"]

    state = load_state()
    if already_posted(state, paper):
        print("이미 게시한 논문이다. 중복 게시를 중단한다.", file=sys.stderr)
        return 1

    post_path = write_post(paper, summary, day)
    record(state, paper, post_path, day)
    save_state(state)

    for path in (CANDIDATE_PATH, SUMMARY_PATH):
        path.unlink(missing_ok=True)

    print(f"포스트 작성 완료: {post_path.name}")
    print(f"한 줄 요약: {summary.one_liner}")
    print(f"요약 근거: {summary.basis}")
    return 0


# --------------------------------------------------------------------------
# run (API 경로 — 로컬 테스트용)
# --------------------------------------------------------------------------

def cmd_run(args: argparse.Namespace) -> int:
    day = date.fromisoformat(args.date) if args.date else today_kst()
    print(f"=== run {day.isoformat()} ===\n")

    state = load_state()
    paper = next((fresh[0] for _, fresh
                  in iter_topic_candidates(day, state, args.topic, args.window_days)), None)
    if paper is None:
        print("\n모든 주제에서 신규 논문을 찾지 못했다. 오늘은 게시를 건너뛴다.")
        return 0

    from summarize import summarize

    print("\n요약 생성 중...")
    summary = summarize(paper, use_fulltext=not args.no_fulltext)

    post_path = write_post(paper, summary, day)
    record(state, paper, post_path, day)
    save_state(state)

    print(f"\n포스트 작성 완료: {post_path.name}")
    print(f"한 줄 요약: {summary.one_liner}")
    return 0


# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="일일 논문 요약 파이프라인")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_selection_args(p: argparse.ArgumentParser) -> None:
        p.add_argument("--date", help="게시 날짜 (YYYY-MM-DD, 기본: 오늘 KST)")
        p.add_argument("--topic", help="주제 고정 (예: geoai, gis, carbon-neutral)")
        p.add_argument("--window-days", type=int, default=240,
                       help="저널 논문 검색 기간(일). 기본 240")
        p.add_argument("--no-fulltext", action="store_true",
                       help="PDF 전문 추출을 건너뛰고 초록만 사용한다")

    p_select = sub.add_parser("select", help="논문 선정 + 전문 추출 → candidate.json")
    add_selection_args(p_select)
    p_select.add_argument("--dry-run", action="store_true",
                          help="선정 결과만 출력하고 파일을 쓰지 않는다")
    p_select.set_defaults(func=cmd_select)

    p_write = sub.add_parser("write", help="summary.json 검증 → 포스트 렌더링")
    p_write.set_defaults(func=cmd_write)

    p_run = sub.add_parser("run", help="선정 + API 요약 + 렌더링 (ANTHROPIC_API_KEY 필요)")
    add_selection_args(p_run)
    p_run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
