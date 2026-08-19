---
layout: post
title: "A longitudinal multi‑proxy geospatial classification of peri‑urban transitions across community health units in coastal Kenya"
date: 2026-08-19 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "다중 위성 proxy로 케냐 연안 보건단위의 peri-urban 전환을 분류한다"
authors: "Prissy Makena, Felix Oluoch, Rosebella Alungata Iseme-Ondiek, Fredrick Owino Gudda, Alfred Keter, Jai Das, Zulfiqar A Bhutta, Anthony Ngugi"
venue: "International Journal of Health Geographics"
published: "2026-08-15"
doi: "https://doi.org/10.1186/s12942-026-00483-5"
paper_url: "https://doi.org/10.1186/s12942-026-00483-5"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "peri-urban"
  - "VIIRS nighttime lights"
  - "Sentinel-2 built-up area"
  - "WorldPop"
  - "Degree of Urbanization"
  - "k-means clustering"
paper_keywords:
  - "urbanization"
  - "peri-urban"
  - "geospatial analysis"
  - "nighttime lights"
  - "Sentinel-2"
  - "WorldPop"
  - "Degree of Urbanization"
  - "Community Health Units"
  - "Kilifi"
  - "Kenya"
figure: "/assets/figures/2026-08-19-a-longitudinal-multiproxy-geospatial-classification-of.png"
---

## 한 줄 요약

**다중 위성 proxy로 케냐 연안 보건단위의 peri-urban 전환을 분류한다**

![원문 대표 그림]({{ '/assets/figures/2026-08-19-a-longitudinal-multiproxy-geospatial-classification-of.png' | relative_url }})

*원문에서 발췌 — Prissy Makena 외, International Journal of Health Geographics, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

사하라 이남 아프리카의 도시화는 공간적으로 불균질하여 행정적 rural·peri-urban 구분만으로는 지역보건 계획을 세우기 어렵다. 연구진은 케냐 Kilifi County의 Kaloleni Rabai Health and Demographic Surveillance System(KRHDSS) 내 10개 Community Health Unit(CHU)을 대상으로 2017~2024년 연간 관측을 수행했다. VIIRS nighttime lights, Sentinel-2 built-up 비율, WorldPop built-up 비율, WorldPop population density, Degree of Urbanization urban 비율 등 5개 공개 geospatial proxy를 CHU 경계 단위로 집계하고 k-means clustering과 cross-proxy vote scoring으로 합의 분류를 도출했다. 그 결과 10개 CHU 중 3개가 consensus peri-urban으로 분류되었고, proxy 간 시계열 거동은 서로 크게 달랐다.

## 주요 차별성

- 단일 지표가 아니라 nighttime lights, Sentinel-2, WorldPop, Degree of Urbanization을 함께 쓰는 multi-proxy 합의 분류 체계를 제시했다
- 행정 경계가 아닌 보건 서비스 운영 단위인 Community Health Unit을 분석 단위로 삼았다
- 단면 분석이 아니라 2017~2024년 8년 연간 패널로 proxy별 변화 속도와 안정성을 비교했다
- proxy별 k-means 결과를 0~5점 vote score로 합산하는 사전 규정 규칙을 사용해 재현 가능한 분류 절차를 만들었다

## 주요 기여점

- 80개 CHU-year 관측으로 구성된 결측 없는 다중 proxy 패널 데이터셋을 구축했다
- proxy 간 concordance를 raw 값, 연간 변화율, 누적 변화율 세 구조로 나누어 정량 비교했다
- Sentinel-2 built-up의 연간 변동성과 Degree of Urbanization의 floor effect라는 상반된 오류 특성을 수치로 드러냈다
- 분석 코드와 CHU-year 데이터셋을 Zenodo에 공개해 다른 감시체계에서 반복 적용할 수 있게 했다

## 연구의 배경

전 세계 인구의 55%가 도시에 거주하며 사하라 이남 아프리카의 도시화는 대도시 확장뿐 아니라 교통축과 중소도시를 따라 진행된다. 이런 peri-urban mosaic은 정적인 행정 분류로는 포착되지 않으면서 인구밀도, 이동성, 지역보건 서비스 비용을 바꾼다. 케냐에서 CHU는 국가 지역보건전략의 기본 운영 단위이지만 CHU 수준의 정착지 성격을 반영한 분류 기준은 부족하다.

## 필요성

Earth observation과 gridded population 자료는 늘었지만 각 산출물은 도시화를 서로 다르게 정의한다. 물리적 확장, 인구 집중, 인프라 발달이 비동기적으로 진행되는 전환기 지역에서는 개별 proxy가 서로 엇갈린 신호를 준다. 따라서 보건 계획에 쓰려면 여러 proxy를 함께 검토해 신뢰 구간을 확인하는 절차가 필요하다.

## 목적

KRHDSS 내 10개 CHU의 다차원 정착지 궤적을 정량화하고 proxy 간 일치도를 비교하는 것이 목적이다. 이를 바탕으로 지역보건 계획의 공간 층화를 주기적으로 갱신할 수 있는 consensus CHU 분류를 도출한다.

## 방법론

케냐 Kilifi County의 Kaloleni·Rabai 지역 10개 CHU를 대상으로 2017~2024년 longitudinal ecological analysis를 수행했다. VIIRS nighttime lights 평균 radiance, Sentinel-2 built-up 면적 비율, WorldPop built-up 면적 비율, WorldPop population density 평균, Degree of Urbanization urban 비율 5개를 CHU 경계 기준 zonal statistics로 집계했다. 공간 처리는 QGIS 3.28.3에서, 통계 분석은 Python 3.10과 scikit-learn에서 수행했다. 연간 변화율과 2017~2024 누적 변화율을 계산하고 10,000회 bootstrap으로 95% 신뢰구간을 추정했으며, proxy 간 일치도는 Fisher z 변환 기반 Pearson correlation으로 평가했다. 분류는 CHU별 proxy 중앙값을 z score로 표준화한 뒤 proxy마다 k=2 k-means clustering을 따로 적용하고, 고강도 cluster 배정 횟수를 합산한 vote score가 3 이상이면 consensus peri-urban으로 정의했다.

## 결과

proxy당 80개 CHU-year 관측이 확보되었고 원자료 결측은 없었다. 2017~2024년 누적 변화율 중앙값은 nighttime lights 62.25%, Sentinel-2 built-up 110.74%, WorldPop built-up 34.14%, population density 14.67%였다. Sentinel-2 built-up은 유효 연간 전이 61건 중 25건(41.0%)이 음수로 변동성이 컸고, Degree of Urbanization은 80개 관측 중 37개가 0인 floor effect를 보였다. 80개 관측을 모은 raw 값 기준 Pearson 상관계수는 0.710~0.955였으나, 연간 변화율에서는 WorldPop built-up과 population density만 유의했다(r = 0.484). cross-proxy vote scoring 결과 Buni와 Mwele Kisurutini가 5점, Vishakani가 4점으로 10개 중 3개(30.0%, 이항 95% CI 6.7~65.2%)가 peri-urban으로 분류되었다.

## 논의

raw 값의 높은 상관은 다섯 proxy가 공통의 정착지 강도 gradient를 포착함을 시사하지만, 변화율 상관이 약하다는 점은 단기 시계열 신호가 산출물 설계에 좌우됨을 뜻한다. Sentinel-2의 변동성은 열대 지역의 cloud contamination과 계절적 식생 변화에서, population density의 좁은 변화 폭은 gridded 모델의 covariate 재분배와 평활화에서 비롯된 것으로 해석된다. 도출된 3개 peri-urban CHU는 KRHDSS 현장에서 이미 peri-urban으로 인식되던 단위와 일치했으나 이는 face validity일 뿐 외부 검증은 아니다. 한계로 10개 CHU라는 작은 표본, CHU 내부 이질성 미반영, k=2와 vote 임계값 3 같은 분석자 선택 의존성이 있으며, 후속 연구로 cloud masking 개선, 대안 clustering 민감도 분석, building footprint 자료 연계 검증이 제시되었다.

## 왜 읽을 만한가

공개 위성·인구 격자 자료를 조합해 행정 경계 기반 도농 구분을 갱신하는 절차를 수치와 코드까지 공개한 사례다. 다중 proxy의 불일치를 오류가 아닌 정보로 다루는 방식은 도시계획·환경계획의 공간 층화 설계에 그대로 응용할 수 있다.

## 원문 키워드

`urbanization`, `peri-urban`, `geospatial analysis`, `nighttime lights`, `Sentinel-2`, `WorldPop`, `Degree of Urbanization`, `Community Health Units`, `Kilifi`, `Kenya`

## 원문 링크

- 원문: [https://doi.org/10.1186/s12942-026-00483-5](https://doi.org/10.1186/s12942-026-00483-5)
- DOI: [https://doi.org/10.1186/s12942-026-00483-5](https://doi.org/10.1186/s12942-026-00483-5)
