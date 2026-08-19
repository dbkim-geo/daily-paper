"""OA PDF에서 본문 텍스트를 추출한다.

표준 라이브러리 + 선택적 pypdf만 사용한다. pypdf가 없으면 조용히 빈 문자열을
반환하고, 파이프라인은 초록 기반 요약으로 넘어간다.
"""

from __future__ import annotations

import io
import re
import urllib.request

from sources import USER_AGENT

# 요약 프롬프트에 넣을 최대 문자 수. 초록만 있을 때보다 방법론/결과 정확도가 크게 오른다.
# 참고문헌을 떼어낸 본문 기준이며, 일반적인 학술 논문은 여기에 통째로 들어간다.
FULLTEXT_CHAR_LIMIT = 200_000

# 페이지에서 읽어들일 원문 예산. FULLTEXT_CHAR_LIMIT보다 넉넉해야 References
# 위치를 찾아 잘라낼 수 있다. 여기서 먼저 멈추면 참고문헌 제거가 작동하지 않는다.
EXTRACT_CHAR_LIMIT = 2 * FULLTEXT_CHAR_LIMIT

PDF_BYTE_LIMIT = 25 * 1024 * 1024


def extract_pdf_text(pdf_url: str) -> str:
    """PDF 본문 텍스트. 실패하면 빈 문자열을 돌려준다."""
    try:
        from pypdf import PdfReader
    except ImportError:
        print("    pypdf 미설치 — 전문 추출을 건너뛴다")
        return ""

    try:
        req = urllib.request.Request(pdf_url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            ctype = (resp.headers.get("Content-Type") or "").lower()
            if "pdf" not in ctype and not pdf_url.lower().endswith(".pdf"):
                return ""
            data = resp.read(PDF_BYTE_LIMIT)
    except Exception as exc:
        print(f"    전문 다운로드 실패: {exc}")
        return ""

    try:
        reader = PdfReader(io.BytesIO(data))
        chunks, total = [], 0
        for page in reader.pages:
            text = page.extract_text() or ""
            chunks.append(text)
            total += len(text)
            if total > EXTRACT_CHAR_LIMIT:
                break
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(chunks))
        text = re.sub(r"[ \t]{2,}", " ", text).strip()
    except Exception as exc:
        print(f"    전문 파싱 실패: {exc}")
        return ""

    # 참고문헌 이후는 요약에 불필요하므로 잘라낸다.
    cut = re.search(r"\n\s*(References|REFERENCES|Bibliography)\s*\n", text)
    if cut and cut.start() > 3000:
        text = text[:cut.start()]

    if len(text) <= 800:
        return ""

    # 잘림은 요약 근거의 손실이므로 조용히 넘어가지 않고 로그에 남긴다.
    if len(text) > FULLTEXT_CHAR_LIMIT:
        print(f"    본문이 {len(text):,}자로 한도({FULLTEXT_CHAR_LIMIT:,}자)를 넘어 뒷부분을 자른다")

    return text[:FULLTEXT_CHAR_LIMIT]
