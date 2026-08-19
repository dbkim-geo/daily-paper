# 인수인계 — 2026-08-19

이 문서는 다음 세션이 바로 이어받기 위한 기록이다. 작업이 끝나면 지워도 된다.

## 현재 상태

파이프라인과 사이트는 **완성되어 푸시된 상태**다 (`858a529`).
다만 **자동 실행 경로가 막혀 있어 아직 한 편도 게시되지 않았다.**

| 항목 | 상태 |
| --- | --- |
| 논문 수집·채점·선정 (`select`) | ✅ 완성, 로컬에서 8개 주제 전부 검증 |
| 요약 스키마·검증·렌더링 (`write`) | ✅ 완성, 표준 라이브러리만으로 동작 검증 |
| Jekyll 사이트 (테마·아카이브·RSS) | ✅ 완성, Liquid 문법 검증 |
| Claude 루틴 | ⛔ **네트워크 차단으로 실패 → 비활성화됨** |
| GitHub Pages 설정 | ❓ 미확인 (Settings → Pages 확인 필요) |
| 첫 포스트 | ❌ 아직 없음 |

## 막힌 지점 (최우선 과제)

Claude 루틴(`trig_01JJ2Jc6ZPv1wkXGSmXAtByg`)을 2026-08-19 00:56 UTC에 수동 실행한 결과,
클라우드 샌드박스의 egress 프록시가 논문 API로의 CONNECT를 **403으로 거부**했다.

```
export.arxiv.org  -> 000 (connect_rejected)
api.openalex.org  -> 000 (connect_rejected)
api.crossref.org  -> 000 (connect_rejected)
```

샌드박스의 `/root/.ccr/README.md`는 이를 조직 egress 정책에 의한 차단으로 규정하고
우회를 금지한다. 따라서 코드로 해결할 수 없다.

루틴은 매일 실패 알림만 보내게 되므로 **`enabled: false`로 꺼 두었다.**
관리: <https://claude.ai/code/routines/trig_01JJ2Jc6ZPv1wkXGSmXAtByg>

## 다음 세션에서 시도할 것 (권장 순서)

### 1순위 — 다른 환경으로 루틴 재시도 (가장 저렴한 시도)

계정에 `Default` 환경이 두 개 있다. 실패한 쪽은 `env_01L5JjsmydmaMHC8WQ58mQk7`.
다른 쪽 `env_01JqT7A19DFoLHFR2nBSqpTC`는 egress 정책이 다를 수 있다.
루틴의 `job_config.ccr.environment_id`만 바꿔 수동 실행해 보면 4분 안에 판별된다.

### 2순위 — egress 허용목록에 세 호스트 추가

가능하다면 Claude Code 환경 설정에서 위 세 호스트를 허용한다.
조직 정책이면 관리자 권한이 필요할 수 있다.

### 3순위 — GitHub Actions + claude-code-action (추가 비용 없음)

GitHub 호스티드 러너는 egress 제한이 없다. **Max 구독을 그대로 쓰므로 API 과금은 없다.**

1. 로컬에서 `claude setup-token` 실행 → OAuth 토큰 발급
2. 저장소 Secret에 `CLAUDE_CODE_OAUTH_TOKEN`으로 등록
3. 워크플로 작성: `select` 실행 → `anthropics/claude-code-action@v1`로 요약
   (prompt에 `scripts/ROUTINE.md`를 따르도록 지시) → `write` → 커밋·푸시
4. `claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}` 사용

주의: 스케줄 워크플로는 GitHub이 마지막으로 cron을 수정한 사용자에게 귀속시킨다.
봇이 워크플로 파일을 건드리지 않게 해야 `allowed_bots` 문제가 생기지 않는다.

### 4순위 — API 키 폴백

`.github/workflows/daily-paper.yml`이 이미 준비되어 있다 (`workflow_dispatch` 전용).
`ANTHROPIC_API_KEY` Secret만 등록하면 즉시 동작한다. 전문 요약 1회 약 $0.15~0.30.

## 검증 완료된 사항 (다시 확인할 필요 없음)

- 3개 API 수집: 8개 주제 전부 후보 24~70건 확보 (로컬 네트워크 기준)
- 채점 로직: 미래 발행일 가점 버그와 주제 무관 논문 선정 버그를 수정함
- 중복 방지: DOI 대소문자·URL 형식 차이를 정규화해 판정
- 포스트 렌더링: 제목의 따옴표·콜론·앰퍼샌드가 YAML에서 안전하게 이스케이프됨
- 스키마 검증: 오류를 전부 모아 한국어로 보고, `write`가 exit 1로 실패
- 표준 라이브러리만으로 `select` → `write` 전 구간 동작 (pypdf 없으면 초록 모드)
- Liquid 템플릿 태그 균형

## 검증하지 못한 사항

- **Jekyll 실제 빌드** — 이 개발 환경에 Ruby·sudo·컨테이너가 없어 실행 불가.
  GitHub Pages 첫 빌드에서 확인해야 한다.
- **Claude가 생성한 실제 요약의 품질** — 아직 한 번도 생성되지 않았다.

## 참고

- 저장소 구조와 커스터마이징 방법: `README.md`
- 루틴 실행 절차: `scripts/ROUTINE.md`
- 요약 작성 규칙·스키마: `scripts/SUMMARY_SPEC.md`
