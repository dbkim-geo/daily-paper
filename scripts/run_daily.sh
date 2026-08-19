#!/usr/bin/env bash
#
# 로컬 머신에서 매일 한 편을 선정·요약·게시한다.
#
# 클라우드 루틴은 샌드박스 egress 정책이 논문 API를 막아 쓸 수 없었다.
# 이 머신은 네트워크가 열려 있고 Claude Code도 구독으로 동작하므로
# 여기서 도는 것이 추가 비용 없이 가장 확실하다. (자세한 경위는 HANDOFF.md)
#
# cron 등록:  30 8 * * *  /home/kei/geo-workspace/daily-paper/scripts/run_daily.sh
#
# DRY_RUN=1 을 주면 선정·요약·렌더링까지만 하고 커밋과 푸시는 건너뛴다.

set -uo pipefail

REPO="/home/kei/geo-workspace/daily-paper"
PY="$REPO/.venv/bin/python"
CLAUDE="/home/kei/.nvm/versions/node/v20.20.2/bin/claude"

STATE_DIR="${XDG_STATE_HOME:-$HOME/.local/state}/daily-paper"
LOG="$STATE_DIR/run.log"
LOCK="$STATE_DIR/run.lock"

mkdir -p "$STATE_DIR"

log() { printf '%s | %s\n' "$(date '+%F %T')" "$*" >>"$LOG"; }

# 실패해도 cron이 계속 돌므로, 어디서 멈췄는지 로그만 보면 알 수 있게 한다.
die() { log "실패: $*"; log "=== 종료 (실패) ==="; exit 1; }

# 앞선 실행이 아직 돌고 있으면 겹쳐 돌지 않는다.
exec 9>"$LOCK"
flock -n 9 || { log "이전 실행이 진행 중이라 건너뛴다"; exit 0; }

cd "$REPO" || die "저장소 디렉터리로 이동 불가"

log "=== 시작 ==="

[ -x "$PY" ]     || die "venv 파이썬 없음: $PY"
[ -x "$CLAUDE" ] || die "claude CLI 없음: $CLAUDE"

# 원격이 앞서 있으면 푸시가 막히므로 먼저 맞춘다. 머지 커밋은 만들지 않는다.
git pull --ff-only --quiet || die "git pull 실패 (로컬과 원격이 갈라졌을 수 있다)"

# 1. 논문 선정 -------------------------------------------------------------
rm -f data/candidate.json data/summary.json

if ! "$PY" scripts/daily_paper.py select >>"$LOG" 2>&1; then
    die "select 단계 오류"
fi

if [ ! -s data/candidate.json ]; then
    log "오늘은 신규 논문이 없다. 게시하지 않고 종료한다."
    log "=== 종료 (게시 없음) ==="
    exit 0
fi

# 2~3. 요약 작성과 검증 ----------------------------------------------------
# write가 실패하면 오류 메시지를 그대로 되돌려주고 다시 쓰게 한다. 최대 3회.
BASE_PROMPT='scripts/SUMMARY_SPEC.md 와 data/candidate.json 을 읽고, 규격에 정확히 맞는 요약을 data/summary.json 에 JSON 객체 하나로 작성하라.

- SUMMARY_SPEC.md 가 작성 규칙의 유일한 기준이다. 13개 필드가 전부이며 하나라도 빠지거나 추가되면 안 된다.
- candidate.json 의 full_text 가 비어 있지 않으면 그것을 근거로 방법론과 결과를 구체적으로 쓴다. 비어 있으면 paper.abstract 만 근거로 삼고 "초록 기준"임을 문장 안에서 밝힌다.
- 논문에 없는 내용을 지어내지 않는다. 추측으로 수치나 절차를 채우지 않는다.
- basis 필드에는 candidate.json 의 basis 값을 그대로 복사한다.
- data/summary.json 파일을 쓰는 것 외에 다른 파일을 만들거나 고치지 않는다.'

published=0
for attempt in 1 2 3; do
    log "요약 시도 $attempt/3"

    if [ "$attempt" -eq 1 ]; then
        PROMPT="$BASE_PROMPT"
    else
        PROMPT="$BASE_PROMPT

이전 시도의 data/summary.json 이 검증에 실패했다. 아래 오류를 보고 고쳐 다시 써라.

$(cat "$STATE_DIR/last_error.txt" 2>/dev/null)"
    fi

    if ! "$CLAUDE" -p "$PROMPT" \
            --model opus \
            --permission-mode acceptEdits \
            --allowedTools Read Write Glob Grep \
            >>"$LOG" 2>&1; then
        log "claude 호출 실패 (시도 $attempt)"
        continue
    fi

    if [ ! -s data/summary.json ]; then
        log "summary.json 이 생성되지 않았다 (시도 $attempt)"
        continue
    fi

    if "$PY" scripts/daily_paper.py write >"$STATE_DIR/last_error.txt" 2>&1; then
        cat "$STATE_DIR/last_error.txt" >>"$LOG"
        published=1
        break
    fi

    cat "$STATE_DIR/last_error.txt" >>"$LOG"
    log "write 검증 실패 (시도 $attempt)"
done

[ "$published" -eq 1 ] || die "3회 시도 후에도 요약이 규격을 통과하지 못했다"

# 4. 커밋과 푸시 -----------------------------------------------------------
post=$(git status --porcelain _posts | awk '/^\?\?/ {print $2}' | head -1)
[ -n "$post" ] || die "새 포스트 파일을 찾지 못했다"

slug=$(basename "$post" .md)

if [ "${DRY_RUN:-0}" = "1" ]; then
    log "DRY_RUN: 커밋·푸시를 건너뛴다. 생성된 포스트: $post"
    log "=== 종료 (dry run) ==="
    exit 0
fi

git config user.name  "daily-paper-bot"
git config user.email "dongbum80@gmail.com"

git add _posts data/state.json                  || die "git add 실패"
git commit --quiet -m "post: $slug"             || die "git commit 실패"
git push --quiet                                || die "git push 실패"

log "게시 완료: $slug"
log "=== 종료 (성공) ==="
