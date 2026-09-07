---
layout: post
title: "Biodiversity and chemical regulation: Status quo, data gaps, and recommendations for future action"
date: 2026-09-08 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "EU 화학물질 규제와 biodiversity 연구의 연결 고리를 점검한 리뷰다."
authors: "Anja Gladbach, Christoph J Mayer, Aaron Stoler, Sian Ellis, Marta Baccaro, David A. Bohan, Franziska Enzmann, Emily Garman, Jutta Hellstern, Sarah Hughes, Philippe Lemaire, Jan‐Dieter Ludwigs"
venue: "Integrated Environmental Assessment and Management"
published: "2026-08-26"
doi: "https://doi.org/10.1093/inteam/vjag145"
paper_url: "https://doi.org/10.1093/inteam/vjag145"
pdf_url: "https://academic.oup.com/ieam/advance-article-pdf/doi/10.1093/inteam/vjag145/70798308/vjag145.pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "biodiversity"
  - "chemical regulation"
  - "REACH"
  - "Essential Biodiversity Variables"
  - "environmental risk assessment"
  - "FAIR data"
paper_keywords:
  - "Biodiversity"
  - "Chemicals"
  - "Regulation"
  - "Chemicals Management"
figure: "/assets/figures/2026-09-08-biodiversity-and-chemical-regulation-status-quo-data-gaps.png"
---

## 한 줄 요약

**EU 화학물질 규제와 biodiversity 연구의 연결 고리를 점검한 리뷰다.**

![원문 대표 그림]({{ '/assets/figures/2026-09-08-biodiversity-and-chemical-regulation-status-quo-data-gaps.png' | relative_url }})

*원문에서 발췌 — Anja Gladbach 외, Integrated Environmental Assessment and Management, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

화학물질 노출은 biodiversity 감소의 주요 동인으로 지목되지만 정량적 연결 고리는 아직 불명확하다. ECETOC가 구성한 다학제 Task Force가 EU 법령과 전략 문서, EU 지원 연구과제, 동료심사 문헌을 함께 검토했다. 검토 결과 화학물질 규제는 biodiversity를 대부분 정성적으로만 언급하고, biodiversity 연구는 화학물질 영향을 거의 다루지 않으며, 연구 성과와 규제 체계의 연결도 약한 것으로 나타났다. 저자들은 규제 맥락에서 쓸 수 있는 operational definition 마련, 지표 표준화, 중앙화된 데이터 플랫폼 구축, machine learning 등 신기술 활용을 권고한다.

## 주요 차별성

- EU 법령·전략 문서, EU 지원 연구과제, 학술 문헌이라는 세 축을 하나의 리뷰에서 동시에 점검한다.
- text mining과 singular value decomposition(SVD)을 써서 biome별 biodiversity 정의·지표 서술을 정량 비교한다.
- 학술 문헌 코퍼스를 GEOBON의 Essential Biodiversity Variables(EBVs)와 EuropaBON 대상 생물군에 매핑해 규제와의 정렬 수준을 진단한다.
- 산업계·학계·규제기관이 함께 참여한 Task Force가 규제 실무 관점에서 gap을 정리한다.

## 주요 기여점

- EU 법령·전략 문서 41건 중 25건을 정밀 평가해 biodiversity 정의 제시 5건, 지표 언급 8건, 평가 방법론 언급 3건이라는 수치를 제시한다.
- CORDIS 기반으로 2017년 이후 biodiversity 관련 과제 1251건을 분류해 직접 관련 34건(약 3%), 간접 관련 234건(약 19%)이라는 구조를 밝힌다.
- biome별 문헌 205편의 코퍼스를 SVD와 k-means로 군집화해 5개 biome 군집을 도출한다.
- operational definition 정립, 지표 표준화, FAIR 원칙 기반 중앙 데이터 플랫폼 구축을 포함한 7개 권고안을 제시한다.

## 연구의 배경

전 지구적으로 biodiversity가 감소하고 있으며 IPBES와 UNEP는 토지이용 변화, 남획, 기후변화, 오염, 침입외래종을 5대 직접 동인으로 든다. EU는 Biodiversity Strategy, Farm to Fork Strategy, Zero Pollution Action Plan, Chemical Strategy for Sustainability를 통해 오염 저감과 생태계 회복을 추진하고 있다. REACH와 Plant Protection Products Regulation 같은 화학물질 규제도 생태계 보호를 목표로 한다.

## 필요성

생태계는 복잡하고 여러 stressor가 동시에 작용하기 때문에 화학물질 규제가 biodiversity 목표 달성에 기여하는 정도를 직접 측정하기 어렵다. 화학물질 노출과 biodiversity 손실 사이의 정량적 연결, 그리고 서식지 손실 같은 다른 압력과 비교한 상대적 기여도는 아직 규명되지 않았다. 규제와 연구가 쓰는 정의와 지표가 서로 달라 조율된 관리도 어렵다.

## 목적

EU 화학물질 규제 안에서 biodiversity가 어떻게 정의·측정되는지, 관련 연구가 규제에 어떻게 연결되는지를 평가하는 것이 목적이다. 이를 통해 지식 격차와 불일치를 드러내고 향후 행동 방향을 제시한다.

## 방법론

리뷰는 세 가지 목표로 나뉜다. 첫째, Task Force의 전문가 판단과 EUR-Lex 검색으로 EU 법령·전략 문서 41건(규정 15건, 지침 12건, 정책 전략 6건, framework 6건, 국가법 1건, 기타 1건)을 선정하고, biodiversity 명시 여부와 화학물질 영향 초점 여부로 선별해 25건을 정밀 평가했다. 둘째, CORDIS 데이터베이스에서 2023년 12월 21일 자료를 추출해 2017년 이후 시작된 biodiversity 관련 과제 1251건을 직접 관련, 간접 관련, 비관련으로 분류했다. 셋째, 2024년 4월 18일 Google Scholar에서 biome별로 2014~2024년 review, perspective, meta-analysis를 검색해 상위 100건에서 biome당 25편씩 총 205편을 선정했다. 선정 문헌의 전문을 biome별 텍스트 파일로 모아 R의 tm과 SnowballC로 stopword 제거와 stemming을 수행하고, JMP의 text mining 도구로 SVD를 적용한 뒤 GEOBON의 Essential Biodiversity Variables와 EuropaBON 대상 생물군 키워드를 document-term matrix에서 집계했다.

## 결과

평가 대상 41건 중 28건이 biodiversity를 언급했고, 1990년대 이후 언급 빈도가 뚜렷이 증가했다. 정밀 평가한 25건에서 biodiversity 정의를 제시한 문서는 5건뿐이며 대부분 CBD 1992 정의를 따랐고, 지표를 보고한 문서는 8건, 화학물질 영향 평가 방법론을 다룬 문서는 3건에 그쳤다. CORDIS 과제 1251건 중 직접 관련은 34건(약 3%), 간접 관련은 234건(약 19%), 비관련은 983건(약 78%)이었으며, 직접 관련 과제 중 화학물질 규제에 바로 쓸 방법론이나 산출물을 목표로 한 과제는 없었다. 문헌 분석에서 SVD의 첫 세 특이벡터가 각각 19.1%, 14.2%, 11.6%(누적 44.9%)의 변동을 설명했고, k-means 군집은 5개에서 87.5%, 6개에서 94.1%의 between sum of squares를 설명했다. 5개 군집은 grassland·forest, soil, urban·tundra·desert, freshwater·coral, coastal·marine으로 나뉘었으며, EBV 계열 중에서는 species traits가 가장 많이, community composition과 ecosystem structure가 가장 적게 나타났다.

## 논의

정의와 지표의 불일치는 biome 간 먹이망 구조, 종 밀도, 물리적 특성, 교란 정도의 차이에서 비롯되므로 획일적인 biodiversity 평가 체계는 실효성이 낮다고 저자들은 본다. EU 지원 연구비는 2019년 이후 크게 늘었지만, 중앙화된 FAIR 데이터 소스가 없어 과제 간 meta-analysis와 규제 활용이 제약된다. 문헌 분석이 review·perspective·meta-analysis에 한정되어 최신 실증 연구와 오래된 문헌이 빠졌고, 연구 출판과 입법 반영 사이의 시차도 한계로 지적된다. 저자들은 규제 맥락의 operational definition 정립, 지표 표준화, FAIR 기반 데이터 플랫폼 구축, mechanistic effect modelling과 AI 활용, fungi·invertebrates·plankton 등 관측이 어려운 생물군의 공백 보완, IPBES 5대 동인을 함께 담는 다요인 연구 설계를 후속 과제로 제시한다.

## 왜 읽을 만한가

환경계획과 규제 연구에서 정책 목표와 측정 지표가 어긋나는 구조를 문서·과제·문헌 수준의 수치로 보여준다. biodiversity 지표 표준화와 데이터 플랫폼 논의를 국내 환경정책 맥락에 옮겨 볼 때 참고 틀이 된다.

## 원문 키워드

`Biodiversity`, `Chemicals`, `Regulation`, `Chemicals Management`

## 원문 링크

- 원문: [https://doi.org/10.1093/inteam/vjag145](https://doi.org/10.1093/inteam/vjag145)
- PDF: [https://academic.oup.com/ieam/advance-article-pdf/doi/10.1093/inteam/vjag145/70798308/vjag145.pdf](https://academic.oup.com/ieam/advance-article-pdf/doi/10.1093/inteam/vjag145/70798308/vjag145.pdf)
- DOI: [https://doi.org/10.1093/inteam/vjag145](https://doi.org/10.1093/inteam/vjag145)
