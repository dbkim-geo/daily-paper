"""Claude API로 논문을 한국어 요약한다.

출력은 Pydantic 스키마로 구조화(structured outputs)해 검증하므로,
템플릿 렌더링 단계에서 파싱 오류가 발생하지 않는다.
"""

from __future__ import annotations

import anthropic
from pydantic import BaseModel, Field

from fulltext import extract_pdf_text
from schema import PaperSummary, validate_summary
from sources import Paper, USER_AGENT

MODEL = "claude-opus-5"
MAX_TOKENS = 16000



class _SummaryModel(BaseModel):
    """Messages API structured outputs용 모델. 검증 후 schema.PaperSummary로 변환한다."""

    one_liner: str = Field(description="이 논문을 한 문장으로. 40자 내외의 한국어.")
    abstract_summary: str = Field(description="초록 요약. 3~4문장 한국어 서술형.")
    novelty: list[str] = Field(description="주요 차별성 2~4개.")
    contributions: list[str] = Field(description="주요 기여점 2~4개.")
    background: str = Field(description="연구의 배경. 2~3문장.")
    necessity: str = Field(description="연구의 필요성. 2~3문장.")
    objective: str = Field(description="연구의 목적. 1~2문장.")
    methodology: str = Field(description="방법론. 데이터·연구 지역·기법 포함 3~5문장.")
    results: str = Field(description="결과. 정량적 수치 포함 3~5문장.")
    discussion: str = Field(description="논의. 함의·한계·후속 연구 3~4문장.")
    keywords: list[str] = Field(description="핵심 키워드 4~6개. 학술 용어는 영어 원문.")
    relevance_note: str = Field(description="왜 읽을 만한지 1~2문장.")
    basis: str = Field(description="full_text 또는 abstract_only.")


SYSTEM_PROMPT = """\
당신은 GeoAI, 환경계획, 도시계획, 탄소중립, GIS/원격탐사를 연구하는 한국인 연구자를 위해
매일 아침 논문 한 편을 정리해 주는 연구 보조자다.

독자 상황: 출근길 지하철·버스에서 3~5분 안에 읽는다. 화면은 작고 집중 시간은 짧다.

작성 규칙:
1. 모든 서술은 한국어로 쓴다. 문체는 '~다' 형태의 간결한 평서문.
2. 학계에서 통용되는 전문 용어는 번역하지 말고 영어 원문 그대로 표기한다.
   예: Random Forest, NDVI, Sentinel-2, land use regression, SHAP, urban heat island,
       LSTM, semantic segmentation, digital elevation model, carbon sequestration.
   일반 명사는 한국어로 쓴다. (예: dataset → 데이터셋 대신 '자료'처럼 억지 번역하지 말고
   맥락상 자연스러운 쪽을 택하되, 고유 기법명·지표명·센서명은 반드시 영어를 유지한다.)
3. 수치는 원문 그대로 옮긴다. 정확도, 감축량, 표본 수, 연구 기간, 대상 지역은
   확인 가능한 경우 빠짐없이 넣는다.
4. 문장은 짧게. 한 문장에 하나의 사실만 담는다. 수식은 쓰지 않는다.
5. 원문에 없는 내용을 지어내지 않는다. 초록만 제공된 경우, 방법론·결과 항목은
   초록에서 확인 가능한 범위까지만 쓰고 "초록 기준"임을 문장 안에서 밝힌다.
   추측으로 세부 절차나 수치를 채우지 않는다.
6. 홍보 문구, 감탄, "본 연구는 매우 흥미롭다" 같은 평가성 수식어를 쓰지 않는다.
"""


def build_user_prompt(paper: Paper, full_text: str) -> str:
    authors = ", ".join(paper.authors) if paper.authors else "정보 없음"
    parts = [
        "다음 논문을 정해진 스키마에 맞춰 한국어로 요약하라.",
        "",
        f"제목: {paper.title}",
        f"저자: {authors}",
        f"출처: {paper.venue or '정보 없음'}",
        f"발행일: {paper.published or '정보 없음'}",
        f"DOI: {paper.doi or '없음'}",
        "",
        "[초록]",
        paper.abstract,
    ]
    if full_text:
        parts += [
            "",
            "[본문 전문 — 아래 내용을 근거로 방법론과 결과를 구체적으로 작성하라]",
            full_text,
        ]
    else:
        parts += [
            "",
            "[안내] 본문 전문에 접근할 수 없어 초록만 제공한다.",
            "초록에서 확인되지 않는 세부 절차나 수치를 만들어 내지 말고,",
            "해당 항목은 초록 기준임을 밝힌 뒤 확인 가능한 범위까지만 서술하라.",
        ]
    return "\n".join(parts)


def summarize(paper: Paper, *, use_fulltext: bool = True,
              client: anthropic.Anthropic | None = None) -> PaperSummary:
    client = client or anthropic.Anthropic()

    full_text = ""
    if use_fulltext and paper.pdf_url:
        print(f"    전문 확보 시도: {paper.pdf_url}")
        full_text = extract_pdf_text(paper.pdf_url)
        print(f"    전문 {len(full_text):,}자 확보" if full_text else "    전문 없음 — 초록 기반 요약")

    response = client.messages.parse(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_prompt(paper, full_text)}],
        output_format=_SummaryModel,
    )

    if response.stop_reason == "refusal":
        raise RuntimeError(f"모델이 요약을 거부했다: {response.stop_details}")

    parsed = response.parsed_output
    if parsed is None:
        raise RuntimeError("구조화 출력 파싱에 실패했다.")

    payload = parsed.model_dump()
    # 모델이 잘못 표기할 수 있으므로 실제 입력 기준으로 교정한다.
    payload["basis"] = "full_text" if full_text else "abstract_only"
    summary = validate_summary(payload)

    usage = response.usage
    print(f"    요약 완료 (in={usage.input_tokens:,} / out={usage.output_tokens:,} tokens)")
    return summary
