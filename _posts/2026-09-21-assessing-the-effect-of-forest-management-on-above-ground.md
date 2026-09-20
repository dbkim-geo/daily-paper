---
layout: post
title: "Assessing the effect of forest management on above-ground carbon stock by remote sensing"
date: 2026-09-21 08:30:00 +0900
topic: "탄소저감"
topic_key: "carbon-reduction"
one_liner: "관리림과 비관리림의 산림 탄소량 차이를 다중센서 원격탐사로 검증한 연구"
authors: "Sofie Van Winckel, Johan Simons, Stef Lhermitte, Bart Muys"
venue: "Biogeosciences"
published: "2025-08-28"
doi: "https://doi.org/10.5194/bg-22-4291-2025"
paper_url: "https://doi.org/10.5194/bg-22-4291-2025"
pdf_url: "https://bg.copernicus.org/articles/22/4291/2025/bg-22-4291-2025.pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "above-ground carbon stock"
  - "forest management"
  - "Sentinel-1"
  - "Sentinel-2"
  - "GEDI"
  - "generalized additive model"
figure: "/assets/figures/2026-09-21-assessing-the-effect-of-forest-management-on-above-ground.png"
---

## 한 줄 요약

**관리림과 비관리림의 산림 탄소량 차이를 다중센서 원격탐사로 검증한 연구**

![원문 대표 그림]({{ '/assets/figures/2026-09-21-assessing-the-effect-of-forest-management-on-above-ground.png' | relative_url }})

*원문에서 발췌 — Sofie Van Winckel 외, Biogeosciences, 2025. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

벨기에 Flanders의 Brabantse Wouden National Park에서 관리 여부만 다른 산림 패치를 짝지어 above-ground carbon stock의 차이를 평가했다. 동시에 Sentinel-2, Sentinel-1, GEDI 기반 canopy height product를 generalized additive model (GAM)의 예측변수로 써서 탄소량 추정 정확도를 비교했다. Sentinel-1과 Sentinel-2를 결합한 모델은 R2=0.73, RMSE=59.21 t ha-1, MAE=50.29 t ha-1로, Sentinel-2 지수만 쓴 모델(R2=0.56, RMSE=99.44 t ha-1, MAE=91.40 t ha-1)보다 정확도가 높았다. 현장 측정에서는 비관리림의 탄소량이 더 높게 나타났지만, 원격탐사 모델은 이 차이를 탐지하지 못했다.

## 주요 차별성

- 기후, 토양, 사면, 우점종, 관리 이력 같은 교란요인을 통제한 orthogonal design의 짝지은 patch 자료를 원격탐사 모델의 보정자료로 직접 사용했다.
- optical, SAR, spaceborne lidar 세 계열의 자료를 한 연구지에서 단계적으로 더해 가며 각 센서의 기여도를 분리해 평가했다.
- random forest 대신 해석 가능성을 유지하는 GAM을 쓰고, 응답변수에 gamma 분포를 가정해 탄소량 분포의 비대칭을 반영했다.
- 모델 정확도 향상과 산림관리 효과 탐지 가능성을 구분해, 정확도가 개선되어도 관리 효과는 탐지되지 않을 수 있음을 실증했다.

## 주요 기여점

- 온대 Atlantic forest에서 비관리림이 관리림보다 above-ground carbon stock이 유의하게 높다는 현장 근거를 제시했다.
- Sentinel-2에 Sentinel-1의 VV·VH backscatter를 더하면 탄소량 추정 정확도가 크게 개선되지만, GEDI 기반 canopy height 추가는 개선 효과가 거의 없음을 보였다.
- signal saturation, 제한된 훈련자료, 높은 mean absolute error가 관리 효과 탐지를 가로막는 요인임을 정량적으로 규명했다.
- R 코드와 자료를 공개해 다른 온대림 지역에서 재현 가능한 분석 절차를 제공했다.

## 연구의 배경

산림 탄소량 증가는 Kyoto Protocol, Paris Agreement, European Green Deal 같은 국제 합의의 핵심 수단이다. 그중 above-ground biomass는 인간 활동과 산림관리의 영향을 가장 크게 받는 탄소 pool이며, 지속가능한 산림관리의 지표로 쓰인다. 그러나 현장 측정은 정확한 대신 비용과 노동이 많이 들어 넓은 면적으로 확장하기 어렵다.

## 필요성

산림관리가 탄소량을 늘리는지 줄이는지에 대한 견해는 아직 엇갈리며, 기후·토양·사면·임분 이력 같은 교란요인 때문에 기존 연구에서 인과를 분리하기 어려웠다. 원격탐사는 넓은 면적을 저비용으로 관측하지만, optical은 구조 정보를 놓치고 SAR은 temporal decorrelation을, spaceborne lidar는 전역 피복 부재를 겪는다. 세 센서를 함께 쓴 연구는 드물고, 대부분 두 종류에 머물러 있다.

## 목적

교란요인을 통제한 관리림·비관리림 짝을 비교해 산림관리가 above-ground carbon stock에 미치는 효과를 평가한다. 또한 optical, lidar, SAR 원격탐사의 상호보완적 강점을 결합해 탄소량 추정의 정확도와 확장성을 높인다.

## 방법론

연구지는 벨기에 Flanders의 Brabantse Wouden National Park이며, 관리 여부만 다른 patch를 묶은 13개 cluster, 26개 patch, 78개 plot을 조사했다. 비관리 patch는 최소 20년간 벌채가 없었고, 현장에서 측정한 DBH와 수고를 Flemish Forest Inventory의 species-specific allometric equation에 넣어 carbon stock을 산정했다. 예측변수로는 Google Earth Engine에서 2023년 7월 1일~9월 1일 구간으로 취득한 Sentinel-2 level-2A 밴드와 16개 vegetation index, Sentinel-1 GRD Interferometric Wide Swath mode의 VV·VH backscatter, Lang et al.의 GEDI/Sentinel-2 기반 10 m canopy height product를 사용했다. recursive feature elimination으로 변수를 선별한 뒤 gamma 분포를 가정한 generalized additive model (GAM)로 탄소량을 추정했으며, 최종 모델은 MCARI, B5, STVI3, B12, GNDVI, 수종, VH, VV로 구성됐다. 전체 78개 plot 중 90%(70개)를 학습, 10%(8개)를 검정에 사용하고 leave-one-out cross-validation으로 조정했으며, 관리 여부 간 차이는 generalized linear mixed model (GLMM)로 검정했다.

## 결과

현장 측정에서 비관리 plot의 carbon stock은 196.50±61.28 t ha-1, 관리 plot은 143.68±48.90 t ha-1였고, patch 수준 차이는 유의했다(p=0.01, effect size -0.33). cluster별 차이는 10~180 t ha-1 범위였으며, 비관리 plot은 큰 직경급의 밀도가 높고 관리 plot은 최소 직경급의 개체수가 많았다. Sentinel-2만 쓴 모델은 R2=0.56, RMSE=99.44 t ha-1, MAE=91.40 t ha-1였고, Sentinel-1을 더하자 R2=0.73, RMSE=59.21 t ha-1, MAE=50.29 t ha-1로 개선됐다. GEDI/Sentinel-2 canopy height를 더한 모델은 R2=0.58로 변화가 작았고, 세 자료를 모두 넣은 모델은 R2=0.68, RMSE=56.35 t ha-1, MAE=50.07 t ha-1였다. 최종 모델의 예측 평균은 비관리 patch 165.89±26.46 t ha-1, 관리 patch 166.80±32.28 t ha-1로 유의한 차이가 없었고(p=0.61), 전체 추정 bias는 -0.83 t ha-1였다.

## 논의

C-band SAR은 잎과 잔가지에 민감해 optical이 놓치는 구조 정보를 보완하며, Sentinel-2 단독 대비 R2를 17% 높이고 RMSE를 40.23 t ha-1 낮췄다. 반면 GEDI/Sentinel-2 canopy height product는 현장 측정 대비 수고를 체계적으로 과소추정해(paired t test, p=1e-05) 추가 설명력을 주지 못했다. 관리 효과가 탐지되지 않은 원인으로는 biomass 400 t ha-1(carbon stock 200 t ha-1) 이상에서 관찰된 signal saturation, 125 t ha-1 이하 구간의 과대추정, 70개 plot에 불과한 훈련자료, 그리고 추정된 차이보다 큰 mean absolute error가 지목됐다. 비관리 기간이 20~40년으로 짧아 차이가 충분히 누적되지 않았을 가능성도 있으며, 후속 연구로는 C-band와 L-band SAR의 결합, 관리림·비관리림 분리 모델링, 탄소량 외 생태계 서비스의 trade-off 분석이 제시됐다.

## 왜 읽을 만한가

탄소흡수량 추정에서 다중센서 결합이 정확도를 얼마나 올리는지, 그리고 정확도 향상이 곧 관리 효과 탐지로 이어지지는 않는다는 한계를 수치로 보여 준다. carbon credit이나 MRV 체계 설계에서 원격탐사의 적용 한계를 가늠하려는 연구자에게 참고가 된다.

## 원문 링크

- 원문: [https://doi.org/10.5194/bg-22-4291-2025](https://doi.org/10.5194/bg-22-4291-2025)
- PDF: [https://bg.copernicus.org/articles/22/4291/2025/bg-22-4291-2025.pdf](https://bg.copernicus.org/articles/22/4291/2025/bg-22-4291-2025.pdf)
- DOI: [https://doi.org/10.5194/bg-22-4291-2025](https://doi.org/10.5194/bg-22-4291-2025)
