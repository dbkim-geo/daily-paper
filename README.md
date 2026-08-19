# Daily Paper

매일 아침 8시 30분(KST)에 논문 한 편을 자동으로 골라 한국어로 요약하고
GitHub Pages에 게시하는 파이프라인.

**사이트:** https://dbkim-geo.github.io/daily-paper/

---

## 동작 방식

```
23:30 UTC (= 08:30 KST)
   │
   ├─ 1. 주제 선택      날짜 기반으로 8개 주제를 순환
   ├─ 2. 후보 수집      arXiv + OpenAlex + Crossref
   ├─ 3. 채점·선정      관련도 + 최신성 + 초록 충실도 + 전문 접근성
   ├─ 4. 전문 확보      OA PDF가 있으면 본문 텍스트 추출 (pypdf)
   ├─ 5. 요약 생성      Claude Opus 5, 구조화 출력(Pydantic 스키마)
   ├─ 6. 포스트 작성    _posts/YYYY-MM-DD-slug.md
   └─ 7. 커밋·푸시      → GitHub Pages가 사이트를 재빌드
```

주제 순환: `GeoAI → GeoXAI → 환경계획 → 도시계획 → 탄소중립 → 탄소저감 → GIS → Remote Sensing`

당일 주제에 게시 가능한 신규 논문이 없으면 다음 주제로 넘어가므로 매일 한 편이 보장된다.
이미 게시한 논문은 DOI · arXiv ID · 제목 해시로 걸러낸다 (`data/state.json`).

> **Google Scholar 추천 논문은 연동하지 않는다.** 공개 API가 없고 추천 피드가 개인 로그인
> 세션을 요구해 자동화가 불가능하다. 위 키워드 기반 수집이 그 대체다.

---

## 최초 설정 (3단계)

### 1. Anthropic API 키를 저장소 Secret으로 등록

1. https://console.anthropic.com/settings/keys 에서 API 키 발급
2. 저장소 → **Settings → Secrets and variables → Actions → New repository secret**
3. Name: `ANTHROPIC_API_KEY`, Secret: 발급받은 키

### 2. GitHub Pages 활성화

저장소 → **Settings → Pages**

- **Source**: `Deploy from a branch`
- **Branch**: `main` / `/ (root)`

Jekyll 빌드는 GitHub Pages가 자동으로 수행한다. 별도 빌드 워크플로가 필요 없다.

### 3. Actions 쓰기 권한 확인

저장소 → **Settings → Actions → General → Workflow permissions**
→ **Read and write permissions** 선택 (봇이 포스트를 커밋해야 한다)

### 첫 실행

**Actions → Daily paper → Run workflow** 로 즉시 한 편을 생성해 볼 수 있다.
`dry_run`을 체크하면 API 호출 없이 후보 선정 결과만 확인한다.

---

## 로컬 실행

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# 후보 선정만 확인 (API 호출 없음, 무료)
.venv/bin/python scripts/daily_paper.py --dry-run

# 특정 주제로 고정
.venv/bin/python scripts/daily_paper.py --dry-run --topic geoai

# 실제 포스트 생성
.venv/bin/python scripts/daily_paper.py
```

| 옵션 | 설명 |
| --- | --- |
| `--date YYYY-MM-DD` | 게시 날짜 지정 (기본: 오늘 KST) |
| `--topic KEY` | 주제 고정. `geoai`, `geoxai`, `env-planning`, `urban-planning`, `carbon-neutral`, `carbon-reduction`, `gis`, `remote-sensing` |
| `--window-days N` | 저널 논문 검색 기간(일). 기본 240 |
| `--dry-run` | 후보 선정까지만. Claude API를 호출하지 않는다 |
| `--no-fulltext` | PDF 전문 추출을 건너뛰고 초록만으로 요약 (비용 대폭 절감) |

### 사이트 로컬 미리보기 (선택)

Ruby가 설치되어 있어야 한다.

```bash
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000/daily-paper/
```

---

## 비용

Claude Opus 5 기준 ($5 / 1M input tokens, $25 / 1M output tokens):

| 모드 | 하루 | 한 달 |
| --- | --- | --- |
| 전문 기반 요약 (기본) | 약 $0.15 ~ $0.30 | 약 **$5 ~ $9** (7,000~13,000원) |
| 초록만 (`--no-fulltext`) | 약 $0.02 ~ $0.05 | 약 **$0.6 ~ $1.5** |

전문 요약이 방법론·결과의 정확도에서 확실히 낫다. 비용을 줄이려면
워크플로의 실행 명령에 `--no-fulltext`를 추가하거나,
`scripts/summarize.py`의 `MODEL`을 `claude-sonnet-5`로 바꾸면 된다.

---

## 구조

```
.
├── .github/workflows/daily-paper.yml   매일 실행되는 스케줄러
├── scripts/
│   ├── daily_paper.py                  오케스트레이터 (CLI 진입점)
│   ├── sources.py                      주제 정의 + arXiv/OpenAlex/Crossref 수집 + 채점
│   ├── summarize.py                    Claude API 요약 (Pydantic 구조화 출력)
│   ├── render.py                       Jekyll 포스트 렌더링 + 게시 이력 관리
│   └── requirements.txt
├── _layouts/ _includes/ assets/        경량 커스텀 Jekyll 테마
├── _posts/                             생성된 요약 (봇이 커밋)
├── data/state.json                     게시 이력 — 중복 게시 방지
├── index.html  archive.md  about.md
└── _config.yml
```

---

## 커스터마이징

**주제 추가·수정** — `scripts/sources.py`의 `TOPICS` 튜플을 편집한다.
각 주제는 arXiv 검색식(`arxiv`), OpenAlex/Crossref 검색어(`scholarly`),
관련도 채점용 키워드(`keywords`)를 갖는다.

**요약 항목 변경** — `scripts/summarize.py`의 `PaperSummary` 스키마와
`scripts/render.py`의 `render_markdown()`을 함께 수정한다.

**문체·용어 규칙 변경** — `scripts/summarize.py`의 `SYSTEM_PROMPT`.

**게시 시각 변경** — 워크플로의 cron. UTC 기준이므로 KST에서 9시간을 뺀다.
(예: 07:00 KST → `0 22 * * *`)

> GitHub Actions의 스케줄 실행은 플랫폼 부하에 따라 수 분~수십 분 지연될 수 있다.
> 정확한 정시 게시가 필요하면 cron을 조금 앞당겨 두는 편이 낫다.

---

## 주의

요약은 자동 생성물이다. 원문의 뉘앙스나 세부 조건을 놓칠 수 있으므로
**인용·활용 전에는 반드시 원문을 확인할 것.** 각 글 상단에 요약 근거
(논문 전문 / 초록)를 표시한다.
