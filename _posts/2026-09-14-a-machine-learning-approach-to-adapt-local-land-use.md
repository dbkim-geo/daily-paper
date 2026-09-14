---
layout: post
title: "A Machine Learning Approach to Adapt Local Land Use Planning to Climate Change"
date: 2026-09-14 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "zoning plan 규제 데이터로 필지의 soil sealing을 ML로 예측하는 방법을 시험한다."
authors: "Julia Forster, Stefan Bindreiter, Birthe Uhlhorn, Verena Radinger-Peer, Alexandra Jiricka-Pürrer"
venue: "Urban Planning"
published: "2024-10-22"
doi: "https://doi.org/10.17645/up.8562"
paper_url: "https://doi.org/10.17645/up.8562"
pdf_url: "https://www.cogitatiopress.com/urbanplanning/article/download/8562/3997"
source: "openalex"
basis: "full_text"
keywords:
  - "machine learning"
  - "soil sealing"
  - "nature-based solutions"
  - "Random Forest"
  - "zoning plan"
  - "spatial planning"
figure: "/assets/figures/2026-09-14-a-machine-learning-approach-to-adapt-local-land-use.png"
---

## 한 줄 요약

**zoning plan 규제 데이터로 필지의 soil sealing을 ML로 예측하는 방법을 시험한다.**

![원문 대표 그림]({{ '/assets/figures/2026-09-14-a-machine-learning-approach-to-adapt-local-land-use.png' | relative_url }})

*원문에서 발췌 — Julia Forster 외, Urban Planning, 2024. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

기초자치단체는 계획 결정이 환경에 미치는 영향을 분석할 데이터와 전문성이 부족하다. 이 연구는 오스트리아 Upper Austria의 단독주택지를 사례로 과거·현재 계획규제를 물리적 환경 데이터와 연결한다. nature-based solutions(NBS) 판단을 위한 면적 유형 목록을 만들고 이를 ML 학습 데이터로 구축한다. 모델은 계획 결정이 soil sealing에 미치는 영향을 예측하며, 신뢰할 만한 계획 판단에는 더 많은 데이터가 필요함을 보인다.

## 주요 차별성

- ML을 토지이용 변화 예측이나 영상 객체 추출에 쓰던 기존 연구와 달리, 오픈스페이스 구성을 그 밑에 있는 planning regulation과 직접 연결해 학습 데이터를 만든다.
- Drachenfels(2021) 분류를 바탕으로 포장면·건물·정원 유형 등을 포함한 ML4Nature surface category를 정의하고 필지 하위 구역(subarea)에 부여한다.
- 대도시가 아닌 역량이 제한된 중소 기초자치단체의 계획 실무를 대상으로 삼는다.

## 주요 기여점

- NBS 잠재력 자동 평가를 위한 5단계 ML4Nature 개념과 그중 학습 단계(Steps 1–3)인 MLbase4NBS 방법을 제시한다.
- zoning plan 문서 8건을 디지털로 통일하고 지적 데이터와 중첩해 1,404개 subarea, 132개 필지의 학습 데이터셋을 구축한다.
- KNN, Random Forest, SVR로 면적 유형 분류와 필지 sealed area 비율 회귀를 시험하고, 소규모 데이터에서 발생하는 overfitting 문제와 데이터 확장 전략을 보고한다.

## 연구의 배경

기초자치단체의 공간계획은 기후변화 적응·완화에 핵심적이다. 비포장 토양은 NBS를 배치하고 연결하는 데 필요한 자원이다. 그러나 중소 지자체에서는 soil sealing이 빠르게 진행되고 NBS 적용은 자주 간과된다.

## 필요성

중소 지자체는 자원·지식·인력이 부족해 계획규제와 결정이 초래하는 sealing 결과를 추적하지 못한다. 데이터 부족과 선형 모델의 한계로 계획 조치의 사전 평가(ex-ante evaluation)도 불충분하다. 계획규제와 토지피복 패턴의 상관을 분석한 ML 연구는 아직 없다.

## 목적

계획규제와 실제 계획 결정을 물리적 환경 데이터와 연결해, 계획 결정이 soil sealing과 면적 유형에 미치는 영향을 예측하는 ML 모델의 학습 기반을 구축하고 그 실현 가능성을 검토한다.

## 방법론

대상지는 Upper Austria Hörsching의 단독주택지 10 ha이며, 오스트리아 주거 건물의 64%가 단독주택이라는 점에서 선정됐다. 수작업으로 georeference한 개발·zoning plan, orthophoto(Geoland, Google Maps), BEV 지적 데이터, 현장 조사를 결합해 subarea를 10개 ML4Nature category로 수동 분류했다. 분류 문제는 필지 규모, 둘레-면적비, 이전 토지이용, 층수·용적률 등 계획규제와 좌표를 포함한 26개 속성으로 subarea의 category를 예측한다. 회귀 문제는 15개 필지 수준 속성으로 필지의 sealed area 비율을 예측한다. KNN, Random Forest, SVR(회귀만)을 test size 30%로 평가했고, 데이터 확장을 위해 2 m point grid와 ±5% noise 추가를 시험했다.

## 결과

사례지 전체 면적의 47% 이상이 건물·도로·기타 포장면으로 sealed 상태다. polygon 기반 분류(N=1,404)의 accuracy는 KNN 0.384, Random Forest 0.382로 무작위 수준(10%)보다는 높지만 부정확하다. 2 m point grid(N=24,703)에서는 KNN 0.967, Random Forest 0.983으로 급등해 강한 overfitting을 보였고, 도로 제외 시(N=20,682)에도 각각 0.962, 0.983으로 소폭만 낮아졌다. 회귀는 필지 132개(Test A)에서 KNN 0.541, Random Forest 0.342, SVR 0.358이었고 KNN 값은 계산마다 크게 변동했다. N=495(Test B)에서는 Random Forest 0.907, KNN 0.870, SVR 0.714였고, ±5% noise를 추가한 Test C에서는 각각 0.861, 0.810, 0.745였다.

## 논의

저자들은 데이터를 확장하고 변동성을 부여하면 overfitting이 줄고 예측이 개선된다고 보지만, 소표본에서는 cross-validation의 타당성을 보장하기 어렵다. 데이터 수집이 가장 노동집약적이며, 결측은 iterative imputation이나 지역 전문지식으로 보완할 수 있다. 실무 적용을 위해서는 학습 데이터를 연방 차원에서 구축하고 유사한 정주 구조의 지역별로 공동 학습해야 하며, 주마다 다른 계획규제를 표준화해야 한다. NBS equipment(수목, 산울타리 등) 반영과 NBS 잠재력 산정 단계(Step 5)는 이번 연구에 포함되지 않았고, 기후학자·생물학자와의 협업 및 이해관계자 워크숍이 후속 과제로 제시된다.

## 왜 읽을 만한가

계획규제 속성을 ML feature로 설계하는 구체적 방식과, 소규모 데이터에서 point grid 확장이 overfitting으로 이어진 실패 사례를 함께 볼 수 있다. 지자체 단위 토지이용 규제와 탄소중립·기후적응을 연결하려는 연구에 참고가 된다.

## 원문 링크

- 원문: [https://doi.org/10.17645/up.8562](https://doi.org/10.17645/up.8562)
- PDF: [https://www.cogitatiopress.com/urbanplanning/article/download/8562/3997](https://www.cogitatiopress.com/urbanplanning/article/download/8562/3997)
- DOI: [https://doi.org/10.17645/up.8562](https://doi.org/10.17645/up.8562)
