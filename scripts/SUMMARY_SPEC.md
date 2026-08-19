# 요약 작성 규격

`data/candidate.json`을 읽고 이 문서의 규칙에 따라 `data/summary.json`을 작성한다.

## 독자와 목표

GeoAI, 환경계획, 도시계획, 탄소중립, GIS/원격탐사를 연구하는 한국인 연구자.
출근길 지하철·버스에서 3~5분 안에 읽는다. 화면은 작고 집중 시간은 짧다.

## 작성 규칙

1. 모든 서술은 **한국어**로 쓴다. 문체는 `~다` 형태의 간결한 평서문.
2. **학계에서 통용되는 전문 용어는 번역하지 말고 영어 원문 그대로** 표기한다.
   예: `Random Forest`, `NDVI`, `Sentinel-2`, `land use regression`, `SHAP`,
   `urban heat island`, `LSTM`, `semantic segmentation`, `digital elevation model`,
   `carbon sequestration`. 고유 기법명·지표명·센서명·데이터셋명은 반드시 영어를 유지한다.
3. 수치는 원문 그대로 옮긴다. 정확도, 감축량, 표본 수, 연구 기간, 대상 지역은
   확인 가능한 경우 빠짐없이 넣는다.
4. 문장은 짧게. 한 문장에 하나의 사실만 담는다. 수식은 쓰지 않는다.
5. **원문에 없는 내용을 지어내지 않는다.** `candidate.json`의 `basis`가
   `abstract_only`이면 방법론·결과 항목은 초록에서 확인 가능한 범위까지만 쓰고,
   "초록 기준"임을 문장 안에서 밝힌다. 추측으로 세부 절차나 수치를 채우지 않는다.
6. 홍보 문구, 감탄, "본 연구는 매우 흥미롭다" 같은 평가성 수식어를 쓰지 않는다.

## 입력: data/candidate.json

```
{
  "date":        "YYYY-MM-DD",
  "topic_key":   "geoxai",
  "topic_label": "GeoXAI",
  "basis":       "full_text" | "abstract_only",
  "paper":       { "title", "abstract", "authors", "venue", "published", "doi", ... },
  "full_text":   "논문 본문 텍스트 (basis가 abstract_only이면 빈 문자열)"
}
```

`full_text`가 비어 있지 않으면 그것을 근거로 방법론과 결과를 구체적으로 작성한다.
비어 있으면 `paper.abstract`만 근거로 삼는다.

## 출력: data/summary.json

**JSON 객체 하나만** 쓴다. 코드펜스, 주석, 설명 문장을 덧붙이지 않는다.
아래 13개 필드가 전부이며, 하나라도 빠지거나 다른 필드가 추가되면 검증에 실패한다.

| 필드 | 타입 | 내용 |
| --- | --- | --- |
| `one_liner` | string | 이 논문을 한 문장으로. 40자 내외 |
| `abstract_summary` | string | 초록 요약. 3~4문장 |
| `novelty` | string[] | 주요 차별성. **2~4개** |
| `contributions` | string[] | 주요 기여점. **2~4개** |
| `background` | string | 연구의 배경. 2~3문장 |
| `necessity` | string | 연구의 필요성. 2~3문장 |
| `objective` | string | 연구의 목적. 1~2문장 |
| `methodology` | string | 방법론. 데이터·연구 지역·모델/분석 기법 포함 3~5문장 |
| `results` | string | 결과. 정량적 수치가 있으면 반드시 포함해 3~5문장 |
| `discussion` | string | 논의. 함의·한계·후속 연구 방향 포함 3~4문장 |
| `keywords` | string[] | 핵심 키워드 **4~6개**. 학술 용어는 영어 원문 |
| `relevance_note` | string | 왜 읽을 만한지 1~2문장 |
| `basis` | string | `candidate.json`의 `basis` 값을 그대로 복사 |

배열 개수 제약(2~4개, 4~6개)은 검증기가 엄격히 확인한다.

## 검증

작성 후 반드시 아래를 실행한다.

```bash
python3 scripts/daily_paper.py write
```

성공하면 `_posts/`에 포스트가 생기고 임시 파일이 정리된다.
실패하면 어떤 필드가 왜 잘못됐는지 한국어로 출력되므로, `summary.json`을 고쳐 다시 실행한다.
