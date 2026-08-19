#!/usr/bin/env python3
"""매일 논문 1편을 골라 요약하고 Jekyll 포스트로 저장한다.

사용 예:
    python scripts/daily_paper.py                  # 오늘 날짜로 실행
    python scripts/daily_paper.py --dry-run        # 후보 선정까지만, API 호출 없음
    python scripts/daily_paper.py --topic geoai    # 주제 고정
    python scripts/daily_paper.py --date 2026-08-19
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import already_posted, load_state, record, save_state, write_post
from sources import TOPICS, TOPICS_BY_KEY, Paper, collect_candidates, rotation_from

KST = timezone(timedelta(hours=9))


def today_kst() -> date:
    return datetime.now(KST).date()


def pick_paper(day: date, state: dict, topic_key: str | None,
               window_days: int) -> Paper | None:
    """당일 주제부터 순회하며 아직 게시하지 않은 최고 점수 논문을 고른다."""
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
            best = fresh[0]
            print(f"\n선정: {best.title}")
            print(f"  주제={topic.label}  소스={best.source}  "
                  f"발행={best.published}  점수={best.score:.1f}")
            return best

        print("    게시 가능한 신규 논문 없음 — 다음 주제로 넘어간다")

    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="일일 논문 요약 포스트 생성")
    parser.add_argument("--date", help="게시 날짜 (YYYY-MM-DD, 기본: 오늘 KST)")
    parser.add_argument("--topic", help="주제 고정 (예: geoai, gis, carbon-neutral)")
    parser.add_argument("--window-days", type=int, default=240,
                        help="저널 논문 검색 기간(일). 기본 240")
    parser.add_argument("--dry-run", action="store_true",
                        help="후보 선정까지만 수행하고 Claude API를 호출하지 않는다")
    parser.add_argument("--no-fulltext", action="store_true",
                        help="OA PDF 전문 추출을 건너뛰고 초록만으로 요약한다")
    args = parser.parse_args()

    day = date.fromisoformat(args.date) if args.date else today_kst()
    print(f"=== daily-paper {day.isoformat()} ===\n")

    state = load_state()
    print(f"기존 게시글 {len(state.get('posted', []))}건\n")

    paper = pick_paper(day, state, args.topic, args.window_days)
    if paper is None:
        print("\n모든 주제에서 신규 논문을 찾지 못했다. 오늘은 게시를 건너뛴다.")
        return 0

    if args.dry_run:
        print("\n[dry-run] 요약과 포스트 작성을 생략한다.")
        print(f"초록 {len(paper.abstract)}자 / PDF={'있음' if paper.pdf_url else '없음'}")
        return 0

    from summarize import summarize  # anthropic 의존성은 실제 실행 시에만 로드

    print("\n요약 생성 중...")
    summary = summarize(paper, use_fulltext=not args.no_fulltext)

    post_path = write_post(paper, summary, day)
    record(state, paper, post_path, day)
    save_state(state)

    print(f"\n포스트 작성 완료: {post_path.relative_to(Path.cwd()) if post_path.is_relative_to(Path.cwd()) else post_path}")
    print(f"한 줄 요약: {summary.one_liner}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
