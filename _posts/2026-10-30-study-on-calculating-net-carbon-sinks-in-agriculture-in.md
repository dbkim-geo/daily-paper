---
layout: post
title: "STUDY ON CALCULATING NET CARBON SINKS IN AGRICULTURE IN SOUTHWEST CHINA: SPATIOTEMPORAL PATTERNS, DRIVING FACTORS, AND MULTI-SCENARIO PROJECTIONS"
date: 2026-10-30 08:30:00 +0900
topic: "탄소저감"
topic_key: "carbon-reduction"
one_liner: "IPCC 계수·STIRPAT·LSTM으로 중국 서남부 농업 net carbon sink를 산정·전망한다."
authors: "F. HU, Z.L. GAN, X.Q. ZHONG, C.R. HU"
venue: "Applied Ecology and Environmental Research"
published: "2026-01-01"
doi: "https://doi.org/10.15666/aeer/2402_28372860"
paper_url: "https://doi.org/10.15666/aeer/2402_28372860"
pdf_url: "https://doi.org/10.15666/aeer/2402_28372860"
source: "openalex"
basis: "full_text"
keywords:
  - "agricultural net carbon sink"
  - "STIRPAT model"
  - "ridge regression"
  - "LSTM"
  - "scenario analysis"
  - "Southwest China"
paper_keywords:
  - "Southwest China"
  - "agricultural net carbon sink"
  - "spatial-temporal dynamics"
  - "STIRPAT model"
  - "scenario analysis"
---

## 한 줄 요약

**IPCC 계수·STIRPAT·LSTM으로 중국 서남부 농업 net carbon sink를 산정·전망한다.**

## 초록 요약

중국 서남부 5개 성·직할시의 2003–2023년 농업 net carbon sink를 IPCC 배출계수와 작물 탄소흡수계수로 산정했다. STIRPAT 모형의 ridge regression으로 동인을 분석하고 LSTM으로 2035년까지 8개 시나리오를 전망했다. 순탄소흡수량은 2,284.33만 t에서 4,753.81만 t으로 108.11% 증가했고 지역 순위는 Sichuan > Yunnan > Guizhou > Chongqing > Tibet였다. Comprehensive Optimization 시나리오에서 2035년 순탄소흡수량은 6,630.11만 t으로 전망됐다.

## 주요 차별성

- 농업 탄소배출(농자재 투입·벼 재배·축산)과 작물 탄소흡수를 함께 산정해 net carbon sink 단위로 분석했다.
- 탄소 산정, STIRPAT 동인 분석, LSTM 다중 시나리오 전망을 하나의 분석 틀로 결합했다.
- 선행연구가 적은 생태 취약 산악지역인 중국 서남부를 21년 장기 패널로 다뤘다.
- 14차 5개년 계획 목표치를 근거로 7개 동인의 증가율을 설정해 8개 정책 시나리오를 구성했다.

## 주요 기여점

- 서남부 농업 배출원의 3분의 2 이상이 축산이라는 지역 특유의 배출 구조를 정량화했다.
- farmland area가 가장 강한 양(+)의 동인이고 농촌 노동력이 음(−)의 동인임을 탄력성 계수로 제시했다.
- 단일 정책 중 Crop Structure Optimization과 Agricultural Scale Expansion이 가장 효과적이고 Rapid Urbanization이 억제 효과를 낸다는 전망을 제시했다.
- Sichuan·Yunnan(공고화), Chongqing(시범), Tibet(축산 구조 조정)으로 차별화된 지역 정책을 제안했다.

## 연구의 배경

농업·임업·토지이용 부문은 전 세계 온실가스 배출의 22%를 차지한다. 농업은 배출원이면서 작물 생장을 통한 carbon sequestration 기능도 갖는다. 중국 서남부는 국토의 약 24%를 차지하는 최대 탄소흡수 지역이자 생태 방벽이지만 산악 지형과 낮은 시장화 수준으로 저탄소 전환이 어렵다.

## 필요성

기존 연구는 전국 단위나 화동·화남·동북 등 농업 선진지역에 집중되어 서남부 연구가 부족하다. 자료 기간이 짧고 배출 또는 흡수 한쪽만 다루는 경우가 많다. 동인 분석과 추세 예측을 결합한 net carbon sink 연구도 드물다.

## 목적

2003–2023년 중국 서남부 농업 net carbon sink의 시공간 변화와 동인을 규명한다. 2035년까지 다중 시나리오 전망으로 정책 경로별 탄소흡수 잠재력을 평가한다.

## 방법론

대상은 Chongqing, Sichuan, Guizhou, Yunnan, Tibet(약 234.06만 km²)이며 China Statistical Yearbook과 성별 통계연감 2003–2023년 자료를 쓰고 결측은 선형보간했다. 배출은 비료·농약·농업용 필름·경유·경운·관개, 벼 재배 CH₄, 축산 enteric fermentation 및 분뇨 CH₄·N₂O를 emission factor 방식으로 산정했고 IPCC AR6 GWP를 적용했다. 흡수는 13개 작물의 수확량·경제계수·함수율·탄소흡수율로 산정했고 순탄소흡수량은 흡수량에서 배출량을 뺐다. 동인 분석은 7개 변수의 STIRPAT 모형을 쓰고 VIF > 10의 다중공선성 때문에 K=0.3의 ridge regression을 적용했다. 2003–2023년 자료로 LSTM을 학습하고 7개 동인에 저·중·고 증가율을 부여한 8개 시나리오로 2024–2035년을 전망했다.

## 결과

총배출은 2003년 5,130.09만 t에서 2019년 4,143.68만 t으로 줄었다가 2023년 4,412.93만 t으로 6.50% 반등했고, 흡수는 7,414.41만 t에서 9,166.74만 t으로 23.63% 증가했다. 축산 배출은 3,824.01만 t에서 2,999.70만 t으로 줄었으나 여전히 총배출의 3분의 2 이상을 차지했다. Sichuan의 순탄소흡수량은 1,341.46만 t에서 2,457.29만 t으로 늘어 지역 합계의 약 절반을 차지했고, Chongqing은 71.82만 t에서 683.84만 t으로 850% 이상 증가했으며, Tibet은 −352.49만 t에서 −431.74만 t으로 순배출이 지속됐다. 탄력성 계수는 farmland area 0.952, 농촌 노동력 −0.525, 도시화율 0.134, 농촌 1인당 가처분소득 0.048, 농업경제 발전 0.041, R&D 투자 0.032, 농업 과학기술 성과 0.029였고 모두 p < 0.01이었다. 2035년 전망치는 Baseline 6,517.41만 t, Crop Structure Optimization 6,658.76만 t, Agricultural Scale Expansion 6,659.71만 t, Comprehensive Optimization 6,630.11만 t, Rapid Urbanization 6,350.98만 t이었다.

## 논의

저자들은 경지 보호와 작물 구조 최적화를 함께 추진하는 정책 조합이 단일 정책보다 효과적이라고 해석한다. 다만 본문 Table 8의 2035년 값은 Crop Structure Optimization과 Agricultural Scale Expansion이 Comprehensive Optimization보다 약간 높아 '종합 시나리오 최고'라는 서술과 차이가 있으며, LSTM 적합 정확도는 수치로 제시되지 않았다. 한계로 선형보간 자료, soil organic carbon 미반영에 따른 과소추정 가능성, 기후·정책 변수 누락, 극한기상 등 불확실성 미고려, 성 단위 분석이 제시됐다. 후속 연구로 soil organic carbon과 농지 방풍림 포함, 현 단위 통계·농가 조사 결합, 기후변화·시장 변동 변수 도입을 제안했다.

## 왜 읽을 만한가

통계연감 기반 농업 탄소수지 산정부터 동인 분석, 시나리오 전망까지 이어지는 절차가 표와 계수로 공개되어 국내 시군 단위 농업 탄소중립 분석에 그대로 참고할 수 있다. 본문 서술과 표 수치의 불일치도 있어 시나리오 결과는 표를 직접 확인하며 읽는 것이 좋다.

## 원문 키워드

`Southwest China`, `agricultural net carbon sink`, `spatial-temporal dynamics`, `STIRPAT model`, `scenario analysis`

## 원문 링크

- 원문: [https://doi.org/10.15666/aeer/2402_28372860](https://doi.org/10.15666/aeer/2402_28372860)
- DOI: [https://doi.org/10.15666/aeer/2402_28372860](https://doi.org/10.15666/aeer/2402_28372860)
