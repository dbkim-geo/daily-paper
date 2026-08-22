---
layout: post
title: "Uncovering the Associations between Human Big Five Personality Traits and Built Environment Characteristics from Street View Imagery"
date: 2026-08-23 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "Street view imagery로 본 근린 건조환경과 Big Five 성격의 연관"
authors: "Koichi Ito, Yuhao Kang, Samuel D. Gosling, Xihan Yao, Jeff Potter, Filip Biljecki"
venue: "Annals of the American Association of Geographers"
published: "2026-08-21"
doi: "https://doi.org/10.1080/24694452.2026.2704575"
paper_url: "https://doi.org/10.1080/24694452.2026.2704575"
pdf_url: "https://arxiv.org/pdf/2608.07489"
source: "openalex"
basis: "full_text"
keywords:
  - "street view imagery"
  - "built environment"
  - "Big Five personality traits"
  - "spatial lag model"
  - "semantic segmentation"
  - "geographic psychology"
paper_keywords:
  - "Geographic psychology"
  - "Built environment"
  - "Personality traits"
  - "Street view imagery"
---

## 한 줄 요약

**Street view imagery로 본 근린 건조환경과 Big Five 성격의 연관**

## 초록 요약

이 연구는 미국 텍사스 4개 도시에서 주민의 Big Five 성격 특성과 street view imagery(SVI)로 추출한 건조환경 특성의 연관을 분석한다. 자기보고 성격 자료를 ZIP code 단위로 집계하고 computer vision으로 도시 경관을 정량화해 결합했다. Moran's I 검정에서 다섯 특성 모두 유의한 spatial clustering을 보였다. 회귀분석에서는 건조환경과 사회경제적 변수가 성격 분포 분산의 상당 부분을 설명했고, Openness의 모형 적합도가 R2 = 0.47로 가장 높았다.

## 주요 차별성

- 성격과 장소의 관계를 국가·주·county가 아니라 ZCTA(근린) 단위에서 분석한다.
- 기후·지형 같은 macroscale 변수 대신 SVI에서 뽑은 미시적 건조환경 요소를 설명변수로 쓴다.
- 대규모 Big Five 자료와 semantic segmentation·object detection 결과를 결합한 첫 시도라고 저자들이 밝힌다.
- OLS와 Spatial Lag Model(SLM)을 함께 추정해 공간의존성을 반영한 계수 변화를 비교한다.

## 주요 기여점

- Austin, Dallas, Houston, San Antonio 4개 도시의 성격 특성 공간분포와 spatial autocorrelation을 실증한다.
- SVI 기반 변수를 8개 grouped built environment 범주로 묶어 특성별 연관 패턴을 정리한다.
- Openness는 인구 연령구성, Conscientiousness는 건조환경, Agreeableness는 사회경제 요인이 주도한다는 특성별 차이를 제시한다.
- geographic psychology와 GeoAI를 연결하는 분석 파이프라인과 ecological fallacy 관련 윤리적 고려사항을 함께 제시한다.

## 연구의 배경

지리학은 장소가 인간의 지각, 행동, 건강, 웰빙에 영향을 준다고 오래 다뤄 왔다. 그러나 인간 쪽 변수는 주로 행동 결과나 지각 평가로 다뤄졌고, 성격 같은 근본적 심리 특성은 상대적으로 덜 연구됐다. 심리학에서는 Big Five 성격 특성이 국가·주·county 수준에서 지역차를 보인다는 결과가 축적돼 있다.

## 필요성

기존 성격-장소 연구는 행정경계 단위와 기후·경제 같은 거시 변수에 머물러, 주민이 실제로 체험하는 근린·가로 수준의 물리적 요소를 놓쳤다. 환경 특성을 대규모로 정량화하기 어렵다는 방법론적 제약이 이런 공백을 만들었다. SVI와 computer vision의 발전은 이 제약을 풀 수 있는 수단을 제공한다.

## 목적

텍사스 4개 도시를 대상으로 Big Five 성격 특성의 지리적 패턴을 파악하고, 성격 특성과 SVI에서 도출한 구체적 건조환경 요소 사이의 연관을 규명하는 것이 목적이다.

## 방법론

연구 지역은 텍사스의 Austin, Dallas, Houston, San Antonio 4개 도시다. 성격 자료는 Gosling-Potter Internet Project의 BFI·BFI-2 응답으로, 2010~2020년 수집된 150,406명분을 340개 ZIP code(ZCTA) 단위로 평균 집계했고, 참여자 20명 미만이거나 100 m 격자 SVI 커버리지가 0.03% 미만인 지역은 제외했다. 건조환경은 100 m 격자로 수집한 약 500만 장의 Google Street View 이미지를 ZenSVI 패키지로 처리해, Mapillary Vistas로 사전학습된 Mask2Former의 semantic segmentation과 GroundingDINO의 object detection으로 정량화했다. 추출된 변수는 Greenery, Open Space, Building, Road, Active Mobility Infrastructure, Active Mobility Presence, Vehicle Presence, Physical Boundaries의 8개 범주로 묶고 Symbolic US Flag, CCTV Surveillance, Visual Complexity를 개별 변수로 유지했으며, ACS 2020 5-Year Estimates의 인구·사회경제 변수 8개와 도시 fixed effects를 통제변수로 넣었다. 분석은 Moran's I 검정 후 최종 255개 ZCTA를 대상으로 OLS와 Queen contiguity 가중치 기반 Spatial Lag Model을 추정했고, Z-score 표준화, Box-Cox 변환, VIF 10 미만 기준의 반복적 변수 제거를 적용했다.

## 결과

Moran's I 검정에서 다섯 특성 모두 유의한 공간적 군집을 보였고 Agreeableness가 I = 0.3127로 가장 강했으며 Openness 0.1890, Conscientiousness 0.1772, Neuroticism 0.1362, Extraversion 0.1212가 뒤를 이었다. OLS 모형 적합도는 Openness가 R2 = 0.467로 가장 높았고 Agreeableness 0.353, Conscientiousness 0.211, Extraversion 0.180, Neuroticism 0.157 순이었다. 다만 Openness의 설명력은 건조환경이 아니라 연령구성이 주도했고, 15~29세 비율의 표준화 계수가 β = 0.775 (p < 0.001)로 가장 컸으며 어떤 건조환경 범주도 통상적 유의수준에 이르지 못했다. Conscientiousness는 건조환경과의 연관이 가장 광범위해 open space(β = -0.544, p < 0.01), greenery(β = -0.532, p < 0.01), physical boundaries(β = -0.297, p < 0.05) 등 8개 범주 중 5개가 모두 음의 방향으로 유의했다. Agreeableness는 median income(β = 0.379, p < 0.01)과 racial diversity(β = 0.223, p < 0.01)가, Neuroticism은 population density(β = 0.280, p < 0.01)가 주요 예측변수였고, Spatial Lag Model에서는 다섯 특성 모두 pseudo R2가 상승해 Agreeableness가 0.404, Conscientiousness가 0.252로 개선폭이 컸다.

## 논의

저자들은 이 관계가 상관관계이며, selective migration과 environmental influence가 동시에 작동하는 양방향 피드백일 수 있다고 해석한다. 개발 이력이나 사회환경 같은 제3의 변수가 성격 분포와 건조환경을 동시에 좌우할 가능성도 명시한다. 한계로는 횡단면 설계라 인과 추론이 불가능하다는 점, 유사한 텍사스 대도시 4곳만 다뤄 압축적·대중교통 중심 도시나 농촌·타 문화권으로 일반화하기 어렵다는 점, ZCTA 집계와 시각 자료에 국한돼 소리·냄새 등 다른 감각 경험을 담지 못한 점을 든다. 후속 연구로는 성격과 환경 변화를 함께 추적하는 종단 연구, 납 배출 감축 같은 natural experiment 활용, 블록·가로 단위의 미세 분석, 장기 거주자와 신규 전입자 비교를 제안하며, 집계 결과를 개인에게 적용하는 ecological fallacy를 경계할 것을 강조한다.

## 왜 읽을 만한가

SVI와 computer vision으로 건조환경을 정량화해 심리 변수와 연결하는 GeoAI 분석 설계를 구체적으로 보여준다. semantic segmentation 결과를 이론 기반 범주로 묶고 공간회귀로 검증하는 절차는 도시계획·환경계획 연구에 그대로 옮겨 쓸 만하다.

## 원문 키워드

`Geographic psychology`, `Built environment`, `Personality traits`, `Street view imagery`

## 원문 링크

- 원문: [https://doi.org/10.1080/24694452.2026.2704575](https://doi.org/10.1080/24694452.2026.2704575)
- PDF: [https://arxiv.org/pdf/2608.07489](https://arxiv.org/pdf/2608.07489)
- DOI: [https://doi.org/10.1080/24694452.2026.2704575](https://doi.org/10.1080/24694452.2026.2704575)
