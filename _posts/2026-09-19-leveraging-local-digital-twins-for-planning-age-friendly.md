---
layout: post
title: "Leveraging Local Digital Twins for planning age-friendly urban environments"
date: 2026-09-19 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "Local Digital Twin으로 근린 고령친화성을 평가하고 개입 효과를 시뮬레이션한다"
authors: "Asel Villanueva-Merino, Silvia Urra-Uriarte, José Luis Izkara, Sergio Campos-Cordobes, Andoni Aranguren, Patricia Molina-Costa"
venue: "Cities"
published: "2024-10-14"
doi: "https://doi.org/10.1016/j.cities.2024.105458"
paper_url: "https://doi.org/10.1016/j.cities.2024.105458"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "Local Digital Twin"
  - "age-friendly city"
  - "CityGML"
  - "Analytic Hierarchy Process"
  - "isochrone"
  - "urban planning"
---

## 한 줄 요약

**Local Digital Twin으로 근린 고령친화성을 평가하고 개입 효과를 시뮬레이션한다**

## 초록 요약

이 연구는 Local Digital Twin(LDT)을 활용해 고령친화 도시환경 계획을 지원하는 방법을 다룬다. EU Horizon 2020 URBANAGE 프로젝트에서 GIS 데이터, data analytics, artificial intelligence를 결합한 Long-Term Urban Planner(LTUP) 도구를 스페인 Santander에 구축했다. 공공공간 개입 제안과 미래 인구구조 변화 대응이라는 두 use case로 도구를 검증했다. 핵심 기여는 재사용과 이식이 쉬운 modular component 기반 LDT의 정의와 구현이다.

## 주요 차별성

- modular component 기반으로 LDT를 구성해 다른 도시로의 재사용과 적응을 쉽게 했다.
- 기술 영역에 사회적 차원을 결합한 통합 접근으로 고령친화성을 다뤘다.
- Euclidean distance 대신 경사와 접근성을 반영한 Age-Friendly Route Planner와 isochrone overlapping으로 고령자의 실제 도달 범위를 산정했다.
- 고령자와 공무원이 참여한 co-creation으로 지표와 도구 기능을 정의했다.

## 주요 기여점

- CIM, AFNI, Solutions Catalogue, AFIS, AHP 기반 multicriteria analysis를 통합한 Long-Term Urban Planner(LTUP) 도구를 구현했다.
- 4개 domain, 12개 topic, 36개 indicator로 구성된 Age-Friendly Neighbourhood Index(AFNI)를 Delphi method로 가중치까지 확정해 근린 단위 평가를 가능하게 했다.
- 공공공간 개입과 인구구조 변화 대응이라는 두 use case로 시뮬레이션 기반 의사결정 절차를 실증했다.
- Santander 공무원 평가를 통해 data governance와 역량 강화가 LDT 운영의 전제임을 확인했다.

## 연구의 배경

유럽 인구의 75%가 도시에 거주하며 2050년에는 80%를 넘을 것으로 전망된다. 65세 이상 인구 비율도 34%에 이를 것으로 예측된다. 그러나 기존 도시계획은 부문별로 분절된 방식에 머물러 인구구조 변화에서 비롯된 요구를 충분히 반영하지 못한다.

## 필요성

WHO의 age-friendly city 프레임워크는 여덟 개 영역에 걸친 통합적 평가를 요구하지만, 기존 GIS 기반 도구는 개별 분석에 머문다. 고령자의 의사결정 참여 부족, 고령자 관련 데이터 공백, 시나리오 시뮬레이션의 활용 미흡이 공통 한계로 지적된다. 상용 mobility simulation 도구도 휴식 공간, 공공화장실, 손잡이 같은 고령자 편의 요소를 다루지 않는다.

## 목적

LDT가 도시계획에서 고령친화 환경 조성을 어떻게 촉진할 수 있는지 규명하는 것이 목적이다. 이를 위해 근린의 고령친화성을 평가하고 도시 개입의 효과를 모델링하는 modular LDT를 설계하고 구현한다.

## 방법론

연구 지역은 2022년 기준 65세 이상 인구가 26.28%인 스페인 북부 도시 Santander다. City Information Model(CIM)은 cadastre, OpenStreetMap, 지자체 open data를 FME 기반 ETL로 처리해 CityGML LoD1의 3D 모델로 구축하고 3DCityDB에 저장했으며, 웹 시각화를 위해 3DTiles로 변환했다. Age-Friendly Neighbourhood Index(AFNI)는 4개 domain, 12개 topic, 36개 indicator로 구성되며, 7개국 전문가 18명이 참여한 Delphi method로 domain과 indicator 가중치를 정했다. Age-Friendly Index Simulator(AFIS)는 네 가지 AI 알고리즘을 포함하는데, OpenTripPlanner의 A* routing에 경사와 접근성을 반영한 Age-Friendly Route Planner, isochrone overlapping 기반 이동성 분석, Solutions Catalogue에서 대안을 고르는 metaheuristic optimisation, 수직 이동 인프라 입지 최적화 모델이다. domain 가중치는 Analytic Hierarchy Process(AHP) 기반 multicriteria analysis로 사용자가 재조정한다.

## 결과

Santander의 65세 이상 인구 비율 26.28%는 Cantabria 평균 23.1%와 스페인 전체 약 20%를 웃돈다. use case 1에서는 Domain 1(outdoor spaces and buildings) 점수가 낮은 근린으로 Camarreal(AFNI 5.99), La Torre(6.61), La Albericia(7.62)가 추출됐고, 65세 이상 비율이 15.62%로 낮은 La Albericia는 우선순위에서 제외됐다. park 시뮬레이션에서 small park는 효과가 미미했고 large park는 지표가 최대치를 넘어, 비용을 고려해 medium park 두 곳 조성이 선택됐으며, 사전 계산된 isochrone을 사용해 계산은 3분 이내에 끝났다. use case 2에서는 Entrehuertas-Prado-San Roque 근린에 protected flats와 social rental housing을 도입하는 시나리오에서 Domain 3 점수가 0에서 32로 올라 전체 AFNI가 12.15에서 23.03으로 상승했다. Santander 공무원 대상 평가에서는 도구의 신뢰도와 활용 가치가 높게 나타났고, 데이터 갱신 시점 표기와 사전 교육의 필요성이 함께 제기됐다.

## 논의

URBANAGE LDT는 Gemini principles의 purpose, trust, function에 부합하며 Atkins/IET maturity model 기준 Level 3에 도달했고 Level 4를 지향한다. 다만 open data와 2D cartography에 의존해 CIM의 정확도에 한계가 있고, 일부 AFNI indicator는 데이터 부족으로 측정되지 못했다. AHP는 비전문가도 쓰기 쉽지만 indicator 수가 늘면 쌍대비교 조합이 지수적으로 증가해 적용 범위가 제한되며, Age-Friendly Route Planner는 경사에 따른 보행 속도 변화를 반영하지 못한다. 후속 연구로는 real-time data를 시뮬레이션에 반영하는 것, 시뮬레이션 결과가 다른 시뮬레이션에 미치는 영향을 다루는 것, 일반 시민에게 digital twin을 개방하기 위한 인터페이스 단순화가 제시된다.

## 왜 읽을 만한가

GIS 데이터와 AI를 도시계획 의사결정 절차에 실제로 연결한 구현 사례로, digital twin을 근린 단위 지표 및 시뮬레이션과 묶는 설계를 참고할 수 있다. 지표 설계부터 공무원 수용성 평가까지 전 과정을 기록해 유사한 도구를 기획할 때 유용하다.

## 원문 링크

- 원문: [https://doi.org/10.1016/j.cities.2024.105458](https://doi.org/10.1016/j.cities.2024.105458)
- DOI: [https://doi.org/10.1016/j.cities.2024.105458](https://doi.org/10.1016/j.cities.2024.105458)
