"""논문 후보 수집 모듈.

Google Scholar 추천 피드는 공개 API가 없고 로그인 세션을 요구하므로 자동화가 불가능하다.
대신 아래 3개 공개 API에서 주제별 최신 논문을 수집한다.

  - arXiv       : GeoAI / RS 계열 preprint 강세, 전문(full text) 접근 용이
  - OpenAlex    : 저널 게재논문 전반, open access PDF 링크 제공
  - Crossref    : OpenAlex 보완용 (초록이 없는 경우가 많아 3순위)
"""

from __future__ import annotations

import hashlib
import html
import json
import math
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from datetime import date, datetime, timedelta, timezone

USER_AGENT = "daily-paper-bot/1.0 (+https://github.com/dbkim-geo/daily-paper; mailto:dongbum80@gmail.com)"
TIMEOUT = 30


# --------------------------------------------------------------------------
# 저널 품질 기준
# --------------------------------------------------------------------------
# 게재량이 많고 선별도가 낮은 megajournal은 제외한다. OpenAlex의 출판사명과
# 그 상위 계열사명(host_organization_lineage_names)을 모두 훑어 판정하므로,
# 자회사 브랜드로 실려도 걸린다.
EXCLUDED_PUBLISHERS = (
    "multidisciplinary digital publishing institute",   # MDPI
    "frontiers media",                                  # Frontiers
    "public library of science",                        # PLOS
    "hindawi",                                          # Hindawi
)

# 출판사가 아니라 저널 이름으로 걸러야 하는 megajournal.
# Springer Nature의 Discover 시리즈가 대표적인데, 출판사명은 평범한
# "Springer Nature"라서 EXCLUDED_PUBLISHERS로는 잡히지 않는다.
# 여기 있는 저널을 다시 받고 싶으면 해당 항목만 지우면 된다.
EXCLUDED_JOURNAL_RE = re.compile(
    r"^(discover\s|heliyon$|scientific reports$|sage open$|cureus$)",
    re.IGNORECASE,
)

# 리뷰 논문 제외. OpenAlex의 type:article 필터가 review 타입을 이미 거르지만,
# 리뷰인데 article로 분류되는 경우가 있어 제목으로 한 번 더 막는다.
REVIEW_TITLE_RE = re.compile(
    r"\b(a review|the review|review of|reviews of|systematic review|literature review"
    r"|scoping review|narrative review|meta-analysis|meta analysis|bibliometric"
    r"|a survey of|survey of the|state of the art|state-of-the-art review)\b",
    re.IGNORECASE,
)

# 저널 등급 하한 (OpenAlex 2yr_mean_citedness, 임팩트팩터 대응 지표).
# 실측상 이 선을 넘겨도 전문(OA PDF) 확보율은 떨어지지 않는다.
# 등급을 조회하지 못한 저널은 배제하지 않고 가점만 0으로 둔다.
MIN_JOURNAL_IMPACT = 1.0

# 등급 가점 상한. relevance(최대 18)를 넘지 않으면서 recency(최대 12)와
# 견줄 만한 크기로 둔다. log를 쓰는 이유는 IF 0.6과 5의 차이는 크게,
# 15와 30의 차이는 작게 보기 위해서다.
PRESTIGE_MAX = 10.0


# --------------------------------------------------------------------------
# 주제 정의 — 하루에 한 주제씩 순환한다.
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Topic:
    key: str
    label: str            # 사이트에 노출되는 한국어 라벨
    arxiv: str            # arXiv search_query 문법
    scholarly: str        # OpenAlex / Crossref 자연어 검색어
    keywords: tuple[str, ...]   # 관련도 채점용 키워드 (소문자)


TOPICS: tuple[Topic, ...] = (
    Topic(
        key="geoai",
        label="GeoAI",
        arxiv='(abs:"GeoAI" OR abs:"geospatial artificial intelligence" OR '
              '(abs:"deep learning" AND abs:"geospatial"))',
        scholarly="GeoAI geospatial artificial intelligence deep learning",
        keywords=("geoai", "geospatial", "spatial", "deep learning", "machine learning",
                  "neural network", "foundation model", "geographic"),
    ),
    Topic(
        key="geoxai",
        label="GeoXAI",
        arxiv='((abs:"explainable" OR abs:"interpretable" OR abs:"XAI") AND '
              '(abs:"geospatial" OR abs:"spatial" OR abs:"geographic"))',
        scholarly="explainable AI XAI interpretable machine learning geospatial spatial",
        keywords=("explainable", "interpretab", "xai", "shap", "attribution",
                  "geospatial", "spatial", "transparency", "black box"),
    ),
    Topic(
        key="env-planning",
        label="환경계획",
        arxiv='((abs:"environmental planning" OR abs:"land use planning" OR '
              'abs:"green infrastructure" OR abs:"ecosystem service"))',
        scholarly="environmental planning land use planning green infrastructure ecosystem services",
        keywords=("environmental planning", "land use", "green infrastructure",
                  "ecosystem service", "landscape", "zoning", "sustainability",
                  "biodiversity", "watershed"),
    ),
    Topic(
        key="urban-planning",
        label="도시계획",
        arxiv='((abs:"urban planning" OR abs:"urban form" OR abs:"smart city" OR '
              'abs:"built environment"))',
        scholarly="urban planning urban form built environment smart city",
        keywords=("urban", "city", "built environment", "planning", "compact city",
                  "accessibility", "mobility", "housing", "neighborhood", "walkability"),
    ),
    Topic(
        key="carbon-neutral",
        label="탄소중립",
        arxiv='((abs:"carbon neutrality" OR abs:"net zero" OR abs:"net-zero" OR '
              'abs:"decarbonization" OR abs:"decarbonisation"))',
        scholarly="carbon neutrality net zero decarbonization pathway",
        keywords=("carbon neutral", "net zero", "net-zero", "decarboni",
                  "climate neutral", "emission pathway", "ghg", "greenhouse gas",
                  "mitigation", "2050"),
    ),
    Topic(
        key="carbon-reduction",
        label="탄소저감",
        arxiv='((abs:"carbon emission reduction" OR abs:"emission reduction" OR '
              'abs:"carbon sequestration" OR abs:"carbon sink" OR abs:"carbon storage"))',
        scholarly="carbon emission reduction carbon sequestration carbon sink urban carbon",
        keywords=("emission reduction", "carbon sequestration", "carbon sink",
                  "carbon storage", "carbon stock", "co2", "abatement",
                  "carbon footprint", "offset"),
    ),
    Topic(
        key="gis",
        label="GIS",
        arxiv='((abs:"geographic information system" OR abs:"GIS" OR '
              'abs:"spatial analysis" OR abs:"spatial statistics"))',
        scholarly="geographic information system GIS spatial analysis spatial statistics",
        keywords=("gis", "geographic information", "spatial analysis", "spatial statistic",
                  "geostatistic", "cartograph", "spatial autocorrelation", "kriging",
                  "spatial data"),
    ),
    Topic(
        key="remote-sensing",
        label="Remote Sensing",
        arxiv='((abs:"remote sensing" OR abs:"satellite imagery" OR '
              'abs:"earth observation" OR abs:"hyperspectral"))',
        scholarly="remote sensing satellite imagery earth observation land cover",
        keywords=("remote sensing", "satellite", "earth observation", "sentinel",
                  "landsat", "hyperspectral", "sar", "lidar", "land cover",
                  "image classification", "ndvi"),
    ),
)

TOPICS_BY_KEY = {t.key: t for t in TOPICS}


def topic_for_date(day: date) -> Topic:
    """날짜 기준 결정론적 주제 순환. 같은 날 재실행해도 같은 주제가 나온다."""
    return TOPICS[day.toordinal() % len(TOPICS)]


def rotation_from(day: date) -> list[Topic]:
    """당일 주제를 선두로 하는 전체 주제 순회 목록 (폴백 순서)."""
    start = day.toordinal() % len(TOPICS)
    return [TOPICS[(start + i) % len(TOPICS)] for i in range(len(TOPICS))]


# --------------------------------------------------------------------------
# 후보 논문 표현
# --------------------------------------------------------------------------

@dataclass
class Paper:
    source: str                     # arxiv | openalex | crossref
    title: str
    abstract: str
    authors: list[str] = field(default_factory=list)
    venue: str = ""
    published: str = ""             # ISO date (YYYY-MM-DD)
    url: str = ""
    pdf_url: str = ""
    doi: str = ""
    arxiv_id: str = ""
    topic_key: str = ""
    score: float = 0.0
    alt_pdf_urls: list[str] = field(default_factory=list)   # 대체 전문 경로
    publisher: str = ""             # 출판사명 + 상위 계열사명 (megajournal 판정용)
    journal_id: str = ""            # OpenAlex source id (저널 등급 조회용)
    venue_type: str = ""            # journal | repository | conference ...

    def identity_keys(self) -> list[str]:
        """중복 게시 방지를 위한 식별자 집합."""
        keys = []
        if self.doi:
            keys.append("doi:" + normalize_doi(self.doi))
        if self.arxiv_id:
            keys.append("arxiv:" + self.arxiv_id.lower())
        keys.append("title:" + title_hash(self.title))
        return keys

    def to_dict(self) -> dict:
        return asdict(self)


def normalize_doi(doi: str) -> str:
    doi = (doi or "").strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi.rstrip("/")


def title_hash(title: str) -> str:
    norm = re.sub(r"[^a-z0-9]+", "", (title or "").lower())
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:16]


def clean_text(text: str) -> str:
    """XML/HTML 태그와 과도한 공백을 제거한다."""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = text.replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


# --------------------------------------------------------------------------
# HTTP 헬퍼
# --------------------------------------------------------------------------

def _fetch(url: str, *, retries: int = 3, backoff: float = 2.0) -> bytes:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.read()
        except Exception as exc:  # 네트워크/429 등은 재시도한다
            last_error = exc
            if attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}") from last_error


# --------------------------------------------------------------------------
# arXiv
# --------------------------------------------------------------------------

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def fetch_arxiv(topic: Topic, limit: int = 50) -> list[Paper]:
    query = urllib.parse.urlencode({
        "search_query": topic.arxiv,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": limit,
    })
    raw = _fetch(f"https://export.arxiv.org/api/query?{query}")
    root = ET.fromstring(raw)

    papers: list[Paper] = []
    for entry in root.findall(f"{ATOM}entry"):
        entry_id = (entry.findtext(f"{ATOM}id") or "").strip()
        arxiv_id = entry_id.rsplit("/", 1)[-1] if entry_id else ""
        published = (entry.findtext(f"{ATOM}published") or "")[:10]

        pdf_url = ""
        abs_url = entry_id
        for link in entry.findall(f"{ATOM}link"):
            if link.get("title") == "pdf":
                pdf_url = link.get("href", "")
            elif link.get("rel") == "alternate":
                abs_url = link.get("href", abs_url)

        doi = entry.findtext(f"{ARXIV_NS}doi") or ""
        journal_ref = entry.findtext(f"{ARXIV_NS}journal_ref") or ""

        papers.append(Paper(
            source="arxiv",
            title=clean_text(entry.findtext(f"{ATOM}title") or ""),
            abstract=clean_text(entry.findtext(f"{ATOM}summary") or ""),
            authors=[clean_text(a.findtext(f"{ATOM}name") or "")
                     for a in entry.findall(f"{ATOM}author")][:12],
            venue=clean_text(journal_ref) or "arXiv (preprint)",
            published=published,
            url=abs_url,
            pdf_url=pdf_url,
            doi=doi,
            arxiv_id=arxiv_id,
            topic_key=topic.key,
        ))
    return papers


# --------------------------------------------------------------------------
# OpenAlex
# --------------------------------------------------------------------------

def _openalex_abstract(inverted: dict | None) -> str:
    """OpenAlex의 abstract_inverted_index를 평문으로 복원한다."""
    if not inverted:
        return ""
    positions: list[tuple[int, str]] = []
    for word, idxs in inverted.items():
        for idx in idxs:
            positions.append((idx, word))
    positions.sort()
    return clean_text(" ".join(word for _, word in positions))


def fetch_openalex(topic: Topic, since: date, limit: int = 200) -> list[Paper]:
    params = urllib.parse.urlencode({
        "search": topic.scholarly,
        "filter": f"from_publication_date:{since.isoformat()},"
                  f"type:article,has_abstract:true,language:en",
        "sort": "publication_date:desc",
        "per-page": limit,
        "mailto": "dongbum80@gmail.com",
    })
    payload = json.loads(_fetch(f"https://api.openalex.org/works?{params}"))

    papers: list[Paper] = []
    for work in payload.get("results", []):
        abstract = _openalex_abstract(work.get("abstract_inverted_index"))
        if not abstract:
            continue

        if work.get("is_retracted"):
            continue

        best_oa = work.get("best_oa_location") or {}
        primary = work.get("primary_location") or {}
        src = (primary.get("source") or best_oa.get("source") or {})
        venue = src.get("display_name") or ""

        # 출판사 판정은 상위 계열사까지 본다. 예를 들어 Frontiers 계열 저널이
        # 다른 브랜드명으로 실려도 lineage에 "Frontiers Media"가 남는다.
        publisher = " / ".join(dict.fromkeys(
            [src.get("host_organization_name") or ""]
            + list(src.get("host_organization_lineage_names") or [])
        )).strip(" /")

        # 상용 출판사 사이트는 봇을 403으로 막는 경우가 많다(ScienceDirect 등).
        # 같은 논문의 리포지토리 사본(green OA)을 대체 경로로 함께 챙겨 둔다.
        primary_pdf = best_oa.get("pdf_url") or ""
        alt_pdfs = []
        for loc in work.get("locations") or []:
            url = loc.get("pdf_url") or ""
            if not url or url == primary_pdf:
                continue
            is_repo = ((loc.get("source") or {}).get("type") or "") == "repository"
            alt_pdfs.append((0 if is_repo else 1, url))
        alt_pdfs = [u for _, u in sorted(alt_pdfs, key=lambda x: x[0])]

        papers.append(Paper(
            source="openalex",
            title=clean_text(work.get("title") or work.get("display_name") or ""),
            abstract=abstract,
            authors=[clean_text((a.get("author") or {}).get("display_name") or "")
                     for a in work.get("authorships", [])][:12],
            venue=clean_text(venue),
            published=(work.get("publication_date") or "")[:10],
            url=work.get("doi") or (primary.get("landing_page_url") or ""),
            pdf_url=primary_pdf,
            alt_pdf_urls=list(dict.fromkeys(alt_pdfs))[:4],
            doi=work.get("doi") or "",
            topic_key=topic.key,
            publisher=clean_text(publisher),
            journal_id=(src.get("id") or "").rsplit("/", 1)[-1],
            venue_type=src.get("type") or "",
        ))
    return papers


def find_arxiv_pdf(title: str) -> str:
    """같은 논문의 arXiv preprint PDF 주소. 못 찾으면 빈 문자열.

    상위 출판사(Elsevier, Springer Nature, Taylor & Francis)는 PDF 요청을
    403이나 HTML 안내 페이지로 막는다. 저널 등급을 낮추지 않고 전문을 얻으려면
    저자가 올린 arXiv 사본을 찾는 것이 가장 확실하다.
    """
    words = re.findall(r"[A-Za-z0-9]+", title)
    if len(words) < 4:
        return ""

    query = urllib.parse.urlencode({
        "search_query": 'ti:"' + " ".join(words[:16]) + '"',
        "max_results": 3,
    })
    try:
        root = ET.fromstring(_fetch(f"https://export.arxiv.org/api/query?{query}", retries=2))
    except Exception:
        return ""

    def norm(s: str) -> str:
        return re.sub(r"[^a-z0-9]+", "", s.lower())

    want = norm(title)
    for entry in root.findall(f"{ATOM}entry"):
        found = norm(entry.findtext(f"{ATOM}title") or "")
        # 제목이 사실상 같을 때만 인정한다. 부제·대소문자·구두점 차이는 무시된다.
        if not found or (found not in want and want not in found):
            continue
        for link in entry.findall(f"{ATOM}link"):
            if link.get("title") == "pdf" and link.get("href"):
                return link.get("href", "")
    return ""


def fetch_journal_impact(journal_ids: list[str]) -> dict[str, float]:
    """OpenAlex source id -> 2yr_mean_citedness (임팩트팩터 대응 지표).

    한 번에 50개씩 묶어 조회한다. 실패하면 빈 dict를 돌려주고, 호출부는
    등급을 모르는 저널로 취급해 배제하지 않는다. 등급 조회가 안 된다고
    그날 게시를 통째로 건너뛰는 것이 더 나쁘기 때문이다.
    """
    ids = [i for i in dict.fromkeys(journal_ids) if i]
    impact: dict[str, float] = {}

    for start in range(0, len(ids), 50):
        chunk = ids[start:start + 50]
        params = urllib.parse.urlencode({
            "filter": "ids.openalex:" + "|".join(chunk),
            "per-page": 200,
            "mailto": "dongbum80@gmail.com",
        })
        try:
            payload = json.loads(_fetch(f"https://api.openalex.org/sources?{params}"))
        except Exception as exc:
            print(f"    저널 등급 조회 실패 ({exc}) — 등급 가점 없이 진행한다")
            continue
        for src in payload.get("results", []):
            key = (src.get("id") or "").rsplit("/", 1)[-1]
            stats = src.get("summary_stats") or {}
            impact[key] = float(stats.get("2yr_mean_citedness") or 0.0)

    return impact


# --------------------------------------------------------------------------
# Crossref (보조)
# --------------------------------------------------------------------------

def fetch_crossref(topic: Topic, since: date, limit: int = 40) -> list[Paper]:
    params = urllib.parse.urlencode({
        "query.bibliographic": topic.scholarly,
        "filter": f"from-pub-date:{since.isoformat()},type:journal-article,has-abstract:true",
        "sort": "published",
        "order": "desc",
        "rows": limit,
        "mailto": "dongbum80@gmail.com",
    })
    payload = json.loads(_fetch(f"https://api.crossref.org/works?{params}"))

    papers: list[Paper] = []
    for item in payload.get("message", {}).get("items", []):
        abstract = clean_text(item.get("abstract") or "")
        if not abstract:
            continue

        parts = (item.get("published") or {}).get("date-parts") or [[]]
        ymd = (parts[0] + [1, 1])[:3] if parts and parts[0] else []
        published = f"{ymd[0]:04d}-{ymd[1]:02d}-{ymd[2]:02d}" if len(ymd) == 3 else ""

        papers.append(Paper(
            source="crossref",
            title=clean_text((item.get("title") or [""])[0]),
            abstract=abstract,
            authors=[clean_text(f"{a.get('given', '')} {a.get('family', '')}")
                     for a in item.get("author", [])][:12],
            venue=clean_text((item.get("container-title") or [""])[0]),
            published=published,
            url=item.get("URL", ""),
            doi=item.get("DOI", ""),
            topic_key=topic.key,
            publisher=clean_text(item.get("publisher") or ""),
            venue_type="journal",
        ))
    return papers


# --------------------------------------------------------------------------
# 채점 및 수집
# --------------------------------------------------------------------------

def keyword_hits(paper: Paper, topic: Topic) -> tuple[int, int]:
    """(제목 매칭 수, 초록 매칭 수)."""
    title_l = paper.title.lower()
    abstract_l = paper.abstract.lower()
    title_hits = sum(1 for kw in topic.keywords if kw in title_l)
    abstract_hits = sum(1 for kw in topic.keywords if kw in abstract_l)
    return title_hits, abstract_hits


def rejection_reason(paper: Paper, impact: dict[str, float]) -> str:
    """저널 품질 기준에 걸리면 그 이유를, 통과하면 빈 문자열을 돌려준다.

    arXiv preprint는 저널 게재논문이 아니므로 이 기준을 적용하지 않는다.
    대신 등급 가점을 받지 못해 자연히 뒤로 밀린다.
    """
    if paper.source == "arxiv":
        return ""

    haystack = paper.publisher.lower()
    for name in EXCLUDED_PUBLISHERS:
        if name in haystack:
            return f"제외 출판사({paper.publisher})"

    if paper.venue and EXCLUDED_JOURNAL_RE.search(paper.venue.strip()):
        return f"제외 저널({paper.venue})"

    # 대학 리포지토리·프로시딩이 저널 논문 자리에 섞여 들어오는 것을 막는다.
    if paper.venue_type and paper.venue_type != "journal":
        return f"비저널 매체({paper.venue_type})"

    if REVIEW_TITLE_RE.search(paper.title):
        return "리뷰 논문"

    if paper.journal_id and paper.journal_id in impact:
        if impact[paper.journal_id] < MIN_JOURNAL_IMPACT:
            return f"저널 등급 미달(2yrIF {impact[paper.journal_id]:.2f})"

    return ""


def is_on_topic(paper: Paper, topic: Topic) -> bool:
    """주제 관련도 최소 기준. 다른 가점만으로 무관한 논문이 뽑히는 것을 막는다."""
    title_hits, abstract_hits = keyword_hits(paper, topic)
    return title_hits >= 1 or abstract_hits >= 2


def score_paper(paper: Paper, topic: Topic, today: date,
                impact: dict[str, float] | None = None) -> float:
    """주제 관련도 + 최신성 + 요약 가능성을 합산한 점수."""
    title_hits, abstract_hits = keyword_hits(paper, topic)
    relevance = min(3.0 * title_hits + 1.0 * abstract_hits, 18.0)

    # 최신성. Crossref는 online-first 논문에 미래 issue 날짜를 싣는 경우가 있어
    # 음수 age가 나오면 가점 없이 0으로 처리한다.
    recency = 0.0
    if paper.published:
        try:
            age = (today - date.fromisoformat(paper.published)).days
            if age >= 0:
                recency = 12.0 * (1.0 - min(age, 365) / 365.0)
        except ValueError:
            pass

    # 요약 품질에 직결되는 신호
    depth = 0.0
    n = len(paper.abstract)
    if n >= 700:
        depth += 4.0
    elif n >= 400:
        depth += 2.5
    elif n < 250:
        depth -= 4.0

    if paper.pdf_url:
        depth += 3.0          # 전문 기반 요약이 가능하면 품질이 올라간다
    if paper.doi:
        depth += 1.0
    if len(paper.authors) >= 2:
        depth += 0.5

    # 소스 신뢰도: 정식 게재논문(OpenAlex) > preprint(arXiv) > 메타데이터만(Crossref)
    source_bonus = {"openalex": 2.0, "arxiv": 1.0, "crossref": 0.0}.get(paper.source, 0.0)

    # 저널 등급. 등급을 모르는 저널과 preprint는 0점이라 자연히 뒤로 밀린다.
    prestige = 0.0
    if impact and paper.journal_id:
        value = impact.get(paper.journal_id, 0.0)
        if value > 0:
            prestige = min(3.0 * math.log1p(value), PRESTIGE_MAX)

    return relevance + recency + depth + source_bonus + prestige


def collect_candidates(topic: Topic, today: date, window_days: int = 240) -> list[Paper]:
    """한 주제에 대해 3개 소스에서 후보를 모아 채점·정렬한다."""
    since = today - timedelta(days=window_days)
    papers: list[Paper] = []

    for name, fn in (
        ("arxiv", lambda: fetch_arxiv(topic)),
        ("openalex", lambda: fetch_openalex(topic, since)),
        ("crossref", lambda: fetch_crossref(topic, since)),
    ):
        try:
            got = fn()
            papers.extend(got)
            print(f"    [{topic.key}] {name}: {len(got)}건")
        except Exception as exc:
            print(f"    [{topic.key}] {name}: 실패 ({exc})")

    # 저널 등급을 한 번에 조회한다. 주제당 요청 1~2회면 충분하다.
    impact = fetch_journal_impact([p.journal_id for p in papers if p.journal_id])

    # 소스 간 중복 제거 (같은 논문이 arXiv/OpenAlex 양쪽에 있을 수 있다)
    seen: set[str] = set()
    unique: list[Paper] = []
    rejected: dict[str, int] = {}
    for paper in papers:
        if not paper.title or not paper.abstract:
            continue
        if not is_on_topic(paper, topic):
            continue

        reason = rejection_reason(paper, impact)
        if reason:
            key = reason.split("(")[0]
            rejected[key] = rejected.get(key, 0) + 1
            continue

        keys = set(paper.identity_keys())
        if keys & seen:
            continue
        seen |= keys
        paper.score = score_paper(paper, topic, today, impact)
        unique.append(paper)

    if rejected:
        detail = ", ".join(f"{k} {v}건" for k, v in sorted(rejected.items()))
        print(f"    [{topic.key}] 품질 기준 제외: {detail}")

    unique.sort(key=lambda p: p.score, reverse=True)
    return unique
