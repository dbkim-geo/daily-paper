# 운영 메모

파이프라인이 매일 어떻게 도는지, 멈췄을 때 어디를 보는지 적어 둔다.
저장소 구조와 주제·가중치 커스터마이징은 `README.md`를 본다.

## 어떻게 도는가

이 저장소는 **로컬 머신의 cron**으로 돈다.

```
30 8 * * *  /home/kei/geo-workspace/daily-paper/scripts/run_daily.sh
```

`scripts/run_daily.sh`가 `scripts/ROUTINE.md`의 절차를 그대로 수행한다.

1. `git pull --ff-only`
2. `.venv/bin/python scripts/daily_paper.py select` — 3개 API에서 후보를 모아 한 편 선정
3. 신규 논문이 없으면 **아무것도 커밋하지 않고 종료**
4. `claude -p --model opus`로 `data/summary.json` 생성
5. `daily_paper.py write`로 스키마 검증 후 `_posts/`에 렌더링.
   실패하면 오류 메시지를 그대로 되먹여 **최대 3회 재시도**
6. `_posts`와 `data/state.json`만 커밋·푸시 → GitHub Pages가 빌드

`flock`으로 중복 실행을 막고, 로그는 `~/.local/state/daily-paper/run.log`에 쌓인다.

### 왜 클라우드가 아니라 로컬인가

처음에는 Claude 루틴(스케줄 클라우드 에이전트)으로 짰으나, 클라우드 샌드박스의
egress 프록시가 `export.arxiv.org` / `api.openalex.org` / `api.crossref.org` 로의
CONNECT를 403으로 거부했다. 조직 egress 정책이라 코드로 우회할 수 없다.

로컬 머신은 네트워크가 열려 있고 항상 켜져 있으며, Claude Code를 헤드리스로 부르면
구독 그대로 동작해 **API 과금이 없다.** 그래서 로컬 cron으로 정착했다.

`.github/workflows/daily-paper.yml`은 이 경로가 막혔을 때를 위한 폴백이다.
`ANTHROPIC_API_KEY` Secret을 등록하면 `workflow_dispatch`로 수동 실행할 수 있다
(전문 요약 1회 약 $0.15~0.30).

## 주제 구성 — 계획이 메인, 공간분석은 도구

**도시계획·환경계획이 주제고, RS·GIS·GeoAI·GeoXAI는 그것을 푸는 수단이다.**
초기에는 도구도 각각 주제였는데, 그러면 절반의 날에 대기보정 알고리즘이나
quantum pooling 같은 순수 방법론 논문이 뽑혔다. 그래서 도구를 주제에서 내렸다.

주제는 4개이며 `ROTATION`이 6일 주기로 돈다. 계획이 6일 중 4일을 차지한다.

```
도시계획 → 환경계획 → 탄소중립 → 도시계획 → 환경계획 → 탄소저감
```

후보가 되려면 **두 조건을 모두** 만족해야 한다(`is_on_topic`).

1. 주제 키워드 — 제목에 1개 이상 또는 초록에 2개 이상. 무엇에 관한 연구인가.
2. 도구 키워드(`TOOL_KEYWORDS`) — 제목이나 초록에 1개 이상. 어떻게 푸는가.

2번이 없으면 설문·정책담론만 다룬 계획 이론 논문이 들어오고, 1번이 없으면
RS·GIS 자체를 다룬 방법론 논문이 들어온다. 도구가 제목에까지 드러나면
`TOOL_TITLE_BONUS`(2점)를 준다.

주제나 비중을 바꾸려면 `TOPICS`와 `ROTATION`만 고치면 된다.

**남은 한계.** 탄소 계열은 계획 두 주제보다 범위가 넓어, 재료과학이나
대기화학 논문이 상위에 섞일 때가 있다("net zero"와 "deep learning"이 초록에
함께 나오면 통과한다). 계획 주제는 이 문제가 거의 없다.

## 연구 대상지 기준

**한국·미국·중국·유럽에서 수행된 연구만 받는다.** 공간정보 방법론을 특정 대상지에
적용한 연구가 관심사이므로, 대상지가 드러나지 않는 순수 방법론 연구와 전 지구 규모
연구도 함께 걸린다.

제목과 초록의 지명으로 판정한다(`region_ok`). 제목의 지명은 대상지일 확률이 높아
`REGION_TITLE_WEIGHT`(3배)로 센다. 통과 조건은 두 가지다.

1. `INCLUDED_REGION_RE`가 한 번 이상 걸릴 것
2. 포함 지역 점수가 제외 지역 점수보다 클 것

2번은 비교 연구와 스쳐가는 언급을 가른다. 케냐 연구가 유럽을 한 번 언급했다고
통과시키면 안 되지만, "Beijing과 Delhi 비교"는 통과해야 한다.

**반드시 단어 경계(`\b`)를 쓴다.** 없으면 `causal`이 `usa`로, `Indiana`가 `India`로,
`Indochina`가 `china`로 잡힌다. 또 `African American`은 미국 연구의 표현이므로
아프리카로 세지 않도록 부정형 전방탐색으로 예외 처리했다. `american`은 포함 목록에
넣지 않는다 — `Latin American`, `African American`과 겹친다.

지역을 조정하려면 `INCLUDED_REGION_RE` / `EXCLUDED_REGION_RE`만 고치면 된다.

**후보가 크게 준다.** 이 기준을 더하면서 주제당 후보가 절반 이하로 떨어져
(도시계획 48 → 9건) OpenAlex 수집을 2페이지(`OPENALEX_PAGES`, 최대 400건)로 늘렸다.
현재 주제당 12~19건이다. 전문 필수 조건과 겹치므로, 더 줄면 페이지를 늘리는 것이
가장 직접적인 대응이다.

## 저널 품질 기준

무명 저널이 뽑히던 문제를 막기 위해 `scripts/sources.py` 상단에 기준을 모아 뒀다.
바꾸고 싶으면 그 상수만 고치면 된다.

| 상수 | 하는 일 |
| --- | --- |
| `EXCLUDED_PUBLISHERS` | MDPI · Frontiers · PLOS · Hindawi 배제. 상위 계열사명까지 훑으므로 자회사 브랜드로 실려도 걸린다 |
| `EXCLUDED_JOURNAL_RE` | 출판사명으로는 안 잡히는 megajournal을 저널 이름으로 배제. Springer의 `Discover *` 시리즈, Heliyon, Scientific Reports 등 |
| `MIN_JOURNAL_IMPACT` | 저널 등급 하한. OpenAlex `2yr_mean_citedness`(임팩트팩터 대응 지표) 기준 1.0 |
| `PRESTIGE_MAX` | 등급 가점 상한 10점. `3.0 * log1p(IF)`로 계산해 IF 0.6↔5의 차이는 크게, 15↔30의 차이는 작게 본다 |
| `REVIEW_TITLE_RE` | 리뷰 논문 제목 배제. OpenAlex `type:article` 필터의 백스톱이다 |

이와 별개로 `source.type != "journal"`인 매체(대학 리포지토리, 프로시딩)와
철회 논문(`is_retracted`)도 뺀다.

몇 가지 알아둘 점:

- **arXiv preprint에는 이 기준을 적용하지 않는다.** 저널 게재논문이 아니라
  판정 대상이 아니고, 등급 가점을 못 받아 자연히 뒤로 밀린다.
- **저널 등급 조회에 실패하면 배제하지 않고 가점만 0으로 둔다.** 조회 실패로
  그날 게시를 통째로 건너뛰는 것이 더 나쁘기 때문이다.
- 등급 조회는 주제당 요청 1~2회다(`fetch_journal_impact`가 50개씩 묶어 조회).
- 로그에 `품질 기준 제외: ...`로 무엇이 몇 건 걸렸는지 남는다.

## 전문 확보가 어려운 이유와 대응

저널 등급을 올리면 **출판사가 봇을 막아** 전문을 못 받는 일이 급격히 늘어난다.
유료화가 아니라 접근 차단이 원인이다. 실측(상위 15건 기준)으로 실제 다운로드
성공률은 Remote Sensing 3/15, GeoAI 4/15였다.

| 호스트 | 응답 |
| --- | --- |
| `sciencedirect.com` (Elsevier) | HTTP 403 |
| `link.springer.com`, `nature.com` | HTTP 200 + HTML 안내 페이지 (3KB) |
| `tandfonline.com` (T&F) | 대체로 403 |
| `arxiv.org`, `copernicus.org` | 정상 |

**OpenAlex에 PDF 링크가 있다는 것과 실제로 받아진다는 것은 다르다.**
링크 존재율은 94%지만 실제 확보율은 20~27%다. 이 둘을 혼동하면 안 된다.

대응은 세 단계다.

1. `best_oa_location` 외에 `locations`의 리포지토리 사본을 대체 경로로 함께 시도한다
   (`Paper.alt_pdf_urls`). 다만 갓 나온 논문은 아직 사본이 없는 경우가 많다.
2. 그래도 실패하면 **같은 논문의 arXiv preprint를 제목으로 찾는다**
   (`find_arxiv_pdf`). 저널 등급을 낮추지 않고 전문을 얻는 유일한 경로다.
   GeoAI·RS 계열은 잘 걸리고, 환경·계획 계열은 arXiv에 잘 안 올라와 잘 안 걸린다.
3. 그래도 안 되면 점수가 `FULLTEXT_FALLBACK_MARGIN`(4.0점) 이내인 차순위 논문으로
   최대 10건까지 넘어간다. 이 범위를 넘어서까지 점수를 희생하지는 않으므로,
   전부 막히면 초록 기반 요약으로 진행한다.

`extract_pdf_text`는 Content-Type이나 URL 확장자를 믿지 않고 **응답 바이트가
`%PDF`로 시작하는지**로 판정한다. Springer Nature가 `.pdf` 주소에 HTML을
돌려주기 때문이다. 이 검사가 없으면 HTML을 pypdf에 먹여 엉뚱한 파싱 오류가 난다.

## 원문 키워드와 대표 그림

포스트에는 요약과 별개로 **원문에서 가져온 것** 두 가지가 들어간다.

**원문 키워드** — 전문에서 저자가 직접 적은 키워드를 뽑아 front matter의
`paper_keywords`와 본문 "원문 키워드" 절에 싣는다(`extract_author_keywords`).
OpenAlex도 `keywords`를 주지만 자동 생성이라 "Vegetation (pathology)",
"Baseline (sea)" 같은 오류가 섞인다. **그건 쓰지 않는다.** 원문에 키워드가
없으면(arXiv 판본 등) 지어내지 않고 절을 통째로 생략한다.

**대표 그림** — PDF에 내장된 이미지 중 본문에서 가장 먼저 나오는 큰 그림을
고른다(`extract_representative_figure`). 보통 Figure 1이라 연구 지역도나
방법론 흐름도가 잡혀 대표성이 있다. `assets/figures/`에 저장하고 포스트 상단에
출처와 함께 넣는다.

선별 규칙은 실측에 근거한다. 로고·러닝헤더는 91×91 같은 소형이고 진짜 그림은
26만~145만 화소였다.

| 기준 | 값 | 이유 |
| --- | --- | --- |
| `FIGURE_SKIP_PAGES` | 1쪽 제외 | 표지에는 학술지 로고·QR만 있다 |
| `FIGURE_MIN_PIXELS` | 150,000 | 로고(8천)와 그림(26만+)을 가른다 |
| 같은 이미지가 3쪽 이상 등장 | 제외 | 러닝 헤더다 |
| 종횡비 | 0.3~5.0 | 얇은 장식 띠를 거른다 |
| `FIGURE_MAX_WIDTH` | 1200px | 저장 용량 억제 |

**저작권.** `FIGURE_OK_LICENSES`(CC BY / BY-SA / BY-NC / BY-NC-SA / CC0 /
public domain)일 때만 싣는다. **ND(변경 금지) 계열과 라이선스 미상은 제외한다** —
그림을 축소해 싣는 것이 2차적 저작물 작성에 해당하기 때문이다. 포스트에는
저작자·저널·연도·라이선스를 함께 표기한다.

그림은 벡터로 그린 도표는 잡히지 않는다(내장 이미지가 아니라서). 그런 논문은
그림 없이 게시된다. Pillow가 없으면 조용히 건너뛴다.

## 손으로 돌리기

```bash
# 커밋·푸시 없이 선정~렌더링까지만 (결과는 _posts/ 에 생기므로 확인 후 지운다)
DRY_RUN=1 scripts/run_daily.sh

# 실제로 한 편 게시
scripts/run_daily.sh

# 로그 보기
tail -f ~/.local/state/daily-paper/run.log
```

## 걸리기 쉬운 곳

- **반드시 `.venv/bin/python`으로 실행한다.** 시스템 `python3`에는 pypdf가 없어
  전문(PDF) 추출을 건너뛰고 초록 기반 요약으로 조용히 떨어진다.
- **GitHub Pages Source는 `main` / `(root)`의 "Deploy from a branch"다.**
  `.github/workflows/daily-paper.yml`은 Pages 배포용이 아니므로 Source로
  "GitHub Actions"를 고르면 사이트가 뜨지 않는다.
- **저장소는 public이어야 한다.** private이면 무료 계정에서 Pages가 404다.
- 논문 API는 가끔 개별적으로 실패한다(arXiv 타임아웃 등). 3개 소스 중 일부만
  실패하면 나머지로 계속 진행하므로 로그에 `실패`가 한 줄 있어도 정상이다.
- 전문 추출은 `scripts/fulltext.py`의 두 상수로 조절한다.
  `EXTRACT_CHAR_LIMIT`(400,000자)까지 페이지를 읽어 참고문헌을 떼어낸 뒤,
  남은 본문을 `FULLTEXT_CHAR_LIMIT`(200,000자)로 자른다. **추출 예산이 최종
  한도보다 넉넉해야** References 위치를 찾을 수 있다. 예산에서 먼저 멈추면
  참고문헌 제거가 작동하지 않고 본문이 대신 잘린다.
  실제로 잘리는 경우 로그에 `한도(...)를 넘어 뒷부분을 자른다`가 남는다.

## 기준 문서

- `scripts/ROUTINE.md` — 일일 실행 절차
- `scripts/SUMMARY_SPEC.md` — 요약 작성 규칙과 13개 필드 스키마
- `README.md` — 저장소 구조, 주제·가중치 커스터마이징
