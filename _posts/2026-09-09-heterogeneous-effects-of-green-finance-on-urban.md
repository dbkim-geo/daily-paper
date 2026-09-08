---
layout: post
title: "Heterogeneous Effects of Green Finance on Urban Decarbonization: Evidence from 285 Cities in China"
date: 2026-09-09 08:30:00 +0900
topic: "탄소중립"
topic_key: "carbon-neutral"
one_liner: "중국 285개 도시에서 green finance의 carbon intensity 감축 효과를 규명한다"
authors: "Xueyang Li, Jinlei Ma"
venue: "arXiv (preprint)"
published: "2026-06-05"
doi: ""
paper_url: "https://arxiv.org/abs/2606.06986v1"
pdf_url: "https://arxiv.org/pdf/2606.06986v1"
source: "arxiv"
basis: "full_text"
keywords:
  - "green finance"
  - "carbon intensity"
  - "spatial spillover"
  - "causal forest"
  - "XGBoost-SHAP"
  - "mediation analysis"
paper_keywords:
  - "GreenFinance"
  - "CarbonIntensity"
  - "DecarbonizationEffect"
  - "MachineLearning"
  - "City"
---

## 한 줄 요약

**중국 285개 도시에서 green finance의 carbon intensity 감축 효과를 규명한다**

## 초록 요약

green finance가 도시 단위 carbon intensity를 실제로 낮추는지, 어떤 경로로 작동하는지 검증한 연구다. 중국 285개 prefecture-level city의 2000~2022년 패널자료에 계량경제 모형과 machine learning 기반 분석을 함께 적용했다. green finance는 carbon intensity를 유의하게 낮추었고 green bond와 green investment의 효과가 가장 컸으며 인접 도시로의 spatial spillover도 확인되었다. 매개경로는 energy structure 최적화가 가장 크고 industrial upgrading, FDI, technological innovation이 뒤를 이었으며, 효과는 4·5선 도시에서 가장 강했다.

## 주요 차별성

- 분석 단위를 국가·성 단위가 아닌 285개 prefecture-level city로 낮춰 도시 간 이질성을 직접 다룬다.
- random effects panel model, spatial econometric model, causal forest를 하나의 실증 틀에 결합한다.
- green finance를 단일 지수로 보지 않고 green credit, bond, fund 등 7개 하위수단으로 분해해 효과 차이를 비교한다.
- XGBoost-SHAP와 비모수 추정으로 선형 모형이 놓치는 비선형 한계효과와 임계 조건을 식별한다.

## 주요 기여점

- green finance의 평균효과, spatial spillover, 이질적 효과, 비선형 한계효과를 한 논문에서 동시에 제시한다.
- energy structure, industrial structure, FDI, technological innovation의 매개 비중을 정량적으로 분해한다.
- 도시 등급·산업구조·에너지믹스·기술역량에 따라 green finance 효과가 달라지는 조건을 제시해 차등적 정책 설계 근거를 만든다.

## 연구의 배경

도시는 중국 전체 탄소배출의 80% 이상을 차지해 기후 완화 정책의 핵심 무대다. 중국은 2030년 이전 탄소정점, 2060년 carbon neutrality를 공표한 상태다. green finance는 금융자원과 환경목표를 잇는 수단으로 low-carbon transition의 주요 정책도구가 되었다.

## 필요성

기존 연구는 국가, 성, 산업 단위에 집중해 도시 간 경제발전·금융접근성·산업구조 차이를 반영하지 못했다. 대부분 선형 계량모형에 의존해 발전단계별 비선형 한계효과를 포착하지 못한다. 도시 간 정책 모방과 자본 이동으로 생기는 공간적 외부효과도 충분히 다뤄지지 않았다.

## 목적

green finance가 도시 carbon intensity를 유의하게 낮추는지 확인하고, 그 효과가 발전단계·산업구조·기술역량에 따라 어떻게 달라지는지 규명하는 것이 목적이다.

## 방법론

2000~2022년 중국 285개 prefecture-level city 패널자료를 구축했으며 관측치는 6,555개다. 종속변수는 탄소배출량을 GDP로 나눈 carbon intensity이고 배출자료는 EDGAR-v2024를 사용했다. 설명변수인 green finance index는 entropy method로 green credit, green investment, green insurance, green bond, green support, green fund, green equity 7개 하위지표를 통합해 산출했다. random effects panel model을 기본으로 하고, green finance의 시차항, 성 평균, governmental environmental attention, Green Finance Reform and Innovation Pilot Zone을 도구변수로 쓰는 2SLS와 경제·지리 거리를 결합한 spatial weight matrix 기반 spatial econometric model을 함께 추정했다. 여기에 medeff 기반 causal mediation analysis, XGBoost-SHAP 모형, double machine learning 기반 causal forest를 적용해 매개경로와 비선형 한계효과를 분석했다.

## 결과

기본 회귀에서 green finance 계수는 -0.1575로 1% 수준에서 유의했고, 7개 하위수단 중 green bond(-2.3169)와 green investment(-1.7298)의 절대 계수가 가장 컸으며 green credit(-0.5213)과 green fund(-0.5396)은 상대적으로 작았다. 도구변수를 바꾼 2SLS에서도 계수는 -0.053에서 -0.237 범위의 음수로 유지되었고, spatial model의 spillover 계수는 -0.1411(p<0.01)로 인접 도시까지 효과가 미쳤다. 도시 등급별로는 4선(-0.1472)과 5선(-0.1344)이 가장 강했고 3선(-0.1134), 1선(-0.1033), 2선(-0.0841) 순이었다. 매개효과는 energy structure가 총효과의 18.95%로 가장 크고 industrial structure 7.68%, FDI 5.86%, technological innovation 2.32% 순이었다. SHAP 분석에서는 green bond, green fund, green credit의 기여가 컸으며, 한계효과는 에너지구조에 대해 역U자 형태를 보이고 green innovation 지수가 40을 넘으면 뚜렷하게 감소했다.

## 논의

green finance는 평균적으로 효과가 있으나 그 크기는 도시의 에너지믹스, 산업기반, 기술역량, 발전단계에 크게 좌우된다. 구조적으로 취약하거나 제도 기반이 약한 도시에서 한계효과가 커, 전환기 정책수단으로서의 지렛대가 더 크다고 저자들은 해석한다. 다만 매개경로가 설명하는 비중은 부분적이고, 4·5선 도시의 강한 효과가 2002~2011년 이후 약해진 점은 제도적 연속성과 시장 기반 메커니즘의 미성숙을 시사한다. 저자들은 정책형 green finance 도구 강화, 도시 등급별 차등 지원, 도시군 단위 협력체계 구축을 후속 과제로 제시한다.

## 왜 읽을 만한가

계량경제 인과추론과 XGBoost-SHAP, causal forest를 결합해 정책효과의 비선형성과 공간 파급을 함께 다루는 설계가 참고할 만하다. 도시 단위 탄소집약도와 정책수단 효과를 분석하는 국내 연구에 그대로 이식할 수 있는 구조다.

## 원문 키워드

`GreenFinance`, `CarbonIntensity`, `DecarbonizationEffect`, `MachineLearning`, `City`

## 원문 링크

- 원문: [https://arxiv.org/abs/2606.06986v1](https://arxiv.org/abs/2606.06986v1)
- PDF: [https://arxiv.org/pdf/2606.06986v1](https://arxiv.org/pdf/2606.06986v1)
