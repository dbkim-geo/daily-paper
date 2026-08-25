---
layout: post
title: "Integrating risk and feasibility in the spatial planning of nature-based solutions: a cross-city analysis of Barcelona, Boston, and Rotterdam"
date: 2026-08-26 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "기후 위험과 NbS 실행 가능성을 겹쳐 도시별 우선 적용 구역을 찾는다"
authors: "Svetlana Khromova, Svea Busse, Giulia Benati, Pablo Herreros-Cantis, Charlie Mioulet, Matthew J. Eckelman, Gara Villalba, Johannes Langemeyer"
venue: "npj Urban Sustainability"
published: "2026-08-20"
doi: "https://doi.org/10.1038/s42949-026-00461-7"
paper_url: "https://doi.org/10.1038/s42949-026-00461-7"
pdf_url: "https://www.nature.com/articles/s42949-026-00461-7_reference.pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "Nature-based Solutions (NbS)"
  - "SETS framework"
  - "multi-hazard climate risk"
  - "feasibility mapping"
  - "Moran's I"
  - "spatial decision support"
paper_keywords:
  - "Urban Stormwater"
  - "Urban Heat"
  - "Nature-based Solutions (NbS)"
  - "Social-Ecological- Technological Systems (SETS)"
  - "Resilience"
  - "Ecosystem Services"
---

## 한 줄 요약

**기후 위험과 NbS 실행 가능성을 겹쳐 도시별 우선 적용 구역을 찾는다**

## 초록 요약

도시의 기후 적응 수단으로 nature-based solutions(NbS)가 확산되고 있으나 위험과 실행 가능성을 함께 평가하는 통합적 계획 도구는 부족하다. 이 연구는 SETS(social-ecological-technological systems) 기반의 이전 가능한 decision-support framework를 만들어 Barcelona, Boston, Rotterdam 세 도시에 적용한다. green roofs, permeable pavements, rain gardens, urban parks 네 가지 NbS를 대상으로 다중 위험(도시 홍수·폭염) 위험도와 실행 가능성을 공간적으로 분석한다. 위험도와 실행 가능성을 중첩해 즉시 적용 가능한 high risk–high feasibility 구역과, 적응 수요는 크지만 여건이 제약된 high-risk/low-feasibility 지역을 함께 식별한다.

## 주요 차별성

- 위험도(needs)와 실행 가능성(feasibility)을 별도 지표로 각각 매핑한 뒤 중첩해 우선순위 구역을 도출한다.
- SETS 관점을 사회·생태·기술 세 축의 vulnerability와 feasibility 지표로 분해해 공간 자료로 구현한다.
- 기후대·도시 형태·거버넌스가 다른 Barcelona, Boston, Rotterdam을 동일한 100×100 m 격자 규격으로 비교한다.
- flood와 heat 두 hazard를 하나의 분석틀에서 다루고 NbS 유형별로 실행 가능성을 구분한다.

## 주요 기여점

- NbS 계획의 사회·생태·기술 차원을 연결하는 통합 risk–feasibility framework를 제시한다.
- 다중 hazard를 대상으로 한 cross-city 비교 분석을 수행해 일반화 가능한 패턴과 도시별 고유 패턴을 함께 보여 준다.
- NbS가 가장 필요한 곳과 가장 실행하기 쉬운 곳을 동시에 찾는 재현 가능한 decision-support 절차를 제공한다.
- OAT sensitivity analysis와 aggregation operator 비교로 합성 지수의 견고성을 검증한다.

## 연구의 배경

도시는 급속한 도시화와 기후변화로 홍수·폭염 위험이 커지고 있으며, 기반시설이 서로 얽혀 있어 한 영역의 충격이 다른 영역으로 연쇄된다. 이에 대응해 NbS 투자가 늘고 있으나 기존 연구는 stormwater management에 편중되어 heat mitigation과의 통합이 부족하다. SETS framework는 도시를 사회·생태·기술이 결합된 체계로 보아 이러한 분절을 메우는 관점을 제공한다.

## 필요성

NbS의 위험 저감 효과는 국지적이어서 어디에 설치하느냐가 누가 혜택을 받는지를 결정한다. 그럼에도 사회적·생태적 편익을 도시 전체 NbS 계획에 함께 반영한 사례는 드물고, NbS가 도시 기술·기반시설과 어떻게 상호작용하는지도 충분히 다뤄지지 않았다. 이 공백은 단편적 시공, 편차가 큰 효과, 취약한 장기 유지·관리 체계로 이어진다.

## 목적

SETS 관점에서 NbS가 필요한 공간(risk)과 실행 가능한 공간(feasibility)을 각각 식별하고, 둘의 정렬과 괴리를 세 도시에 걸쳐 비교하는 것이 목적이다. 이를 통해 계획가가 우선 적용 구역을 판단할 수 있는 재현 가능한 절차를 제시한다.

## 방법론

대상지는 Barcelona(인구 1.7백만, 101.35 km², 16,905 residents/km²), Boston(652천, 125 km², 5,212 residents/km²), Rotterdam(611천, 319 km², 3,000 residents/km²) 세 연안 도시다. 위험도는 IPCC risk framework를 따라 risk = hazard × exposure × SETS vulnerability로 산정하며, hazard는 1-in-100-year(T100) 모형에서 얻은 pluvial flood depth(mm)와 과거 heatwave 기간의 주간 기온(°C), exposure는 population density로 구성한다. feasibility는 green roofs, rain gardens, porous pavement, urban parks 네 유형에 대해 current land use, social acceptance, administrative suitability, ground slope, distance to buildings, underground structures, rooftop slope 지표를 낮음·중간·높음(0, 0.5, 1)으로 분류한 뒤 geometric mean으로 합성하고 0–1로 정규화한다. 모든 지표는 ArcGIS Pro 3.32의 Zonal Statistics로 100×100 m 격자에 조화시켰고, 공간 분석과 시각화는 ArcGIS Pro 3.32와 QGIS 3.34, 통계·민감도 분석은 Python 3.13(pandas, numpy)으로 수행했다. 진단 단계에서는 Moran's I로 공간 군집을, Pearson correlation으로 위험도와 실행 가능성의 정렬을 확인하고, 지표를 ±10% 교란하는 OAT sensitivity analysis와 산술·기하·조화·이차평균 및 중앙값 등 aggregation operator 비교로 견고성을 평가했다. Boston은 green roofs 관련 도시 규모 공간자료가 대부분 없어 해당 유형을 실행 가능성 평가에서 제외했다.

## 결과

모든 지수에서 통계적으로 유의한 양의 공간 자기상관이 나타났다(Moran's I = 0.5–1.0, p < 0.01). heat risk의 군집이 가장 강해 Moran's I가 0.9–1.0에 이르렀고 Rotterdam에서 특히 두드러졌으며, flood risk는 0.6–0.8, feasibility는 0.5–0.7이었다. Rotterdam에서는 social vulnerability와 SETS vulnerability가 exposure(r = 0.73, r = 0.77) 및 heat risk(r = 0.61, r = 0.69)와 강하게 상관했고, 빈곤선 이하 인구는 flood risk r = 0.63, heat risk r = 0.73으로 형평성 신호가 뚜렷했다. Barcelona에서는 impervious surfaces가 heat risk r = 0.79, heat hazard r = 0.62로 도시 형태 중심의 열 패턴을 보였고, green roofs feasibility가 exposure r = 0.62, heat risk r = 0.61, heat hazard r = 0.60으로 정렬되었으며 roof slope(r = 0.97)와 administrative suitability(r = 0.94)가 실행 가능성을 좌우했다. 반면 rain gardens와 urban parks는 위험 지표와 약하거나 음의 상관을 보였고 Rotterdam에서는 flood·heat hazard와 r = -0.25 ~ -0.41이었으며, land use는 모든 도시·유형에서 r = 0.91–0.98로 가장 지배적인 실행 가능성 결정 요인이었다. 민감도 분석에서 지수 변화는 5% 미만으로 안정적이었으나, aggregation 방식에 대해서는 Rotterdam이 가장 견고하고(mean range 0.272) Boston의 flood risk가 가장 민감했다(mean range 0.990).

## 논의

high risk–high feasibility 구역은 즉시 착수 가능한 대상이며, 밀집·고온 지역의 green roofs와 permeable pavements가 대표적이다. high-risk/low-feasibility 지역은 토지 이용과 지하 기반시설이 제약 요인이므로 grey–green 혼합 같은 대안과 별도의 거버넌스·재원 전략이 필요하다. heat 위험은 국지적 개입으로 대응할 수 있으나 flood 위험은 상류 유출과 하수 용량에 좌우되어 유역 규모의 통합 접근을 요구한다는 점에서 hazard별로 전략이 달라야 한다. 한계로는 비교 가능성을 위해 지표를 표준 자료로 축소한 점, social acceptance를 선거 결과로 대리한 점, Global North 세 도시에 한정된 점을 들며, 후속 연구로 drought·wildfire 등 hazard 확장, Global South 적용, 참여형 계획과의 결합을 제시한다.

## 왜 읽을 만한가

위험도와 실행 가능성을 각각 격자 단위로 지수화한 뒤 중첩해 우선순위를 도출하는 절차가 명확해, 국내 도시의 폭염·침수 대응 그린인프라 입지 분석에 그대로 옮겨 적용할 수 있다. 지표 구성과 100×100 m 격자 조화, Moran's I·Pearson 기반 진단 절차가 구체적으로 제시되어 있다.

## 원문 키워드

`Urban Stormwater`, `Urban Heat`, `Nature-based Solutions (NbS)`, `Social-Ecological- Technological Systems (SETS)`, `Resilience`, `Ecosystem Services`

## 원문 링크

- 원문: [https://doi.org/10.1038/s42949-026-00461-7](https://doi.org/10.1038/s42949-026-00461-7)
- PDF: [https://www.nature.com/articles/s42949-026-00461-7_reference.pdf](https://www.nature.com/articles/s42949-026-00461-7_reference.pdf)
- DOI: [https://doi.org/10.1038/s42949-026-00461-7](https://doi.org/10.1038/s42949-026-00461-7)
