---
layout: post
title: "Gated Multimodal Learning for Interpretable Property Energy Performance Prediction and Retrofit Scenario Analysis"
date: 2026-08-22 08:30:00 +0900
topic: "탄소중립"
topic_key: "carbon-neutral"
one_liner: "EPC 표·텍스트·GIS를 gated fusion으로 합쳐 주택 에너지 성능을 예측한다"
authors: "Yunfei Bai, Aaron Tesfa Tsion, Raul Rosales, Barbara Shollock, Wei He"
venue: "arXiv (preprint)"
published: "2026-05-06"
doi: ""
paper_url: "https://arxiv.org/abs/2605.05088v1"
pdf_url: "https://arxiv.org/pdf/2605.05088v1"
source: "arxiv"
basis: "full_text"
keywords:
  - "multimodal learning"
  - "gated fusion"
  - "Energy Performance Certificate"
  - "SHAP"
  - "building retrofit"
  - "GIS"
paper_keywords:
  - "multimodal learning"
  - "property energy performance"
  - "gated fusion"
  - "interpretability"
  - "sustainable cities"
---

## 한 줄 요약

**EPC 표·텍스트·GIS를 gated fusion으로 합쳐 주택 에너지 성능을 예측한다**

## 초록 요약

주거 건물 decarbonisation에는 도시 규모로 확장 가능한 에너지 성능 평가가 필요하다. 이 연구는 Energy Performance Certificate(EPC)의 tabular 변수, 평가자가 작성한 free text, GIS 기반 공간 특성을 통합하는 gated multimodal model을 제안한다. 모델은 SAP(Standard Assessment Procedure) 점수와 EI(Environmental Impact) 점수를 연속값으로 동시에 예측하며, sample-wise gating이 물건별 modality 가중치를 학습한다. London Westminster 사례에서 SAP과 EI의 MAE는 각각 4.03점과 4.76점, R2는 0.757과 0.748이었고, 학습된 모델은 wall insulation·roof insulation·window glazing 개선 시나리오 분석에도 적용되었다.

## 주요 차별성

- facade 이미지 대신 EPC의 다중 필드 assessor text와 GIS 기반 footprint geometry를 modality로 사용한다.
- sample-wise gated fusion으로 물건마다 tabular·text·spatial 가중치를 다르게 학습하고, 그 가중치를 추론 시 추출해 해석에 쓴다.
- band 분류가 아니라 SAP과 EI를 연속값으로 dual-target 회귀하며, band classification을 auxiliary head로만 둔다.
- carbon 지표인 EI를 SAP과 대등한 예측 대상으로 다룬다.

## 주요 기여점

- tabular·text·spatial 증거를 결합해 연속 SAP·EI를 추정하는 해석 가능한 multimodal EPC 예측 프레임워크를 제시한다.
- Westminster에서 예측 성능, modality ablation, subgroup robustness, 수렴 거동, 다층 해석 분석을 체계적으로 수행한다.
- 학습된 모델을 wall insulation·roof insulation·window glazing 시나리오로 확장해 SAP·EI·연간 에너지 비용·eCO2 변화량을 추정한다.

## 연구의 배경

주거 건물은 UK 온실가스 배출의 약 20%, EU 에너지 관련 배출의 약 25%를 차지한다. UK에서 EPC는 주택 에너지 성능 평가의 핵심 근거이며, SAP 점수와 EI 점수로 효율과 탄소 영향을 각각 나타낸다. EPC 기록에는 건물 속성, 설비 정보, 평가자가 작성한 텍스트 설명이 함께 담긴다.

## 필요성

EPC는 자격을 갖춘 평가자의 현장 조사에 의존하고 갱신 주기가 불규칙해, 지자체 주택 재고 전체를 대상으로 한 신속한 평가와 시나리오 분석이 어렵다. 기존 data-driven 연구는 대부분 단일 소스 수치 입력이나 시뮬레이션 데이터를 쓰고, 에너지 소비량이나 rating class를 예측해 retrofit의 한계 효과를 담는 연속 지표를 다루지 못한다. multimodal 연구도 대체로 street view 같은 외부 이미지에 의존해 occlusion·갱신 주기·사생활 제약을 받으며, 예측이 어떤 modality에서 나왔는지 물건 단위로 설명하지 못한다.

## 목적

EPC tabular 속성, 다중 필드 EPC 텍스트, GIS 기반 공간 정보를 결합해 연속 SAP·EI 점수를 동시에 예측하는 해석 가능한 gated multimodal 프레임워크를 제안한다. 나아가 이 모델로 property 단위 retrofit 시나리오의 효과를 추정한다.

## 방법론

연구 지역은 면적 21.5 km2의 London Westminster이며, EPC database와 Property Location and Geometry 데이터를 UPRN-TOID 매핑으로 연결하고 Building Height Attributes를 결합해 최종 124,990개 물건을 확보했다. tabular modality는 CONSTRUCTION_AGE_BAND, BUILT_FORM, MAIN_FUEL, TOTAL_FLOOR_AREA 등 EPC 구조화 변수로, text modality는 벽·창·바닥·지붕·난방·급탕·조명 설명 필드로, spatial modality는 OS MasterMap 기반 footprint boundary와 footprint area·height·orientation으로 구성했다. 건물 footprint는 equal arc-length sampling으로 길이 128의 경계 좌표 시퀀스로 바꾸고 평행이동·스케일 정규화를 거쳤으며, 주축 방향은 경계점 covariance matrix의 최대 고유벡터로 구했다. 인코더는 categorical embedding과 MLP(tabular), DistilBERT와 mask-aware mean pooling(text), Conv1D 기반 경계 시퀀스 인코더와 MLP(spatial)로 모두 128차원 latent space에 정렬했고, softmax gate가 sample별 modality 가중치를 산출해 fused embedding을 만든다. 손실은 SAP·EI 회귀의 Huber loss에 7개 band에 대한 cross-entropy를 가중 결합했고, property type과 SAP·EI band로 joint stratification한 뒤 70%/15%/15%로 분할해 Adam optimiser와 layer-wise learning rate로 학습했다.

## 결과

학습은 early stopping으로 38 epoch에서 종료되었고, test set에서 SAP은 MAE 4.033·RMSE 5.739·R2 0.757, EI는 MAE 4.756·RMSE 6.711·R2 0.748을 기록해 mean MAE는 4.394였다. modality ablation에서 full multimodal 모델이 두 번째로 좋은 Tabular+Text 대비 R2를 SAP 2.4%, EI 2.9% 높였고 band accuracy도 각각 2.2%, 1.9% 높였다. 해석 분석에서 gated fusion 가중치는 text modality에 가장 크게 의존했고, SHAP는 main fuel·built form·construction age band를 상위 tabular 변수로 지목했으며, text occlusion은 roof description과 wall description을, spatial permutation은 height와 footprint area를 상위로 꼽았다. subgroup 분석에서는 Flat의 성능이 가장 좋고 House가 가장 낮았으며, 2003~2006년 건축 물건의 R2는 약 0.5로 떨어졌으나 band accuracy는 0.7 이상을 유지했다. retrofit 시나리오에서 wall insulation 대상 100,701호(80.5%)는 SAP 평균 4.64점, roof insulation 대상 22,082호(17.7%)는 12.01점, glazing 대상 48,788호(39.0%)는 3.07점 개선이 예측되었고, 물건당 연간 절감은 roof insulation이 £497.18과 1,572.78 kg eCO2로 가장 컸다.

## 논의

결과는 EPC 텍스트와 GIS geometry가 현장 재조사 없이도 property 단위 에너지 성능 근거를 만들 수 있음을 보여주며, gating 가중치와 field-level 중요도가 지자체의 retrofit 우선순위 결정에 감사 가능한 설명을 제공한다. 총량 기준으로는 대상 호수가 많은 wall insulation의 절감이 가장 크지만 물건당 효과는 roof insulation이 가장 커, 조치 순서 설계에 서로 다른 기준이 필요하다. 한계로는 Westminster 한 곳에 국한된 사례라 교외·농촌이나 사회경제적으로 다른 지역으로의 전이 가능성이 검증되지 않았고, XGBoost나 LightGBM 같은 강한 non-neural tabular baseline과의 비교가 빠져 있으며, boundary-sequence encoder의 기여가 크지 않아 계산 비용 대비 효용을 더 따져야 한다는 점을 저자들이 밝힌다. 또한 retrofit 분석은 물리 시뮬레이션이나 인과 추정이 아닌 모델 기반 시나리오 투영이므로, 후속 연구로 engineering simulation 결합과 불확실성 분석, SAP 후속 체계인 Home Energy Model로의 적응이 제시된다.

## 왜 읽을 만한가

행정 텍스트와 GIS geometry를 modality로 묶고 sample별 gating 가중치로 설명까지 뽑아내는 구성은, 공공 데이터 기반 탄소중립 분석에 그대로 응용할 수 있는 설계다. 예측 모델을 시나리오 분석과 비용·배출 환산까지 연결한 흐름도 정책 연계 연구에 참고가 된다.

## 원문 키워드

`multimodal learning`, `property energy performance`, `gated fusion`, `interpretability`, `sustainable cities`

## 원문 링크

- 원문: [https://arxiv.org/abs/2605.05088v1](https://arxiv.org/abs/2605.05088v1)
- PDF: [https://arxiv.org/pdf/2605.05088v1](https://arxiv.org/pdf/2605.05088v1)
