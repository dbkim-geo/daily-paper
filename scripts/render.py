"""요약 결과를 Jekyll 포스트로 렌더링하고 게시 이력을 관리한다."""

from __future__ import annotations

import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

from sources import Paper, TOPICS_BY_KEY

if TYPE_CHECKING:  # anthropic 의존성을 dry-run 경로에서 끌어오지 않기 위함
    from schema import PaperSummary

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
STATE_PATH = ROOT / "data" / "state.json"


# --------------------------------------------------------------------------
# 게시 이력 (중복 방지)
# --------------------------------------------------------------------------

def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"posted": [], "keys": []}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def already_posted(state: dict, paper: Paper) -> bool:
    return bool(set(paper.identity_keys()) & set(state.get("keys", [])))


def record(state: dict, paper: Paper, post_path: Path, day: date) -> None:
    state.setdefault("keys", []).extend(paper.identity_keys())
    state["keys"] = sorted(set(state["keys"]))
    state.setdefault("posted", []).append({
        "date": day.isoformat(),
        "topic": paper.topic_key,
        "title": paper.title,
        "doi": paper.doi,
        "arxiv_id": paper.arxiv_id,
        "source": paper.source,
        "post": post_path.name,
    })


# --------------------------------------------------------------------------
# 렌더링
# --------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text or "paper"


def yq(value) -> str:
    """YAML 안전 인용. JSON 문자열은 YAML 이중인용 스칼라와 호환된다."""
    return json.dumps(value, ensure_ascii=False)


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {item.strip()}" for item in items if item and item.strip())


def render_markdown(paper: Paper, summary: "PaperSummary", day: date) -> str:
    topic = TOPICS_BY_KEY.get(paper.topic_key)
    topic_label = topic.label if topic else paper.topic_key

    fm = [
        "---",
        "layout: post",
        f"title: {yq(paper.title)}",
        f"date: {day.isoformat()} 08:30:00 +0900",
        f"topic: {yq(topic_label)}",
        f"topic_key: {yq(paper.topic_key)}",
        f"one_liner: {yq(summary.one_liner)}",
        f"authors: {yq(', '.join(paper.authors))}",
        f"venue: {yq(paper.venue)}",
        f"published: {yq(paper.published)}",
        f"doi: {yq(paper.doi)}",
        f"paper_url: {yq(paper.url)}",
        f"pdf_url: {yq(paper.pdf_url)}",
        f"source: {yq(paper.source)}",
        f"basis: {yq(summary.basis)}",
        "keywords:",
        *[f"  - {yq(k)}" for k in summary.keywords],
    ]
    if paper.paper_keywords:
        fm.append("paper_keywords:")
        fm.extend(f"  - {yq(k)}" for k in paper.paper_keywords)
    if paper.figure_file:
        fm.append(f"figure: {yq('/assets/figures/' + paper.figure_file)}")
    fm.extend(["---", ""])

    body = [f"## 한 줄 요약\n\n**{summary.one_liner}**\n"]

    if paper.figure_file:
        # 저작권 표시는 CC BY 계열의 조건이다. 출처·저작자·라이선스를 함께 적는다.
        credit = ", ".join(filter(None, [
            paper.authors[0] + " 외" if paper.authors else "",
            paper.venue,
            paper.published[:4] if paper.published else "",
        ]))
        body.append(
            f"![원문 대표 그림]({{{{ '/assets/figures/{paper.figure_file}' | relative_url }}}})\n\n"
            f"*원문에서 발췌 — {credit}. "
            f"[{paper.license.upper()}](https://creativecommons.org/licenses/) 라이선스.*\n"
        )

    # 전문 기반일 때는 굳이 밝히지 않는다. 초록 기반일 때만 경고가 의미가 있다.
    if summary.basis != "full_text":
        body.append(
            "> 본문 전문에 접근할 수 없어 **초록(abstract) 기준**으로 요약했다. "
            "방법론과 결과의 세부 사항은 원문 확인이 필요하다.\n"
        )

    body += [
        f"## 초록 요약\n\n{summary.abstract_summary}\n",
        f"## 주요 차별성\n\n{_bullets(summary.novelty)}\n",
        f"## 주요 기여점\n\n{_bullets(summary.contributions)}\n",
        f"## 연구의 배경\n\n{summary.background}\n",
        f"## 필요성\n\n{summary.necessity}\n",
        f"## 목적\n\n{summary.objective}\n",
        f"## 방법론\n\n{summary.methodology}\n",
        f"## 결과\n\n{summary.results}\n",
        f"## 논의\n\n{summary.discussion}\n",
        f"## 왜 읽을 만한가\n\n{summary.relevance_note}\n",
    ]

    if paper.paper_keywords:
        body.append("## 원문 키워드\n\n"
                    + ", ".join(f"`{k}`" for k in paper.paper_keywords) + "\n")

    # 원문 링크
    links = []
    if paper.url:
        links.append(f"- 원문: [{paper.url}]({paper.url})")
    if paper.pdf_url and paper.pdf_url != paper.url:
        links.append(f"- PDF: [{paper.pdf_url}]({paper.pdf_url})")
    if paper.doi:
        doi_url = paper.doi if paper.doi.startswith("http") else f"https://doi.org/{paper.doi}"
        links.append(f"- DOI: [{doi_url}]({doi_url})")
    if links:
        body.append("## 원문 링크\n\n" + "\n".join(links) + "\n")

    return "\n".join(fm) + "\n" + "\n".join(body)


def write_post(paper: Paper, summary: "PaperSummary", day: date) -> Path:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    path = POSTS_DIR / f"{day.isoformat()}-{slugify(paper.title)}.md"
    path.write_text(render_markdown(paper, summary, day), encoding="utf-8")
    return path
