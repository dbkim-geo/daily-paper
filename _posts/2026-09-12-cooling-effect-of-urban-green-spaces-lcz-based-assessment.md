---
layout: post
title: "Cooling effect of urban green spaces: LCZ-based assessment comparing four cities at similar latitudes via hotspot and regression models"
date: 2026-09-12 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "위도가 비슷한 4개 도시에서 LCZ별 도시녹지 냉각 효과를 비교했다"
authors: "Dilara Yilmaz, Öznur Işınkaralar, Kaan Işınkaralar, Emmanuel Yeboah, Isaac Sarfo, Ayyoob Sharifi, Sevgi Öztürk, Collins Oduro, Ali Soltani, Mohsen Roohani Qadikolaei"
venue: "International Journal of Biometeorology"
published: "2026-03-19"
doi: "https://doi.org/10.1007/s00484-026-03172-x"
paper_url: "https://doi.org/10.1007/s00484-026-03172-x"
pdf_url: "https://link.springer.com/content/pdf/10.1007/s00484-026-03172-x.pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "local climate zone (LCZ)"
  - "land surface temperature (LST)"
  - "urban heat island"
  - "urban green space"
  - "Getis-Ord Gi*"
  - "Geographically Weighted Regression (GWR)"
paper_keywords:
  - "Climate action"
  - "Land surface temperature"
  - "Life on earth"
  - "Sustainable towns and cities"
---

## 한 줄 요약

**위도가 비슷한 4개 도시에서 LCZ별 도시녹지 냉각 효과를 비교했다**

## 초록 요약

도시녹지(urban green space, UGS)의 냉각 효과가 면적뿐 아니라 공간 배치와 주변 도시 형태에 좌우된다는 문제의식에서 출발한다. 위도는 비슷하지만 형태가 다른 중규모 도시 Salt Lake City(미국), L'Aquila(이탈리아), Krakow(폴란드), Kastamonu(튀르키예)를 대상으로 삼았다. MODIS 기반 land surface temperature(LST), local climate zone(LCZ) 분류, Getis-Ord Gi* hot spot 분석, OLS regression과 Geographically Weighted Regression(GWR)을 결합했다. 공원 400 m 이내에서 냉각이 가장 강했고, 그 크기와 공간적 일관성은 LCZ 유형과 도시 맥락에 따라 체계적으로 달랐다.

## 주요 차별성

- 위도와 해안 영향을 통제하고 도시 형태만 다르게 둔 cross-latitude 비교 설계를 적용했다. 단일 도시나 위도가 다른 도시를 다룬 기존 LCZ 연구와 구분된다.
- LCZ 분류, Getis-Ord Gi* hot spot 분석, OLS와 GWR을 하나의 분석 흐름으로 결합해 전역 관계와 국지적 이질성을 함께 다뤘다.
- 400 m라는 냉각 buffer를 보편 기준으로 두지 않고 LCZ별로 유효 거리가 달라짐을 제시했다. LCZ5/6은 450 m, LCZ3은 350 m, LCZ2는 300 m였다.

## 주요 기여점

- 네 도시의 400 m buffer 내 최대 LST 저감량을 각각 제시했다. Salt Lake City 4.2 °C, Kastamonu 3.5 °C, Krakow 3.1 °C, L'Aquila 2.8 °C다.
- 통계적으로 유의한 hot spot이 고밀 건조환경 LCZ에, cold spot이 자연 LCZ(A~D)와 공원 주변에 집중됨을 확인했다.
- LCZ3 우선 녹화, 자연 LCZ 보전, 냉각 영향권이 겹치도록 약 800 m 간격으로 UGS network를 구성하는 계획 지침을 도출했다.

## 연구의 배경

도시화로 urban heat island(UHI)가 심해지면서 도시 열 저감 전략의 필요성이 커졌다. UGS는 증산과 차폐를 통해 온도를 낮추는 nature-based solution으로 인정받는다. 다만 냉각 능력은 식생 유형, 밀도, 공간 배치, 주변 시가지 구조에 따라 크게 달라진다.

## 필요성

Stewart와 Oke가 제안한 LCZ 체계는 형태와 토지피복을 기준으로 도시 간 열환경 비교를 가능하게 한다. 그러나 기존 LCZ-LST 연구는 대부분 단일 도시이거나 위도와 기후대가 서로 다른 도시를 다뤘다. 위도는 비슷하되 형태가 다른 도시들을 대상으로 UGS 냉각 효과를 비교한 연구는 드물다.

## 목적

위도가 비슷하고 해안 영향이 적은 중규모 도시 4곳에서 UGS가 LST에 미치는 영향이 LCZ 유형에 따라 어떻게 달라지는지 규명한다. 이를 통해 거리 기준의 일반화를 넘어 형태에 민감한 녹지 배치 기준을 제시한다.

## 방법론

대상지는 위도가 비슷하고 해안 영향이 배제된 중규모 도시 Salt Lake City, L'Aquila, Krakow, Kastamonu 4곳이다. LST는 MODIS MOD11A2 v6(공간해상도 1 km) 산출물에서 2023년 6~8월 3개월 평균으로 산정했다. LCZ는 WUDAPT global LCZ raster를 사용했고 분석 단위는 500 m 격자다. UGS polygon은 Google Earth와 OpenStreetMap에서 취득해 400 m buffer를 적용했으며, buffer 안에 포함된 격자는 Salt Lake City 967개, L'Aquila 89개, Krakow 193개, Kastamonu 125개로 총 1,374개다. 열 군집은 Getis-Ord Gi*로 탐지하고, 녹지와 LST의 전역 관계는 OLS regression, 국지적 이질성은 GWR로 추정했으며 분석에는 SPSS 23과 ArcGIS 10.1.1을 사용했다.

## 결과

여름 주간 LST는 약 24.81~56.05 °C 범위였다. 중앙값은 Salt Lake City 56.26 °C, Kastamonu 55.84 °C, L'Aquila 41.20 °C, Krakow 40.44 °C였고, 모든 대상지에서 자연 LCZ의 LST가 건조환경 LCZ보다 낮았다. 400 m buffer 내 최대 LST 저감은 Salt Lake City 4.2 °C, Kastamonu 3.5 °C, Krakow 3.1 °C, L'Aquila 2.8 °C로 추정됐다. Getis-Ord Gi* 분석에서 cold spot은 공원과 400 m buffer 안에 99% 신뢰수준으로 집중됐고, hot spot은 불투수면 비율이 높은 고밀 LCZ에 95~99% 신뢰수준으로 모였다. Krakow의 LCZ3에서는 녹지 피복 한 단위 증가가 LST를 0.214 °C 낮췄고, 같은 LCZ3에서 녹지 10% 증가의 효과는 400 m에서 0.154 °C, 600 m에서 0.042 °C로 감소했다(p < 0.01).

## 논의

냉각 크기는 도시 형태에 따라 갈렸다. Salt Lake City는 건조 기후와 개방형 고층·저층 LCZ가 증산 냉각과 온도 대비를 키운 반면, 자연 LCZ가 이미 넓은 L'Aquila는 추가 녹지의 한계 효과가 작았다. 공간자기상관도 대비를 보여 Moran's I는 격자형 가로망의 Salt Lake City에서 0.789, 농지가 섞인 Krakow에서 0.569였고, 후자는 냉·온 구역이 교차하는 패턴으로 해석됐다. 계획 측면에서는 고밀 저층 LCZ3 우선 녹화, 자연 LCZ 보전, 냉각 영향권이 겹치도록 약 800 m 간격의 UGS network 구성을 제안한다. 한계는 MODIS 1 km 해상도로 미기후 변동을 놓친 점, 여름철에 한정된 분석, 식생 유형과 관개 조건 미반영이며, 후속 연구로 Landsat이나 Sentinel-3 같은 고해상도 열 자료와 NDVI·수관 밀도 등 식생 지표의 결합을 제시한다.

## 왜 읽을 만한가

공원 400 m 영향권이라는 관행적 기준을 LCZ 유형별로 해체해 검증한 사례다. 녹지 배치 우선순위를 정하거나 LCZ와 LST를 결합한 분석 설계를 참고할 때 쓸 만하다.

## 원문 키워드

`Climate action`, `Land surface temperature`, `Life on earth`, `Sustainable towns and cities`

## 원문 링크

- 원문: [https://doi.org/10.1007/s00484-026-03172-x](https://doi.org/10.1007/s00484-026-03172-x)
- PDF: [https://link.springer.com/content/pdf/10.1007/s00484-026-03172-x.pdf](https://link.springer.com/content/pdf/10.1007/s00484-026-03172-x.pdf)
- DOI: [https://doi.org/10.1007/s00484-026-03172-x](https://doi.org/10.1007/s00484-026-03172-x)
