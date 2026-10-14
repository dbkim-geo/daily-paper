---
layout: post
title: "Leveraging open source land use and land cover data for urban and regional planning in transforming areas"
date: 2026-10-15 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "공개 LULC open data로 탈석탄 전환 지역의 토지이용 계획 근거를 만든 사례 연구다."
authors: "Florian Klopfer, Dietwald Gruehn"
venue: "Regional Studies Regional Science"
published: "2024-11-26"
doi: "https://doi.org/10.1080/21681376.2024.2422348"
paper_url: "https://doi.org/10.1080/21681376.2024.2422348"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "land use and land cover (LULC)"
  - "ecosystem services"
  - "open data"
  - "land suitability analysis"
  - "spatial planning"
  - "coal phase-out"
paper_keywords:
  - "Ecosystem services (ES)"
  - "future land use"
  - "geographical analysis"
  - "land use and land cover (LULC)"
  - "open data"
  - "Rhineland mining area"
  - "spatial planning"
  - "structural shifts JEL R14"
  - "R52"
  - "R58"
  - "Q15"
  - "Q24"
figure: "/assets/figures/2026-10-15-leveraging-open-source-land-use-and-land-cover-data-for.png"
---

## 한 줄 요약

**공개 LULC open data로 탈석탄 전환 지역의 토지이용 계획 근거를 만든 사례 연구다.**

![원문 대표 그림]({{ '/assets/figures/2026-10-15-leveraging-open-source-land-use-and-land-cover-data-for.png' | relative_url }})

*원문에서 발췌 — Florian Klopfer 외, Regional Studies Regional Science, 2024. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

독일 Rhineland mining area를 대상으로 공개 land use and land cover (LULC) 데이터의 공간계획 활용 가능성을 실증했다. 세 가지 분석을 수행했다. 첫째는 ecosystem services (ES) 종합 평가, 둘째는 정주지 개발 제약 기반 go to/no-go 평가, 셋째는 농업·정주지·자연/휴양 세 용도의 community 단위 적합성 평가다. 결과는 상세 표현과 단순화 표현으로 함께 제시해 계획 전문가부터 일반 시민까지 서로 다른 청중에 맞추도록 했다.

## 주요 차별성

- 모든 분석 결과를 상세판과 단순화판(평균 기준 2분류, go to/no-go 2분류 등)으로 동시에 제시해 청중별 커뮤니케이션 수준을 조절했다.
- ES 평가, 정주지 개발 제약 평가, 미래 토지이용 적합성 평가를 하나의 open data 기반 워크플로로 연결했다.
- 탈석탄으로 구조 전환 중인 광산 지역에 공개 LULC 데이터를 적용한 실무 지향 사례다.
- 25 m raster와 community 단위 집계라는 두 공간 해상도로 같은 적합성 분석을 비교 제시했다.

## 주요 기여점

- OpenStreetMap, INSPIRE, NRW open government 등 공개 데이터만으로 지역·도시계획 의사결정 근거를 구축할 수 있음을 보였다.
- 7개 ES 중첩, 4개 제약 요인 중첩, 12개 요인 적합성 평가라는 재현 가능한 분석 절차를 제시했다.
- 광산 주변 community 다수가 단일 우세 용도를 갖지 않아 탈광산 경관 계획에 선택의 여지가 있음을 확인했다.
- ES 개념을 계획 참여 과정의 정보 전달 수단으로 쓰는 통합 framework를 제안했다.

## 연구의 배경

기후변화, 인구 고령화, 산업 구조 전환이 도시·지역계획에 동시에 압력을 가하고 있다. 한편 OpenStreetMap, EU INSPIRE directive, NRW open government 체계 등으로 공개 LULC 데이터가 빠르게 늘고 있다. 독일 Rhineland mining area는 탈석탄 시점이 2038년에서 2030년으로 8년 앞당겨져 탈광산 이후 계획이 시급해졌다.

## 필요성

공개 LULC 데이터의 상당 부분은 여전히 계획 실무에서 활용되지 않는다. ES 연구는 방법론·개념 연구에 치우쳐 있고 계획 과정에 통합된 사례는 제한적이다. 해당 지역에는 여러 전략이 있지만 가용 데이터를 활용한 공간 명시적 분석이 부족하다.

## 목적

공개 LULC 데이터가 전환 지역의 공간계획을 어떻게 지원할 수 있는지 세 가지 예시 분석으로 보여주는 것이 목적이다. 동시에 청중별로 정보의 상세 수준을 조절하는 제시 방식을 제안한다.

## 방법론

연구 지역은 독일 North Rhine-Westphalia의 Düren, Euskirchen, Heinsberg 등 6개 county/district와 Mönchengladbach 시다. Basis DLM, Geobasis NRW, LANUV, BfN, EEA 데이터를 ArcGIS Pro에서 25 m raster로 통일해 중첩했다. ES 평가는 thermic compensation, biomass production potential, surface runoff regulation, groundwater recharge, groundwater protection, recreation, habitat의 7개 ES를 각각 등간격 3등급(1~3)으로 나눈 뒤 동일 가중치로 합산해 7~21점으로 산출했다. 정주지 평가는 산림, 엄정 보호지역, biotope network, 토양가치 55 초과 등을 제약 요인으로 두고 제약 수와 go to/no-go를 지도화했다. 적합성 평가는 12개 요인이 상위 사분위에 속할 때 저자가 정한 ++/+/0/– 가중을 더하고, community 단위 사분위로 우세 용도를 분류했다.

## 결과

연구 지역은 open space가 약 78.7%, 농업 52.2%, 경작지 37.7%, 산림 24.4%, 수역 약 1.4%를 차지한다. ES 종합값은 남부·남서부가 최대 약 20(최대 21)으로 높고 북부·북동부는 정주지와 집약 농업으로 낮았다. 제약이 3~4개 겹치는 지역은 Inden과 Hambach 노천광 인근에 두드러졌다. community 단위 종합에서 남서부는 자연/휴양 용도가 뚜렷했고, 동부 중앙은 정주지 적합성이 높지만 농업과 경합했다. 2개 community는 우세 적합 용도가 없었고, 광산 인근 다수 community도 단일 우세 용도가 나타나지 않았다.

## 논의

상세 지도는 계획 실무에, 단순화 지도는 시민 참여 초기 단계에 적합해 계획 단계에 따라 순차적으로 쓸 수 있다. 적합성 평가의 요인 가중은 저자 판단에 따른 주관적 설정이며 4단계 평가 체계와 집계 수준 선택이 결과에 영향을 준다. 독일은 데이터가 16개 주와 county, 지자체에 분산돼 광역 분석에 제약이 있다. 후속 연구로 전문가 인터뷰 기반 가중치 설정, 실제 계획 과정 적용, 오스트리아·스위스 등 다른 국가와의 비교를 제안한다.

## 왜 읽을 만한가

공개 데이터와 단순 raster 중첩만으로 계획 의사결정 근거를 만드는 절차가 구체적으로 제시돼 국내 탄광 지역이나 전환 지역 계획에 바로 참고할 만하다. 청중별 지도 상세도 조절 방식은 주민 참여 설계에도 응용할 수 있다.

## 원문 키워드

`Ecosystem services (ES)`, `future land use`, `geographical analysis`, `land use and land cover (LULC)`, `open data`, `Rhineland mining area`, `spatial planning`, `structural shifts JEL R14`, `R52`, `R58`, `Q15`, `Q24`

## 원문 링크

- 원문: [https://doi.org/10.1080/21681376.2024.2422348](https://doi.org/10.1080/21681376.2024.2422348)
- DOI: [https://doi.org/10.1080/21681376.2024.2422348](https://doi.org/10.1080/21681376.2024.2422348)
