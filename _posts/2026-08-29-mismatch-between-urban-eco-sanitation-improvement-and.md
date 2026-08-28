---
layout: post
title: "Mismatch between urban eco-sanitation improvement and health service supply capacity: evidence from Chinese city panel data and interpretable machine learning"
date: 2026-08-29 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "중국 도시의 eco-sanitation 개선은 보건서비스 공급역량으로 전환되지 않는다"
authors: "Zhen Peng, Lin Wang"
venue: "BMC Health Services Research"
published: "2026-08-25"
doi: "https://doi.org/10.1186/s12913-026-15444-8"
paper_url: "https://doi.org/10.1186/s12913-026-15444-8"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "health service supply capacity"
  - "eco-sanitation environment"
  - "two-way fixed effects"
  - "interpretable machine learning"
  - "SHAP"
  - "urban green infrastructure"
paper_keywords:
  - "health service supply capacity"
  - "healthcare resource allocation"
  - "urban eco-sanitation environment"
  - "health service governance"
  - "Chinese cities"
  - "interpretable machine learning"
figure: "/assets/figures/2026-08-29-mismatch-between-urban-eco-sanitation-improvement-and.png"
---

## 한 줄 요약

**중국 도시의 eco-sanitation 개선은 보건서비스 공급역량으로 전환되지 않는다**

![원문 대표 그림]({{ '/assets/figures/2026-08-29-mismatch-between-urban-eco-sanitation-improvement-and.png' | relative_url }})

*원문에서 발췌 — Zhen Peng 외, BMC Health Services Research, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

중국 prefecture-level 이상 도시 2002-2024년 panel data로 eco-sanitation environment index(ESE)와 health service supply capacity index(HSC)의 전환 관계를 분석한 연구다. two-way fixed effects model, 차원별 분해, mechanism test, moderation analysis, robustness check, interpretable machine learning을 결합했다. ESE, green infrastructure, municipal sanitation facilities는 지속적으로 개선됐지만 HSC 증가는 느렸고, baseline model은 안정적인 양(+)의 전환을 지지하지 않았다. 저자들은 eco-sanitation 개선이 보건서비스 공급역량 강화의 충분조건이 아니며 시간적·공간적·제도적 mismatch가 존재한다고 결론짓는다.

## 주요 차별성

- 환경 개선이 건강 결과(mortality, disease burden)에 미치는 영향이 아니라, 환경 개선이 보건서비스 '공급역량'으로 전환되는지를 질문 대상으로 삼는다
- eco-sanitation environment를 green infrastructure index(GII), municipal sanitation facility index(MSI), pollution pressure index(PPI)로 분해해 차원별로 상반된 부호를 확인한다
- panel econometric model로 평균 관계를 식별하고 interpretable machine learning으로 변수 중요도·비선형 경계를 보완하는 역할 분담을 명시한다
- 양(+)의 전환을 전제하지 않고 mismatch 자체를 식별 대상으로 설정한다

## 주요 기여점

- 2002-2024년 289개 도시, 6,647개 city-year 관측치의 장기 city panel dataset을 구축하고 entropy weighting method로 HSC·ESE·GII·MSI·PPI 지수를 산출한다
- urban construction investment를 매개로 한 eco-sanitation → 보건서비스 공급역량 전달 경로가 현 데이터에서 성립하지 않음을 mechanism test로 보인다
- 지역, Hu Huanyong line, 도시 규모, 경제발전 수준, 재정역량별 이질성과 비선형 경계를 제시해 도시 유형별 차별화된 정책 방향을 도출한다
- healthy city 정책이 eco-sanitation governance, 인프라 투자, 의료인력 배치, 재정을 하나의 governance framework로 통합해야 함을 실증 근거로 제시한다

## 연구의 배경

도시화는 인구, 자원, 환경위험, 공공서비스의 분포를 재편한다. 기존 environmental health 연구는 주로 환경노출과 사망률·질병부담 같은 건강 결과의 관계를 다뤘다. 반면 green space, 상하수도, 폐기물 처리 같은 도시 eco-sanitation 개선이 보건서비스 공급역량과 의료자원 배분으로 이어지는지는 health services research 관점에서 거의 다뤄지지 않았다.

## 필요성

green infrastructure, 상수도·가스 공급, 하수처리, 폐기물 관리, 오염압력은 각각 따로 연구돼 왔고 이를 보건서비스 공급역량과 연결하는 통합 분석틀이 없다. 중국 도시를 대상으로 eco-sanitation 개선이 공급역량으로 전환되는지, 그리고 그 전환이 에너지·탄소 조건, 재정, 의료자원 배분, 도시 이질성에 의해 어떻게 제약되는지를 동시에 검토한 연구도 드물다. 환경 개선이 자동으로 보건서비스 역량으로 이어진다는 전제를 검증할 필요가 있다.

## 목적

중국 도시 panel data로 eco-sanitation 개선이 health service supply capacity로 안정적으로 전환되는지 검증하고, 전환이 막히는 mismatch 메커니즘과 경계조건을 식별하는 것이 목적이다.

## 방법론

연구 지역은 중국 prefecture-level 이상 도시이며, 주 표본은 2002-2024년 289개 도시 6,647개 city-year 관측치이고 이 중 5,070개가 baseline model에 사용된다. 종속변수는 인구 1만 명당 병상 수, 면허의사 수, 병원·보건소 수로 구성한 health service supply capacity index(HSC)이고, 핵심 설명변수는 1년 시차 eco-sanitation environment index(ESE_i,t-1)로 park green area per capita, 녹지율, 상수도·가스 보급률, 하수처리율, 생활폐기물 무해화 처리율 등 8개 지표로 구성한다. 모든 합성지수는 min-max normalization 후 entropy weighting method로 가중한다. 추정은 city·year two-way fixed effects model에 city-level clustered standard error를 사용하고, GII·MSI·PPI 차원별 모형, urban construction investment 경로의 mechanism test, PPI·energy intensity·CEADs 도시 부문별 CO₂ 배출과의 moderation model, 지역·Hu Huanyong line·도시 규모·재정역량별 heterogeneity 분석, placebo test를 포함한 robustness check를 수행한다. 보조 분석으로 2018년 이전을 훈련, 2019년 이후를 검증으로 나눈 시계열 분할에서 random forest와 gradient boosting을 학습하고 SHAP으로 변수 기여도와 비선형 관계를 해석한다.

## 결과

기술통계에서 HSC 평균은 0.2201, ESE 평균은 0.6419로 eco-sanitation 인프라가 의료자원 배분보다 빠르게 개선됐다. baseline model에서 ESE 0.1 단위 증가의 계수는 통제변수 없이 -0.0069(1% 유의), 기본 통제 추가 시 -0.0057, 확장 통제 추가 시 -0.0053으로 모두 음(-)이며, fixed-asset investment를 넣어 표본이 3,919개로 줄면 유의성이 사라진다. 차원별 분석에서 GII 계수는 유의한 음, MSI는 비유의, PPI는 유의한 양으로 나타났고 저자들은 PPI의 양의 계수를 오염의 건강 편익이 아니라 수요유발형 자원배분 반응으로 해석한다. mechanism test에서 ESE는 조경투자와 약한 양의 관계, 하수처리 투자와 유의한 음의 관계를 보였고 투자·지출 변수의 HSC에 대한 직접효과는 유의하지 않아 전달 경로가 지지되지 않았다. 강건성 검증에서 equal-weighted index 계수는 -0.0050(1% 유의), PCA index는 -0.0035(5% 유의)였고, machine learning에서는 random forest가 test set R² 0.5936, RMSE 0.0763, MAE 0.0589로 gradient boosting(R² 0.5637)보다 우수했으며 SHAP 중요도는 per capita GDP, 인구 규모, 3차산업 비중, 대출잔액/GDP가 상위였다.

## 논의

저자들은 eco-sanitation 시스템과 보건서비스 시스템 사이에 시간적(인프라 건설과 의료인력·병상 확충의 주기 차이), 공간적(개선이 빠른 도시와 의료자원 집중 도시의 불일치), 제도적(도시건설·환경 부처와 보건·재정·인사 부처의 분절) mismatch가 존재한다고 본다. 이질성 결과는 이 관계가 동부·중부, 고소득, 대규모 인구, Hu Huanyong line 남동측 도시에서만 유의하게 나타나 도시 발전단계와 자원배분 조건에 의존함을 보여준다. 한계로는 HSC가 자원 개수 기반 공급측 proxy여서 의료의 질, 실제 이용, 접근성을 대표하지 못한다는 점, 도시 단위 자료라 근린·집단별 접근성 차이를 포착하지 못한다는 점, CEADs 자료의 연도 불일치, 준자연실험 설계가 아니라는 점, 일관된 spatial weights matrix 부재로 Moran's I·SAR·SEM 같은 공간패널 검정을 수행하지 못해 도시 간 spatial spillover가 미처리 편의로 남는다는 점을 든다. 후속 연구로 주민 건강조사, 의료보험 청구자료, 의료기관 geocoding, remote sensing 기반 green-space exposure, 공간가중행렬, quasi-natural experiment의 결합을 제안한다.

## 왜 읽을 만한가

환경·인프라 지표를 entropy weighting으로 합성하고 fixed effects model과 SHAP 기반 해석을 역할 분담시킨 구성은 도시계획·탄소중립 분야의 도시 panel 분석에 바로 참고할 만하다. 환경 개선이 공공서비스 역량으로 자동 전환된다는 전제를 실증적으로 반박하는 사례로도 읽힌다.

## 원문 키워드

`health service supply capacity`, `healthcare resource allocation`, `urban eco-sanitation environment`, `health service governance`, `Chinese cities`, `interpretable machine learning`

## 원문 링크

- 원문: [https://doi.org/10.1186/s12913-026-15444-8](https://doi.org/10.1186/s12913-026-15444-8)
- DOI: [https://doi.org/10.1186/s12913-026-15444-8](https://doi.org/10.1186/s12913-026-15444-8)
