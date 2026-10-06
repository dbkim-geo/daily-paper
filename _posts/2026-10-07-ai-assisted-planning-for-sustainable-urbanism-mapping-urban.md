---
layout: post
title: "AI-Assisted Planning for Sustainable Urbanism: Mapping Urban Livability in a Contemporary American City through Tree Coverage"
date: 2026-10-07 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "tree canopy coverage 가중 취약성 지수로 Austin의 도시 취약성을 육각 격자 단위로 지도화한 연구다."
authors: "Kunth Shah, Edwin Flores"
venue: "Journal of Contemporary Urban Affairs"
published: "2026-09-29"
doi: "https://doi.org/10.25034/ijcua.2026.v10n2-5"
paper_url: "https://doi.org/10.25034/ijcua.2026.v10n2-5"
pdf_url: "https://ijcua.com/ijcua/article/download/647/763"
source: "openalex"
basis: "full_text"
keywords:
  - "urban vulnerability"
  - "tree canopy coverage"
  - "hexagonal tessellation"
  - "K-Means"
  - "Random Forest"
  - "zoning"
figure: "/assets/figures/2026-10-07-ai-assisted-planning-for-sustainable-urbanism-mapping-urban.png"
---

## 한 줄 요약

**tree canopy coverage 가중 취약성 지수로 Austin의 도시 취약성을 육각 격자 단위로 지도화한 연구다.**

![원문 대표 그림]({{ '/assets/figures/2026-10-07-ai-assisted-planning-for-sustainable-urbanism-mapping-urban.png' | relative_url }})

*원문에서 발췌 — Kunth Shah 외, Journal of Contemporary Urban Affairs, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

Texas주 Austin을 대상으로 ArcGIS 기반 공간분석과 KNIME 기반 machine learning을 결합해 도시 livability와 취약성을 평가한다. 환경·건강·사회경제·인프라 4개 영역 10개 변수로 composite vulnerability index를 만들고, tree canopy coverage를 flexible variable로 더한 weighted index를 추가로 구성한다. census tract 자료를 hexagonal tessellation으로 재구성하고 K-Means로 위험 등급을, Random Forest로 재현성을 검증한다. 고취약 지역은 Austin 동부·남동부에 집중되며, zoning overlay로 계획 우선 지구를 도출한다.

## 주요 차별성

- tree canopy coverage를 독립 지표나 동일 가중 지표가 아닌 weighted flexible variable로 composite index에 넣는다. flexible variable만 바꾸면 같은 틀을 다른 계획 질문에 적용할 수 있다.
- census tract 대신 100,000㎡ hexagonal tessellation을 분석 단위로 써서 행정경계의 크기 편차와 choropleth 왜곡을 줄인다.
- 취약성 점수를 Austin zoning map에 중첩해 특정 용도지역 단위의 계획 우선순위로 전환한다.

## 주요 기여점

- City of Austin, CDC 500 Cities, U.S. Census ACS 공개 데이터로 4개 영역 10개 변수의 Composite Urban Vulnerability Index를 구축했다.
- ArcGIS Pro와 KNIME을 연결한 GIS–ML workflow를 제시했다. 고급 데이터과학 훈련 없이도 실무자가 재현할 수 있다는 점을 강조한다.
- K-Means 군집화로 5단계 위험 등급 지도를 만들고 Random Forest로 지수 구조의 재현성을 검증했다.
- Industrial, Commercial, Planned Unit Development 지구를 canopy·green infrastructure 투자 우선 지역으로 제시했다.

## 연구의 배경

도시는 급속한 도시화, 기후변화, 사회공간적 불평등의 복합 압력을 받고 있다. Austin은 2020~2024년 사이 250,000명 이상 인구가 늘어난 고성장 도시다. 1928년 City Plan이 지정한 East Avenue(현 Interstate 35)는 흑인·라틴계 공동체를 분리하는 경계로 작동했고, 그 분할이 현재의 환경 위험과 사회경제적 불이익 분포에 남아 있다.

## 필요성

기존 urban vulnerability 평가는 '취약'의 정의에 합의가 없어 지수 구성 방식에 따라 결과가 크게 달라진다. 가중 방식은 견고한 기준과 재현 가능한 정량 근거가 부족하다는 비판을 받는다. 개발 압력이 큰 Austin 같은 도시에서는 엄밀하고 적용 가능한 분석 도구가 더 필요하다.

## 목적

4개 영역의 Composite Urban Vulnerability Index와 tree canopy coverage를 가중한 Weighted Vulnerability Index를 구축하고, ML로 그 신뢰성을 검증하는 것이 목적이다. 연구 질문은 취약성 군집이 canopy 결핍을 넘어 환경 불평등 전반을 반영하는지, canopy 가중 지수가 일반 지수보다 계획적 활용도가 높은지 두 가지다.

## 방법론

연구 지역은 Austin 시 경계이며, 2022~2024년 자료의 10개 변수(flood %, CO2 emissions, heat island, mental·physical health %, household income, below poverty %, minority status, impervious cover %, sidewalk conditions)와 2024년 tree canopy %를 사용한다. 2022 TIGER/Line census tract에 자료를 결합한 뒤, 100,000㎡ 크기의 hexagonal tessellation에 최대 교차 면적 기준 spatial join으로 옮긴다. KNIME에서 min-max normalization 후 4개 영역 평균을 다시 평균해 일반 지수(VulScore)를 만들고, VulScore 0.3과 canopy 변수 0.7의 가중합으로 VulScore_wTree%를 만든다. K-Means로 두 지수를 각각 5개 군집(Low~High Risk)으로 나누고, 70% stratified partition과 100개 tree의 Random Forest로 재현성을 평가한다. 마지막으로 Considerable·High Risk 육각형을 Austin zoning map에 중첩한다.

## 결과

K-Means 군집화에 쓰인 점수 범위는 VulScore 0.21~0.69, VulScore_wTree% 0.06~0.84다. 일반 지수에서 고취약 지역은 중앙·동부 Austin에서 남동부로 이어지는 연속된 구역에 모이고, 서부·북서부는 낮다. canopy를 70% 가중하면 동부·남동부의 고취약 구역이 넓어지고 강도가 높아지며, canopy가 많은 서부는 낮은 점수를 유지한다. Random Forest 재현율은 3.3.4절에서 VulScore 97.33%(error 2.67%), VulScore_wTree% 98.32%(error 1.678%)로 보고된다. 반면 4.3절은 70/30 split 50회 반복 기준 각각 85.3%, 79.1%로 서로 다른 수치를 제시한다. zoning overlay에서는 남동부의 Industrial, Commercial, Planned Unit Development 지구에 고취약 단위가 가장 많이 몰렸다.

## 논의

고취약 패턴은 1928년 City Plan과 Interstate 35 축의 역사적 분할과 공간적으로 겹치며, 저자들은 이를 인과가 아닌 공간적 연관으로 해석한다. canopy-소득 관계와 redlining 지역의 canopy 결핍을 보고한 선행연구(Schwarz et al. 2015, Locke et al. 2021)와 일치하는 결과를 도시 내부의 세밀한 해상도로 보여준다. 한계로 0.7 가중치가 분석적 판단이라 sensitivity analysis가 필요하고, 육각형 크기에 따른 modifiable areal unit problem 검토, 데이터 불확실성 전파, 2022년 단일 시점이라는 점을 든다. 후속 연구로 spatial autocorrelation·multi-scale 진단, 다른 고성장 도시 비교, 종단 분석, 참여형 자료 결합, 개발 시나리오 예측 모델을 제안한다.

## 왜 읽을 만한가

공개 데이터와 ArcGIS·KNIME만으로 다영역 취약성 지수를 만들고 zoning 단위 정책 우선순위까지 연결하는 절차가 단계별로 제시되어 국내 도시 녹지 형평성 분석에 옮겨 보기 쉽다. 다만 가중치 설정 근거와 본문 내 Random Forest 수치 불일치는 비판적으로 읽을 필요가 있다.

## 원문 링크

- 원문: [https://doi.org/10.25034/ijcua.2026.v10n2-5](https://doi.org/10.25034/ijcua.2026.v10n2-5)
- PDF: [https://ijcua.com/ijcua/article/download/647/763](https://ijcua.com/ijcua/article/download/647/763)
- DOI: [https://doi.org/10.25034/ijcua.2026.v10n2-5](https://doi.org/10.25034/ijcua.2026.v10n2-5)
