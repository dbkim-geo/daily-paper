# Daily Paper

매일 아침 8시 30분(KST)에 논문 한 편을 자동으로 골라 한국어로 요약하고
GitHub Pages에 게시하는 파이프라인.

**사이트:** https://dbkim-geo.github.io/daily-paper/

요약은 **Claude 루틴**(스케줄 클라우드 에이전트)이 Max 구독 한도로 수행한다.
Anthropic API 과금은 발생하지 않는다.

---

## 동작 방식

```
23:30 UTC (= 08:30 KST) — Claude 루틴이 클라우드 세션을 띄우고 저장소를 체크아웃
   │
   ├─ 1. select    주제 순환 → 후보 수집 → 채점·선정 → PDF 전문 추출
   │               (scripts/daily_paper.py, 표준 라이브러리만 사용)
   │                          ↓ data/candidate.json
   ├─ 2. 요약       Claude가 SUMMARY_SPEC.md 규격대로 작성
   │                          ↓ data/summary.json
   ├─ 3. write     스키마 검증 → 포스트 렌더링 → 게시 이력 갱신
   │               (실패 시 오류를 보고 고쳐 재시도, 최대 3회)
   └─ 4. 커밋·푸시  _posts/ 와 data/state.json 만 → GitHub Pages 재빌드
```

요약 생성만 Claude가 맡고, **선정과 렌더링은 결정론적인 Python 코드가 담당한다.**
덕분에 출력 형식이 매일 동일하고, 스키마를 어기면 게시되지 않고 실패한다.

주제 순환: `GeoAI → GeoXAI → 환경계획 → 도시계획 → 탄소중립 → 탄소저감 → GIS → Remote Sensing`

당일 주제에 신규 논문이 없으면 다음 주제로 넘어가므로 매일 한 편이 보장된다.
이미 게시한 논문은 DOI · arXiv ID · 제목 해시로 걸러낸다 (`data/state.json`).

> **Google Scholar 추천 논문은 연동하지 않는다.** 공개 API가 없고 추천 피드가 개인 로그인
> 세션을 요구해 자동화가 불가능하다. 위 키워드 기반 수집이 그 대체다.

---

## 설정

### 1. GitHub Pages 활성화

저장소 → **Settings → Pages**

- **Source**: `Deploy from a branch`
- **Branch**: `main` / `/ (root)`

Jekyll 빌드는 GitHub Pages가 자동으로 수행한다. 별도 빌드 워크플로가 필요 없다.

### 2. 루틴

이미 생성되어 있다. 관리: <https://claude.ai/code/routines>

| 항목 | 값 |
| --- | --- |
| 이름 | Daily Paper - 매일 논문 1편 요약 게시 |
| 스케줄 | `30 23 * * *` UTC = 매일 08:30 KST |
| 모델 | Claude Opus 5 |
| 저장소 | `dbkim-geo/daily-paper` |

루틴이 읽는 지시서는 저장소 안에 있다. 동작을 바꾸려면 이 두 파일을 고치면 된다.

- [`scripts/ROUTINE.md`](scripts/ROUTINE.md) — 실행 절차
- [`scripts/SUMMARY_SPEC.md`](scripts/SUMMARY_SPEC.md) — 요약 작성 규칙과 출력 스키마

API 키도, Actions Secret도 필요 없다.

---

## 로컬 실행

논문 선정은 표준 라이브러리만으로 동작한다. 전문 추출을 쓰려면 `pypdf`만 있으면 된다.

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt

# 후보 선정만 확인 (파일을 쓰지 않는다)
.venv/bin/python scripts/daily_paper.py select --dry-run

# 특정 주제로 고정
.venv/bin/python scripts/daily_paper.py select --dry-run --topic geoai

# candidate.json 생성 → 직접 summary.json 작성 → 렌더링
.venv/bin/python scripts/daily_paper.py select
.venv/bin/python scripts/daily_paper.py write
```

| 서브커맨드 | 설명 | API 키 |
| --- | --- | --- |
| `select` | 논문 선정 + 전문 추출 → `data/candidate.json` | 불필요 |
| `write` | `data/summary.json` 검증 → 포스트 렌더링 + 이력 갱신 | 불필요 |
| `run` | 선정부터 요약까지 한 번에 (Anthropic API 사용) | **필요** |

`select` / `run` 공통 옵션:

| 옵션 | 설명 |
| --- | --- |
| `--date YYYY-MM-DD` | 게시 날짜 지정 (기본: 오늘 KST) |
| `--topic KEY` | 주제 고정. `geoai`, `geoxai`, `env-planning`, `urban-planning`, `carbon-neutral`, `carbon-reduction`, `gis`, `remote-sensing` |
| `--window-days N` | 저널 논문 검색 기간(일). 기본 240 |
| `--no-fulltext` | PDF 전문 추출을 건너뛰고 초록만 사용 |

### 사이트 로컬 미리보기 (선택)

Ruby가 설치되어 있어야 한다.

```bash
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000/daily-paper/
```

---

## 폴백: GitHub Actions + API 키

루틴이 막혔을 때를 대비한 수동 백업 경로. **평소에는 쓰지 않는다.**

`.github/workflows/daily-paper.yml`은 `workflow_dispatch`만 걸려 있어 자동 실행되지 않는다.
쓰려면 저장소 Secret에 `ANTHROPIC_API_KEY`를 등록해야 하고, 사용량만큼 과금된다
(전문 요약 기준 1회 약 $0.15~0.30).

스케줄 트리거를 다시 켜면 루틴과 함께 돌아 같은 날 두 편이 올라가므로 주의.

---

## 구조

```
.
├── scripts/
│   ├── ROUTINE.md              루틴 실행 절차 (루틴이 읽는 지시서)
│   ├── SUMMARY_SPEC.md         요약 작성 규칙 + 출력 스키마
│   ├── daily_paper.py          CLI — select / write / run
│   ├── sources.py              주제 정의 + arXiv/OpenAlex/Crossref 수집 + 채점
│   ├── fulltext.py             OA PDF 본문 추출 (pypdf 선택 의존)
│   ├── schema.py               요약 스키마 + 검증 (표준 라이브러리만)
│   ├── render.py               Jekyll 포스트 렌더링 + 게시 이력
│   ├── summarize.py            Anthropic API 요약 (폴백 경로 전용)
│   ├── requirements.txt        pypdf
│   └── requirements-api.txt    + anthropic, pydantic
├── .github/workflows/daily-paper.yml   수동 폴백
├── _layouts/ _includes/ assets/        경량 커스텀 Jekyll 테마
├── _posts/                             생성된 요약
├── data/state.json                     게시 이력 — 중복 방지
└── index.html  archive.md  about.md  _config.yml
```

---

## 커스터마이징

| 바꾸고 싶은 것 | 고칠 파일 |
| --- | --- |
| 요약 문체·용어 규칙 | `scripts/SUMMARY_SPEC.md` |
| 실행 절차 (재시도 횟수, 커밋 범위 등) | `scripts/ROUTINE.md` |
| 주제 추가·수정 | `scripts/sources.py`의 `TOPICS` |
| 요약 항목 추가·삭제 | `scripts/schema.py` + `scripts/render.py` + `SUMMARY_SPEC.md` (셋 다) |
| 논문 선정 기준 | `scripts/sources.py`의 `score_paper()` / `is_on_topic()` |
| 사이트 디자인 | `assets/css/style.css` |
| 게시 시각·모델 | <https://claude.ai/code/routines> 에서 루틴 편집 |

---

## 주의

요약은 자동 생성물이다. 원문의 뉘앙스나 세부 조건을 놓칠 수 있으므로
**인용·활용 전에는 반드시 원문을 확인할 것.** 각 글 상단에 요약 근거
(논문 전문 / 초록)를 표시한다.
