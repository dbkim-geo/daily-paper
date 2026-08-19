"""요약 결과 스키마 및 검증.

표준 라이브러리만 사용한다. 클라우드 샌드박스에서 pip install이 실패해도
요약 검증과 포스트 렌더링은 항상 동작해야 하기 때문이다.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict

# (필드명, 한국어 설명, 타입) — 순서는 포스트에 표시되는 순서와 같다.
TEXT_FIELDS: tuple[tuple[str, str], ...] = (
    ("one_liner",        "이 논문을 한 문장으로. 40자 내외의 한국어"),
    ("abstract_summary", "초록 요약. 3~4문장"),
    ("background",       "연구의 배경. 2~3문장"),
    ("necessity",        "연구의 필요성. 2~3문장"),
    ("objective",        "연구의 목적. 1~2문장"),
    ("methodology",      "방법론. 데이터·연구 지역·모델/분석 기법 포함 3~5문장"),
    ("results",          "결과. 정량적 수치가 있으면 반드시 포함해 3~5문장"),
    ("discussion",       "논의. 함의·한계·후속 연구 방향 포함 3~4문장"),
    ("relevance_note",   "이 논문을 왜 읽을 만한지 1~2문장"),
)

LIST_FIELDS: tuple[tuple[str, str, int, int], ...] = (
    ("novelty",       "주요 차별성", 2, 4),
    ("contributions", "주요 기여점", 2, 4),
    ("keywords",      "핵심 키워드. 학술 용어는 영어 원문 그대로", 4, 6),
)

VALID_BASIS = ("full_text", "abstract_only")


@dataclass
class PaperSummary:
    one_liner: str
    abstract_summary: str
    background: str
    necessity: str
    objective: str
    methodology: str
    results: str
    discussion: str
    relevance_note: str
    novelty: list[str] = field(default_factory=list)
    contributions: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    basis: str = "abstract_only"

    def to_dict(self) -> dict:
        return asdict(self)


class SummaryValidationError(ValueError):
    """요약 JSON이 스키마를 만족하지 않을 때."""


def validate_summary(data: object) -> PaperSummary:
    """dict를 검증해 PaperSummary로 변환한다. 문제가 있으면 전부 모아서 보고한다."""
    if not isinstance(data, dict):
        raise SummaryValidationError(f"최상위가 JSON 객체가 아니다 (실제: {type(data).__name__})")

    errors: list[str] = []
    values: dict[str, object] = {}

    for name, desc in TEXT_FIELDS:
        value = data.get(name)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"'{name}' ({desc}): 비어 있지 않은 문자열이어야 한다")
        else:
            values[name] = value.strip()

    for name, desc, lo, hi in LIST_FIELDS:
        value = data.get(name)
        if not isinstance(value, list):
            errors.append(f"'{name}' ({desc}): 문자열 배열이어야 한다")
            continue
        items = [v.strip() for v in value if isinstance(v, str) and v.strip()]
        if len(items) != len(value):
            errors.append(f"'{name}': 비어 있지 않은 문자열만 담아야 한다")
        elif not (lo <= len(items) <= hi):
            errors.append(f"'{name}' ({desc}): {lo}~{hi}개여야 한다 (실제 {len(items)}개)")
        else:
            values[name] = items

    basis = data.get("basis")
    if basis not in VALID_BASIS:
        errors.append(f"'basis': {' 또는 '.join(VALID_BASIS)} 중 하나여야 한다 (실제: {basis!r})")
    else:
        values["basis"] = basis

    unknown = set(data) - {n for n, _ in TEXT_FIELDS} - {n for n, _, _, _ in LIST_FIELDS} - {"basis"}
    if unknown:
        errors.append(f"알 수 없는 필드: {', '.join(sorted(unknown))}")

    if errors:
        raise SummaryValidationError("\n".join(f"  - {e}" for e in errors))

    return PaperSummary(**values)  # type: ignore[arg-type]
