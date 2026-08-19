# 일일 실행 절차 (Claude 루틴용)

매일 08:30 KST에 클라우드 세션이 이 문서를 읽고 아래를 수행한다.
문서에 없는 동작은 하지 않는다.

## 1. 논문 선정

```bash
pip install pypdf 2>/dev/null || true
python3 scripts/daily_paper.py select
```

- `pip install`이 실패해도 무시하고 진행한다. 전문(PDF) 추출만 건너뛰고
  초록 기반 요약으로 자동 전환된다.
- `data/candidate.json`이 생기면 2단계로 간다.
- "모든 주제에서 신규 논문을 찾지 못했다"가 출력되고 파일이 없으면 오늘은
  게시할 것이 없다. **아무것도 커밋하지 말고** 그 사실만 보고하고 종료한다.

## 2. 요약 작성

- `scripts/SUMMARY_SPEC.md`를 읽고 그 규격을 정확히 따른다.
  이것이 작성 규칙의 유일한 기준이다.
- `data/candidate.json`을 읽는다.
  - `full_text`가 비어 있지 않으면 그것을 근거로 방법론과 결과를 구체적으로 쓴다.
  - 비어 있으면 `paper.abstract`만 근거로 삼는다. 방법론·결과는 초록에서 확인
    가능한 범위까지만 쓰고, "초록 기준"임을 문장 안에서 밝힌다.
- 논문에 없는 내용을 지어내지 않는다. 추측으로 수치나 절차를 채우지 않는다.
- 본문은 한국어로 쓰되 학술 전문용어(Random Forest, NDVI, Sentinel-2, SHAP,
  urban heat island 등)는 영어 원문 그대로 둔다.
- `data/summary.json`에 **JSON 객체 하나만** 쓴다. 코드펜스나 설명 문장을 붙이지 않는다.

## 3. 검증 및 렌더링

```bash
python3 scripts/daily_paper.py write
```

- 실패하면 어떤 필드가 왜 잘못됐는지 한국어로 출력된다. `data/summary.json`을
  고쳐 다시 실행한다.
- **최대 3회까지 시도한다.** 그래도 실패하면 커밋하지 말고 마지막 오류 메시지를
  보고하고 종료한다.
- 성공하면 `_posts/`에 새 포스트가 생기고 임시 파일이 정리된다.

## 4. 커밋 및 푸시

```bash
git config user.name  "daily-paper-bot"
git config user.email "dongbum80@gmail.com"
git add _posts data/state.json
git commit -m "post: <새로 생긴 포스트 파일명에서 .md를 뺀 것>"
git push
```

- `_posts`와 `data/state.json` 외에는 커밋하지 않는다.
  `data/candidate.json`과 `data/summary.json`은 커밋 대상이 아니다.
- 푸시가 실패하면 원인을 보고한다. 강제 푸시나 히스토리 재작성은 하지 않는다.

## 마무리 보고

어떤 주제로 어떤 논문을 게시했는지, 요약 근거가 전문인지 초록인지를
두세 문장으로 보고한다.
