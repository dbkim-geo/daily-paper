---
layout: post
title: "Local data matters: Improving biodiversity risk and impact assessment through a data quality focus"
date: 2026-08-24 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "local data 없이 외삽한 biodiversity 평가는 신뢰하기 어렵다"
authors: "R Goodsell, Emma Granqvist, Christophe Christiaen, Fredrik Ronquist"
venue: "Journal of Environmental Management"
published: "2026-08-20"
doi: "https://doi.org/10.1016/j.jenvman.2026.130651"
paper_url: "https://doi.org/10.1016/j.jenvman.2026.130651"
pdf_url: "https://www.sciencedirect.com/science/article/pii/S0301479726021110/pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "Essential Biodiversity Variables"
  - "eDNA metabarcoding"
  - "Earth observation"
  - "XGBoost"
  - "biodiversity impact assessment"
  - "leave-one-site-out cross-validation"
paper_keywords:
  - "Biodiversity impact assessment and reporting"
  - "eDNA"
  - "Earth observation"
  - "Machine learning"
  - "Sustainable finance"
  - "Essential biodiversity variables"
figure: "/assets/figures/2026-08-24-local-data-matters-improving-biodiversity-risk-and-impact.png"
---

## 한 줄 요약

**local data 없이 외삽한 biodiversity 평가는 신뢰하기 어렵다**

![원문 대표 그림]({{ '/assets/figures/2026-08-24-local-data-matters-improving-biodiversity-risk-and-impact.png' | relative_url }})

*원문에서 발췌 — R Goodsell 외, Journal of Environmental Management, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

기업과 금융기관은 biodiversity 영향 평가 압박을 받지만 현장 데이터 수집 비용이 크다. 그래서 global dataset과 proxy를 site 단위로 외삽하는 방식이 지배적이다. 저자들은 스웨덴과 마다가스카르의 eDNA 조사 자료와 고해상도 Earth observation(EO) 시계열을 결합해 machine learning으로 5개 essential biodiversity variable(EBV)을 예측하고 cross-validation으로 정확도를 검증했다. 기존 관측 지점 안에서는 비교적 정확했으나 새로운 지점에서는 성능이 크게 떨어졌고, 저자들은 이를 보완할 biodiversity data hierarchy framework를 제안한다.

## 주요 차별성

- 대규모 eDNA metabarcoding 자료와 고해상도 EO 자료를 결합해 EBV 예측의 신뢰도를 직접 검증했다.
- 기후와 생물상이 크게 다른 스웨덴과 마다가스카르를 함께 다뤄 예측 성능의 지역 의존성을 비교했다.
- leave-one-site-out cross-validation으로 local data가 전혀 없는 신규 site라는 실제 사용 상황을 재현했다.
- 예측 오차뿐 아니라 site ranking의 priority tier 변화까지 평가해 의사결정 관점의 유용성을 따졌다.

## 주요 기여점

- TNFD 정렬 보고서 84건을 분석해 기업과 금융기관의 global dataset 의존 실태를 정량화했다.
- 5개 EBV에 대해 site 내부 예측과 신규 site 예측의 mean absolute error(MAE) 차이를 수치로 제시했다.
- 온실가스 회계의 data quality score를 본뜬 biodiversity data hierarchy framework 초안을 제안했다.
- 분석에 쓴 데이터와 코드를 GitHub 저장소 ronquistlab/finbio-ebv로 공개했다.

## 연구의 배경

자연 훼손이 금융 리스크로 인식되면서 sustainable finance 분야가 빠르게 커지고 있다. 기업과 금융기관은 TNFD 같은 이니셔티브에 맞춰 자사가 영향을 주는 지역의 biodiversity 상태를 보고해야 한다. 그러나 현장 조사 비용 때문에 대부분 무료로 쓸 수 있는 global dataset과 tool에 의존한다.

## 필요성

global tool은 실제 생물 관측이 아니라 pressure나 proxy에 기반하거나, 소수 분류군만 다루는 경우가 많다. eDNA와 Copernicus 같은 EO 데이터가 늘면서 통계 모델로 미관측 지점의 biodiversity를 추정하는 방식이 대안으로 제시되지만, 정작 그 지점에 원자료가 없어 검증이 어렵다. 검증되지 않은 예측값이 투자와 보전 우선순위 결정에 쓰이면 잘못된 판단으로 이어질 수 있다.

## 목적

고품질 biodiversity 자료와 고해상도 환경 자료를 써도 EBV를 새로운 site로 외삽할 때 신뢰할 만한 결과가 나오는지 검증하는 것이 목적이다. 아울러 평가의 데이터 품질을 단계적으로 개선할 수 있는 framework를 제시하고자 한다.

## 방법론

먼저 TNFD 웹사이트에 공개된 보고서 84건(기업 57건, 금융기관 27건)을 NotebookLM으로 정성 분석해 현재 쓰이는 데이터셋과 tool을 목록화하고 수작업으로 검증했다. biodiversity 자료로는 Insect Biome Atlas의 Malaise trap metabarcoding 조사를 썼으며, 스웨덴 198개 지점과 마다가스카르 50개 지점에서 각각 4,500개와 2,000개가 넘는 샘플을 얻었다. 이 자료에서 species richness, local contribution to beta diversity(LCBD), functional dispersion, functional evenness, genetic diversity 등 GEO BON 체계의 5개 EBV를 산출했다. 환경 변수는 ERA5 기후 자료(0.1° 격자, 약 9 km)와 Copernicus 100 m land cover, 그리고 photoperiod와 harmonic 계절항으로 구성했고, 예측 모델은 XGBoost의 gradient boosted regression tree를 grid search로 튜닝해 적합했다. 검증은 각 site에서 관측치 20%를 빼는 stratified test-train split과 site 하나씩 통째로 빼는 leave-one-site-out cross-validation 두 가지로 수행하고 MAE로 정확도를 평가했다.

## 결과

보고서 분석에서는 금융기관의 93%, 기업의 67%가 ENCORE 같은 global screening tool을 썼고, 국가·지역·내부 데이터를 언급한 금융기관은 26%에 그쳤다. 신규 site 예측에서는 모든 EBV의 MAE가 커졌고, species richness는 스웨덴에서 62%, 마다가스카르에서 68% 증가했다. genetic diversity는 각각 25%와 20%, functional evenness는 48%와 36%, functional dispersion은 19%와 32% 늘었으며, LCBD는 스웨덴 18%, 마다가스카르 1%로 나라별 차이가 컸다. site ranking에서도 species richness는 site 내부 예측 시 두 나라 모두 78%가 원래 quantile을 유지했으나, 신규 site 예측에서는 스웨덴 35%, 마다가스카르 44%로 떨어졌다. 신규 site 예측에서 스웨덴은 25%, 마다가스카르는 15%의 지점이 priority tier를 두 단계 이상 벗어났다.

## 논의

고품질 자료를 써도 local data가 없는 site에서는 예측 오차와 순위 변동이 커지므로, global dataset 외삽만으로 site 단위 의사결정을 내리면 우선순위가 뒤바뀔 수 있다. 저자들은 GBIF 전체 occurrence record 중 기업이 보고한 비율이 0.3%에 불과하다는 점을 들어 기업 스스로의 현장 데이터 수집이 필요하다고 본다. 대안으로 온실가스 회계의 data hierarchy와 data quality score를 본떠 직접 관측, site 내부 예측, 신규 site 예측, proxy를 구분하는 biodiversity data hierarchy를 제안하고 단계적 개선을 추적하도록 했다. 다만 분석은 스웨덴과 마다가스카르의 무척추동물 metabarcoding 자료에 한정되며, 보고서 분석도 기업이 공개한 방법론 수준에 의존한다는 한계가 있다.

## 왜 읽을 만한가

환경계획과 GeoAI에서 흔히 쓰는 전역 모델 외삽이 신규 지점에서 어디까지 믿을 만한지 정량적으로 보여준다. 예측 오차를 순위 변화로 환산해 의사결정 영향까지 평가한 방식은 다른 공간 예측 연구에도 그대로 적용할 수 있다.

## 원문 키워드

`Biodiversity impact assessment and reporting`, `eDNA`, `Earth observation`, `Machine learning`, `Sustainable finance`, `Essential biodiversity variables`

## 원문 링크

- 원문: [https://doi.org/10.1016/j.jenvman.2026.130651](https://doi.org/10.1016/j.jenvman.2026.130651)
- PDF: [https://www.sciencedirect.com/science/article/pii/S0301479726021110/pdf](https://www.sciencedirect.com/science/article/pii/S0301479726021110/pdf)
- DOI: [https://doi.org/10.1016/j.jenvman.2026.130651](https://doi.org/10.1016/j.jenvman.2026.130651)
