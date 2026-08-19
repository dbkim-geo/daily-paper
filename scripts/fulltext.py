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


# 저자 키워드 블록의 시작과 끝. 끝은 다음 섹션 제목이 나오는 지점이다.
_KEYWORD_HEAD = re.compile(
    r"(?ims)^[ \t]*(?:key\s?words?|index\s+terms)[ \t]*[:\-—.]?[ \t]*\n?(.{0,400})"
)
_KEYWORD_TAIL = re.compile(
    r"(?is)\b(abstract|introduction|1\s*\.\s*introduction|article\s+info|"
    r"received|©|copyright|highlights)\b"
)


def extract_author_keywords(text: str) -> list[str]:
    """전문에서 저자가 직접 적은 키워드를 뽑는다. 없으면 빈 리스트.

    OpenAlex도 keywords를 주지만 자동 생성이라 "Vegetation (pathology)" 같은
    오류가 섞인다. 원문에 적힌 것만 쓰고, 없으면 지어내지 않는다.
    """
    if not text:
        return []

    match = _KEYWORD_HEAD.search(text)
    if not match:
        return []

    block = match.group(1)
    tail = _KEYWORD_TAIL.search(block)
    if tail:
        block = block[:tail.start()]

    parts = re.split(r"[,;\n·•]+", block)
    keywords: list[str] = []
    for part in parts:
        word = re.sub(r"\s+", " ", part).strip(" .:-—\t")
        # 한 낱말도 안 되거나 문장으로 흘러간 조각은 키워드가 아니다.
        if not (2 <= len(word) <= 60) or len(word.split()) > 6:
            continue
        if word.lower() in {w.lower() for w in keywords}:
            continue
        keywords.append(word)
        if len(keywords) >= 12:
            break

    # 한두 개만 잡혔다면 오탐일 가능성이 높다.
    return keywords if len(keywords) >= 3 else []


def download_pdf(pdf_url: str) -> bytes:
    """PDF 바이트를 받아온다. PDF가 아니면 빈 바이트를 돌려준다."""
    try:
        req = urllib.request.Request(
            pdf_url,
            headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read(PDF_BYTE_LIMIT)
    except Exception as exc:
        print(f"    전문 다운로드 실패: {exc}")
        return b""

    # Content-Type이나 URL 확장자는 믿을 수 없다. Springer Nature 등은 .pdf
    # 주소에 HTTP 200과 text/html 안내 페이지를 돌려준다. 실제 바이트로 판정한다.
    if not data.startswith(b"%PDF"):
        head = data[:200].decode("utf-8", "replace").strip().replace("\n", " ")
        print(f"    PDF가 아닌 응답({len(data):,}바이트): {head[:60]}")
        return b""

    return data


def extract_pdf_text(pdf_url: str, data: bytes | None = None) -> str:
    """PDF 본문 텍스트. 실패하면 빈 문자열을 돌려준다.

    이미 받아둔 바이트가 있으면 `data`로 넘겨 재다운로드를 피한다.
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        print("    pypdf 미설치 — 전문 추출을 건너뛴다")
        return ""

    if data is None:
        data = download_pdf(pdf_url)
    if not data:
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


# --------------------------------------------------------------------------
# 대표 그림 추출
# --------------------------------------------------------------------------

# 재배포가 허용되는 라이선스만 허용한다. 그림을 축소해 싣는 것은 2차적 저작물
# 작성에 해당하므로 ND(변경 금지) 계열은 제외한다. 라이선스를 모르면 넣지 않는다.
FIGURE_OK_LICENSES = ("cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa", "cc0", "public-domain")

FIGURE_MIN_PIXELS = 150_000     # 로고(91x91=8천)와 진짜 그림(26만~145만)을 가른다
FIGURE_MAX_WIDTH = 1200         # 저장 시 가로 상한
FIGURE_SKIP_PAGES = 1           # 표지에는 학술지 로고·QR만 있다


def figure_license_ok(license_name: str) -> bool:
    return (license_name or "").strip().lower() in FIGURE_OK_LICENSES


def extract_representative_figure(data: bytes) -> tuple[bytes, str] | None:
    """PDF에서 대표 그림 하나를 골라 (이미지 바이트, 확장자)로 돌려준다.

    본문에서 가장 먼저 나오는 큰 그림을 고른다. 보통 Figure 1(연구 지역도나
    방법론 흐름도)이라 대표성이 있다. 실패하면 None.
    """
    try:
        from pypdf import PdfReader
        from PIL import Image
    except ImportError:
        print("    Pillow/pypdf 미설치 — 그림 추출을 건너뛴다")
        return None

    try:
        reader = PdfReader(io.BytesIO(data))
    except Exception as exc:
        print(f"    그림 추출용 PDF 파싱 실패: {exc}")
        return None

    # 여러 쪽에 반복되는 이미지는 러닝 헤더/로고다. 먼저 세어 두고 제외한다.
    pages_by_name: dict[str, int] = {}
    for page in reader.pages[:40]:
        try:
            for img in page.images:
                pages_by_name[img.name] = pages_by_name.get(img.name, 0) + 1
        except Exception:
            continue

    for index, page in enumerate(reader.pages[:40], start=1):
        if index <= FIGURE_SKIP_PAGES:
            continue
        try:
            images = list(page.images)
        except Exception:
            continue

        for img in images:
            if pages_by_name.get(img.name, 0) >= 3:
                continue
            try:
                pil = Image.open(io.BytesIO(img.data))
                width, height = pil.size
            except Exception:
                continue

            if width * height < FIGURE_MIN_PIXELS:
                continue
            ratio = width / height if height else 0
            if not (0.3 <= ratio <= 5.0):     # 얇은 띠(장식선·배너)를 거른다
                continue

            try:
                if width > FIGURE_MAX_WIDTH:
                    scale = FIGURE_MAX_WIDTH / width
                    pil = pil.resize((FIGURE_MAX_WIDTH, max(1, round(height * scale))),
                                     Image.LANCZOS)
                if pil.mode not in ("RGB", "RGBA", "L"):
                    pil = pil.convert("RGB")
                buffer = io.BytesIO()
                pil.save(buffer, format="PNG", optimize=True)
            except Exception as exc:
                print(f"    그림 변환 실패: {exc}")
                continue

            print(f"    대표 그림: p{index} {width}x{height} "
                  f"-> {len(buffer.getvalue()) / 1024:,.0f}KB")
            return buffer.getvalue(), "png"

    return None
