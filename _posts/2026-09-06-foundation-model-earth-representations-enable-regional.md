---
layout: post
title: "Foundation-Model Earth Representations Enable Regional-Scale Forest Aboveground Biomass Monitoring Across the Northeastern United States"
date: 2026-09-06 08:30:00 +0900
topic: "탄소저감"
topic_key: "carbon-reduction"
one_liner: "AlphaEarth 위성 embedding으로 미국 북동부 산림 AGB를 연 단위로 추정한다"
authors: "Shashika Lamahewage, Chandi Witharana"
venue: "arXiv (preprint)"
published: "2026-06-25"
doi: ""
paper_url: "https://arxiv.org/abs/2607.27217v1"
pdf_url: "https://arxiv.org/pdf/2607.27217v1"
source: "arxiv"
basis: "full_text"
keywords:
  - "Google Satellite Embeddings"
  - "AlphaEarth Foundation Model"
  - "aboveground biomass"
  - "airborne LiDAR"
  - "XGBoost"
  - "spatial autocorrelation"
paper_keywords:
  - "Google Satellite Embeddings"
  - "Machine Learning"
  - "LiDAR"
  - "Forest Aboveground Biomass"
---

## 한 줄 요약

**AlphaEarth 위성 embedding으로 미국 북동부 산림 AGB를 연 단위로 추정한다**

## 초록 요약

산림 aboveground biomass(AGB)는 육상 탄소 저장량의 핵심 지표지만, 현장 인벤토리와 airborne LiDAR의 성긴 공간·시간 coverage가 지역 규모 모니터링을 제약한다. 저자들은 AlphaEarth Foundation Model이 생성한 Google Satellite Embeddings(GSE)를 미국 북동부 온대림의 AGB 추정에 적용했다. 연간 GSE 관측, airborne LiDAR, Northeastern Forest Inventory Network(NEFIN)의 continuous forest inventory 자료를 machine learning framework로 통합했다. LiDAR와 GSE를 결합한 모델은 R² 0.79를, 연간 GSE로 학습 자료를 10배 이상 늘린 경우 R² 0.82를 기록했다.

## 주요 차별성

- AlphaEarth Google Satellite Embeddings를 산림 AGB 추정에 적용한 첫 체계적 프레임워크다.
- 실제 좌표가 공개되지 않는 FIA 대신 NEFIN continuous forest inventory 자료를 airborne LiDAR·GSE와 함께 지역 규모 AGB 모델링에 처음 사용했다.
- 연간 갱신되는 GSE 시계열과 AGB 생장 보정을 결합해, LiDAR coverage에 묶여 있던 학습 표본을 589개에서 6,801개로 확장했다.
- Moran's I 기반 잔차 공간자기상관 진단과 Monte Carlo 안정성 분석을 모델 비교 절차에 함께 넣었다.

## 주요 기여점

- 공간적으로 불균등한 CFI 자료와 다년도 LiDAR, 연간 GSE를 하나의 AGB 추정 파이프라인으로 통합했다.
- LiDAR-only, GSE-only, LiDAR+GSE 세 예측변수 그룹에서 Random Forest, XGBoost, ExtraTrees의 성능을 정량 비교했다.
- spatial covariate 도입이 LiDAR-only 모델의 Moran's I를 약 50~80% 낮추는 것을 보였고, 결합 모델에서는 잔차 공간 종속성이 통계적으로 유의하지 않게 됐다.
- LiDAR가 없는 지역에서 연간 AGB 지도를 만들 수 있는 확장 가능한 대안 경로를 제시했다.

## 연구의 배경

산림은 약 861 Gt의 탄소를 저장하는 주요 carbon sink이며, 온대림은 생태계 지상부 탄소의 약 34%를 차지한다. 미국 북동부(NEUSA)는 국토의 70% 이상이 산림이지만 1990~2010년 사이 매일 31 ha가 비산림으로 전환됐다. 현장 기반 AGB 추정만으로는 이런 변화 속도를 따라가기 어렵다.

## 필요성

US Forest Service의 FIA 실제 플롯 좌표가 더는 연구자에게 공개되지 않아 지역 규모 공간 모델의 보정·검증 자료가 부족하다. LiDAR는 3차원 구조 정보가 풍부하지만 취득 시기와 범위가 제한되고, 광학 영상은 수직 구조에 둔감하다. 전 지구적으로 매년 갱신되는 Earth observation foundation model 표현이 이 공백을 메울 수 있는지는 생태 분야에서 거의 검증되지 않았다.

## 목적

NEFIN-CFI, airborne LiDAR, AlphaEarth GSE를 통합해 미국 북동부 7개 주의 AGB를 추정하는 통일된 framework를 구축하는 것이 목적이다. 아울러 LiDAR와 GSE 예측변수의 설명력 기여를 평가하고 RF, XGBoost, ExtraTrees의 정확도를 비교한다.

## 방법론

대상 지역은 CT, MA, ME, NH, NY, RI, VT 등 미국 북동부 7개 주로 28만 km² 이상이다. 플롯 AGB는 Chojnacky et al.의 allometric equation으로 DBH 12.7 cm 이상 개체를 합산해 산정했고, 연속 측정 간 연간 생장률(ΔAGB)로 LiDAR·GSE 취득 연도에 맞춰 보정했다. 예측변수는 USGS-3DEP airborne LiDAR(2011~2025년, pulse density 1~20 points/m²)에서 유도한 29개 구조 지표와, Google Earth Engine의 연간 GSE(2017~2025년, 10 m 해상도 64개 feature)를 플롯 단위 최대·평균·최소·표준편차로 요약한 256개 변수다. GSE 변수는 PCA로 차원을 줄여 누적 분산 95%를 설명하는 54개 principal component만 남기고, 위경도와 그 다항·교호항으로 만든 spatial covariate를 덧붙였다. RF, XGBoost, ExtraTrees를 GridSearchCV와 10-fold cross-validation으로 튜닝해 80:20 hold-out으로 평가하고, 100회 Monte Carlo 반복과 permutation 기반 변수군 민감도 분석을 수행했다.

## 결과

LiDAR와 GSE를 결합하고 spatial correction과 tuning을 적용한 XGBoost 모델(XG3_T)은 589개 플롯 기준 R² 0.79, MAE 237.05 Mg ha⁻¹를 기록했다. 단일 소스에서는 LiDAR-only 최적 모델(RF1_T)이 R² 0.79, MAE 225.40 Mg ha⁻¹였고 GSE-only 최적 모델(XG2_T)은 R² 0.67, MAE 292.13 Mg ha⁻¹에 그쳤다. GSE 시계열로 표본을 6,801개로 늘린 Scenario II에서는 tuned XGBoost가 R² 0.82, MAE 245.23 Mg ha⁻¹로 전체 최고 성능을 냈고, 초록 기준 model bias는 70% 이상 줄었다. 잔차 Moran's I는 spatial covariate 도입 후 LiDAR-only 모델에서 약 50~80% 감소했고, 결합 XGBoost 모델은 -0.0095(p>0.05)까지 낮아졌다. Monte Carlo 100회 반복에서 hyperparameter tuning은 R² 표준편차를 9.40~27.90% 줄였다.

## 논의

저자들은 LiDAR coverage가 없는 지역에서도 GSE와 spatial predictor 조합이 연 단위 AGB 추정의 대안이 될 수 있다고 본다. 다만 표본이 600개 미만일 때는 LiDAR 구조 지표를 함께 쓰는 편이 여전히 유리했고, GSE-only 모델은 LiDAR-only 대비 R²가 약 17.91% 낮고 RMSE·MAE가 20% 이상 컸다. 한계로는 embedding feature의 black-box 특성으로 생태적 해석이 어렵다는 점, 600 Mg ha⁻¹를 넘는 극단 AGB 플롯에서 오차가 커진 점, 30 m를 넘을 수 있는 CFI 플롯 위치 오차와 프로그램별로 7~20 m로 다른 플롯 크기, 이 연구에서 평가하지 않은 allometric 불확실성을 든다. 후속 연구로는 기온·강수·고도·경사 같은 기후·지형 변수 추가와 공간적으로 대표성 있는 산림 인벤토리 체계 확충을 제안한다.

## 왜 읽을 만한가

foundation model 기반 geospatial embedding이 기존 LiDAR·광학 자료를 어디까지 대체할 수 있는지 정량 비교한 사례라, GeoAI를 탄소 모니터링에 적용하려는 연구에 직접 참고가 된다. PCA, spatial covariate, Monte Carlo 안정성 검토까지 포함한 절차 설계도 그대로 벤치마킹할 만하다.

## 원문 키워드

`Google Satellite Embeddings`, `Machine Learning`, `LiDAR`, `Forest Aboveground Biomass`

## 원문 링크

- 원문: [https://arxiv.org/abs/2607.27217v1](https://arxiv.org/abs/2607.27217v1)
- PDF: [https://arxiv.org/pdf/2607.27217v1](https://arxiv.org/pdf/2607.27217v1)
