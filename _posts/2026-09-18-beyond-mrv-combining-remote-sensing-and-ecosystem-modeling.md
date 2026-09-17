---
layout: post
title: "Beyond MRV: combining remote sensing and ecosystem modeling for geospatial monitoring and attribution of forest carbon fluxes over Maryland, USA"
date: 2026-09-18 08:30:00 +0900
topic: "탄소저감"
topic_key: "carbon-reduction"
one_liner: "lidar와 생태계 모델을 결합해 Maryland 산림탄소 flux를 30 m·연 단위로 복원했다"
authors: "G. C. Hurtt, Lei Ma, Rachel Lamb, Elliott Campbell, Ralph Dubayah, Matthew C. Hansen, Chengquan Huang, Haley Leslie-Bole, Andrew J. Lister, Jiaming Lu, Frances Marie Panday, Quan Shen"
venue: "Environmental Research Letters"
published: "2024-11-08"
doi: "https://doi.org/10.1088/1748-9326/ad9035"
paper_url: "https://doi.org/10.1088/1748-9326/ad9035"
pdf_url: "https://iopscience.iop.org/article/10.1088/1748-9326/ad9035/pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "forest carbon monitoring"
  - "Ecosystem Demography model"
  - "airborne lidar"
  - "above-ground biomass"
  - "disturbance attribution"
  - "climate mitigation planning"
paper_keywords:
  - "forest"
  - "carbon"
  - "monitoring"
  - "climate mitigation"
  - "remote sensing"
  - "modeling"
---

## 한 줄 요약

**lidar와 생태계 모델을 결합해 Maryland 산림탄소 flux를 30 m·연 단위로 복원했다**

## 초록 요약

미국 U.S. Climate Alliance 소속 24개 주는 산림탄소를 기후완화 계획에 넣는 방안을 검토하고 있으나 과거부터 미래까지 이어지는 일관된 산림탄소 자료가 없다. 연구진은 앞서 Maryland주 계획 수립용으로 개발한 high-resolution remote sensing·현장자료·생태계 모델 통합 시스템을 monitoring 용도로 확장했다. 과거 기상과 disturbance 자료를 입력해 1984~2016년 산림 above-ground carbon stock을 30 m 해상도로 연 단위 재구성하고 2023년까지 연장했다. 주 전체 평균 순 above-ground carbon sink는 1.37 Tg C yr−1였고, 연간 변동은 −0.65~2.77 Tg C yr−1로 컸다.

## 주요 차별성

- process-based ecosystem model과 remote sensing을 하나의 일관된 geospatial framework로 결합해 과거 monitoring과 미래 planning에 같은 시스템을 쓴다
- 1 m airborne lidar 기반 baseline biomass에서 출발해 disturbance 이력을 따라 과거로 거슬러 올라가며 시계열을 역산하는 재구성 알고리즘을 새로 구현했다
- factorial 모의실험(ED-B, ED-A1~ED-A4)으로 평균 flux와 연간 변동성을 meteorology, CO2, disturbance 등 개별 driver에 정량적으로 귀속시켰다
- 주(state)·county·개별 disturbance event, 연·십년 단위까지 동일 자료로 보고할 수 있는 정책 대응형 산출물을 제공한다

## 주요 기여점

- Maryland 전역 27,000,000여 개 30 m 격자와 39년, 3,000,000건 이상 disturbance event에 대한 연 단위 AGB stock·flux 지도를 산출했다
- net AGB flux를 persistent, recovering, disturbed 세 성분으로 분해해 잔존 산림의 지속 성장이 순흡수를 주도함을 보였다
- NTSG Landsat NPP, USFS FIA plot, NAFD-DI disturbance intensity 등 독립 자료로 다변수·다축척 검증을 수행했다
- 산출 결과가 Maryland주 온실가스 인벤토리 보고와 조림·재조림 계획에 실제로 사용되었다

## 연구의 배경

산림은 대기 탄소의 큰 흡수원이자 배출원이지만 육상 생태계 flux의 불확실성은 여전히 크다. 미국에서는 24개 주가 주 단위 배출 감축 정책을 두고 있고 33개 주가 기후행동계획을 갖고 있다. Maryland주는 Forest Conservation Act, Greenhouse Gas Reduction Act, Climate Solutions Now Act를 통해 2045년 net zero 목표를 세웠다.

## 필요성

현재 산림탄소를 감축 실적에 반영하는 주는 전체의 4분의 1에 불과하며 사용하는 방법도 제각각이다. 기후완화 계획은 1990년, 2000년, 2005년처럼 이른 기준연도부터의 변화 추적과 driver 귀속을 요구하는데 기존 자료는 이를 충족하지 못한다. monitoring 방법이 미래 계획 수립에 쓰는 방법과 일관되어야 한다는 요구도 충족되지 않았다.

## 목적

계획 수립용으로 개발했던 산림탄소 모델링 시스템에 과거 기상·CO2·disturbance 입력을 추가해, 산림 above-ground carbon stock과 flux의 시공간 변화를 일관되게 monitoring하는 것이 목적이다. 동시에 그 flux를 개별 driver에 귀속시키는 것을 목표로 한다.

## 방법론

연구 지역은 온대 기후에 산림과 woody wetland가 육지 면적의 45%를 차지하는 미국 Maryland주다. 식생 동역학 모의에는 개체 기반 기작 모델인 Ecosystem Demography(ED v3.0)를 사용했으며, 이 모델은 수고와 탄소를 함께 추적해 remote sensing 관측과 직접 연결된다. 입력자료는 2004~2014년 leaf-off 조건에서 취득한 1 m airborne lidar 기반 Canopy Height Model과 NAIP 영상 기반 tree canopy cover, Landsat 기반 disturbance 자료인 NAFD(1985~2016)와 Global Forest Watch(2001~2023), Daymet와 MERRA2를 융합한 1 km 기상자료, NOAA Carbon Tracker의 CO2, SSURGO·CONUS-SOIL 토양자료다. 모델은 1 m lidar·광학 자료로 만든 30 m baseline biomass에서 초기화한 뒤, 교란되지 않은 격자는 시행 초기값 중 baseline AGB를 감싸는 두 사례를 선형 가중해, 교란된 격자는 disturbance event로 나눈 구간마다 같은 절차를 반복해 과거 시계열을 재구성했다. driver 귀속은 meteorology, CO2, disturbance의 시간·공간 변동을 단계적으로 제거한 부분 factorial 실험(ED-B, ED-A1~ED-A4)의 차이로 진단했고, 검증은 NTSG Landsat NPP, USFS FIA plot 자료, NAFD-DI와의 비교로 수행했다.

## 결과

주 전체 산림의 평균 순 above-ground carbon sink는 1.37 Tg C yr−1였고 연간 범위는 −0.65~2.77 Tg C yr−1였다. county 단위 평균 순 flux는 공간적으로 0.01~0.13 Tg C yr−1, 시공간적으로는 −0.43~0.24 Tg C yr−1로 나타났다. 1985~2016년 성분별로는 기존 산림의 지속 성장에 의한 흡수가 1.68 Tg C yr−1, 교란 후 재성장에 의한 흡수가 0.20 Tg C yr−1, 교란에 의한 손실이 0.51 Tg C yr−1였다. 귀속 실험에서는 평균 flux에 disturbance rate가, 연간 변동성에는 transient meteorology가 가장 큰 영향을 미쳤다. 검증에서 모의 NPP는 0.82 ± 0.09 kg C m−2 yr−1로 NTSG 추정치 0.80 ± 0.06과 유사했고 FIA plot 단위 AGB는 R2 = 0.34, RMSE = 3.21 kg C m−2였으며, GFW 입력으로 연장한 2017~2023년 평균 flux는 1.42 Tg C yr−1였다.

## 논의

큰 연간 변동성은 특정 목표연도를 기준으로 감축 실적을 평가하는 정책 설계에 문제를 일으키고 관리 행위의 효과를 가릴 수 있다. 신규 성장보다 기존 산림의 지속 성장 기여가 훨씬 크다는 점은 현존 수관 보전의 중요성을 뒷받침한다. 한계로는 1 m lidar 자료가 특정 시기 단발 취득이라 갱신이 어렵다는 점, disturbance 강도를 직접 관측하지 못해 stand clearing은 과대, partial disturbance는 과소 추정했을 가능성이 있다는 점, 연간 약 40,000 acre 규모 산림관리 중 thinning처럼 교란으로 잡히지 않는 행위가 누락된다는 점이 있다. 후속 연구로는 wetland의 별도 처리, soil carbon과 목제품 pool로의 확장, GEDI·ICESat-2와 NISAR 등 위성 lidar·레이더 자료를 활용한 다른 지역·시기로의 확대가 제시된다.

## 왜 읽을 만한가

탄소중립 계획에 산림 흡수원을 넣으려는 지자체 단위 연구에 바로 적용할 수 있는 monitoring 프레임을 제시한다. remote sensing과 process-based model을 하나의 체계로 묶어 과거 복원과 미래 전망을 함께 다루는 설계가 참고할 만하다.

## 원문 키워드

`forest`, `carbon`, `monitoring`, `climate mitigation`, `remote sensing`, `modeling`

## 원문 링크

- 원문: [https://doi.org/10.1088/1748-9326/ad9035](https://doi.org/10.1088/1748-9326/ad9035)
- PDF: [https://iopscience.iop.org/article/10.1088/1748-9326/ad9035/pdf](https://iopscience.iop.org/article/10.1088/1748-9326/ad9035/pdf)
- DOI: [https://doi.org/10.1088/1748-9326/ad9035](https://doi.org/10.1088/1748-9326/ad9035)
