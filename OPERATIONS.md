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
- 전문 추출은 `FULLTEXT_CHAR_LIMIT`(`scripts/fulltext.py`, 현재 60,000자)에서
  잘린다. 긴 논문은 Discussion 이후가 잘려 요약 근거에서 빠질 수 있다.

## 기준 문서

- `scripts/ROUTINE.md` — 일일 실행 절차
- `scripts/SUMMARY_SPEC.md` — 요약 작성 규칙과 13개 필드 스키마
- `README.md` — 저장소 구조, 주제·가중치 커스터마이징
