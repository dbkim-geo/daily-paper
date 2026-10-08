---
layout: post
title: "Unraveling nonlinear impacts of seasonal climate and built environments on exercise walking in high-density cities via a modified machine learning approach"
date: 2026-10-09 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "GW-XGBoost로 고밀도 도시의 계절 기후·건조환경이 운동 보행에 미치는 비선형 효과를 밝힌다."
authors: "Bo Lu, Ting Long, Bo Li, Yu Chen, Lin Zhu"
venue: "International Journal of Health Geographics"
published: "2026-02-06"
doi: "https://doi.org/10.1186/s12942-026-00453-x"
paper_url: "https://doi.org/10.1186/s12942-026-00453-x"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "exercise walking"
  - "built environment"
  - "seasonal climate"
  - "GW-XGBoost"
  - "SHAP"
  - "Walk Score"
paper_keywords:
  - "Built environment"
  - "Seasonal climatic factors"
  - "High density cities"
  - "Exercise walking"
  - "GW- XGBoost"
  - "Health-oriented"
---

## 한 줄 요약

**GW-XGBoost로 고밀도 도시의 계절 기후·건조환경이 운동 보행에 미치는 비선형 효과를 밝힌다.**

## 초록 요약

베이징·우한·광저우 3개 고밀도 도시의 여름·겨울 crowdsourced 보행 궤적을 분석했다. 건조환경, 계절 기후, 사회경제 변수를 geographically weighted XGBoost(GW-XGBoost)에 넣고 SHAP, partial dependence plot, clustering으로 해석했다. Walk Score가 도시·계절 전반에서 가장 안정적이고 영향력 큰 변수였고, 기후 변수 중에서는 AQI와 기온의 영향이 특히 겨울에 컸다. 변수 반응은 지속 증가형·임계값 민감형·변동형의 세 유형으로, 국지 유형은 환경 주도·기능 주도·구조 불균형 지역의 세 유형으로 나뉘었다.

## 주요 차별성

- 기후대가 다른 세 고밀도 도시(Dwa·Cfa·Cwa)를 여름·겨울로 나눠 도시-계절 6개 시나리오를 비교했다.
- geographic weighting을 XGBoost에 결합한 GW-XGBoost로 표본마다 국지 모델을 학습해 spatial heterogeneity를 반영했다.
- utilitarian walking이 아닌 여가형 exercise walking(EW)을 별도 대상으로 다뤘다.
- GVI의 영향력-안정성 사분면 분석과 국지 SHAP 기반 K-means clustering으로 전역·국지 동인을 함께 제시했다.

## 주요 기여점

- 변수의 비선형 반응을 지속 증가형, 임계값 민감형, 변동형의 세 유형으로 정리했다.
- Walk Score 70점, 보행자 가로 길이 약 8 km/km², 건물 높이 10–20 m 등 계획에 쓸 수 있는 임계값을 제시했다.
- 국지 동인을 환경 주도형, 기능 주도형, 구조 불균형·전환형으로 유형화하고 유형별 계획 전략을 제안했다.
- 베이징은 여름 27.8°C 초과 시 보행이 급감하는 등 남북 도시 간 기온 임계값 차이를 보였다.

## 연구의 배경

WHO에 따르면 신체활동 부족은 전 세계 사망의 6%를 차지한다. 보행은 가장 접근성 높은 운동이며 저탄소 도시 이동에도 기여한다. 건조환경 연구는 "5D" 프레임워크를 기반으로 발전했고, 최근에는 GBDT, Random Forest, XGBoost와 SHAP을 이용한 비선형 분석이 늘었다.

## 필요성

기존 연구는 주로 서구 도시의 가로·근린 단위에 머물렀고, 단일 기후대만 다루는 경우가 많았다. 보행 유형 구분이 약해 운동 보행의 동인이 따로 규명되지 않았다. 전역 머신러닝 모델은 spatial heterogeneity를 충분히 반영하지 못한다.

## 목적

고밀도 도시에서 건조환경과 계절 기후가 운동 보행에 미치는 비선형 효과를 전역·국지 수준에서 규명한다. 이를 통해 건강 지향적이고 기후 적응적인 도시계획에 근거를 제공한다.

## 방법론

피트니스 앱 Duo Rui의 2018년 1월–2019년 2월 보행 궤적을 사용했고, 6–8월을 여름, 12–2월을 겨울로 구분했다. 연구 지역은 인구밀도 10,000명/km² 이상인 세 도시 중심부(베이징 약 1,379 km², 우한 965 km², 광저우 1,473 km²)이며, 500 m × 500 m 격자별 궤적 수를 종속변수로 삼았다. 독립변수는 "5D" 기반 건조환경, Temp·HiTIC·습도·최대풍속·AQI의 계절 기후, 인구밀도·GDP·주택가격의 사회경제 변수로 구성했다. GW-XGBoost는 Haversine 거리와 Gaussian kernel 가중치로 표본별 국지 모델(최소 80개 이웃)을 학습하고, Bayesian optimization 30회와 5-fold cross-validation으로 튜닝했다. 80/20 분할로 OLS, GWR, Random Forest, XGBoost와 비교했고, SHAP, PDP, LISA, K-means clustering으로 결과를 해석했다.

## 결과

GW-XGBoost는 모든 도시-계절에서 비교 모델보다 높은 R²와 낮은 RMSE·MAE를 보였으나, 본문에는 구체적 수치가 보충자료로 넘겨져 있다. 운동 보행의 Moran's I는 약 0.5(p<0.05)였고 도심부에 high-high cluster가 형성됐으며, 계절 차이는 베이징에서 가장 컸다. Walk Score는 70점을 넘으면 SHAP 값이 양수로 바뀌었고, 인구밀도는 베이징·우한 10,000명/km², 광저우 5,000명/km²에서 효과가 정체됐다. 교통 정류장 밀도는 격자당 약 10개, 교차로 밀도는 약 25개에서 효과가 정체됐다. 베이징은 여름 27.8°C를 넘으면 보행이 급감하고 겨울에는 -3°C 이상에서 증가했으며, 우한·광저우는 겨울 기온 상승과 보행이 음의 관계를 보였다.

## 논의

보행 친화 가로, 밀도 임계값 관리, climate-sensitive design이 계절에 관계없는 보행을 유도하는 핵심 수단으로 제시됐다. 공원·캠퍼스에는 미기후 회복력 강화를, 상업지에는 밀도·기능 혼합 최적화를, 대형 가구 지역에는 "small blocks + mixed use + micro-greening"을 권고했다. 한계로 2018–2019년 자료의 시의성, 개인 속성 변수 부재, 1년치 기후 자료, 거시 스케일 분석, 기후-건조환경 상호작용 미분석을 들었다. 본 요약의 근거 본문은 Research Square 프리프린트 v1이므로 출판본과 일부 수치가 다를 수 있다.

## 왜 읽을 만한가

GeoXAI 기법을 도시계획 의사결정에 쓸 임계값으로 연결한 사례다. 기후대별 비교 설계는 한국 고밀도 도시의 기후 적응형 보행 환경 연구에 참고가 된다.

## 원문 키워드

`Built environment`, `Seasonal climatic factors`, `High density cities`, `Exercise walking`, `GW- XGBoost`, `Health-oriented`

## 원문 링크

- 원문: [https://doi.org/10.1186/s12942-026-00453-x](https://doi.org/10.1186/s12942-026-00453-x)
- DOI: [https://doi.org/10.1186/s12942-026-00453-x](https://doi.org/10.1186/s12942-026-00453-x)
