---
layout: post
title: "Urban forms across continents: A data-driven comparison of Lausanne and Philadelphia"
date: 2026-10-23 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "OSM feature와 GMM으로 Lausanne·Philadelphia의 urban form을 군집·비교한 연구다."
authors: "Arthur Carmès, Léo Catteau, Andrew J. Sonta, Arash Tavakoli"
venue: "Transportation Research Interdisciplinary Perspectives"
published: "2026-01-06"
doi: "https://doi.org/10.1016/j.trip.2025.101823"
paper_url: "https://doi.org/10.1016/j.trip.2025.101823"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "urban form"
  - "OpenStreetMap"
  - "Gaussian Mixture Model"
  - "walkability"
  - "degree centrality"
  - "cross-city comparison"
paper_keywords:
  - "Walkability"
  - "Clustering"
  - "Cities"
  - "Urban Forms"
figure: "/assets/figures/2026-10-23-urban-forms-across-continents-a-data-driven-comparison-of.png"
---

## 한 줄 요약

**OSM feature와 GMM으로 Lausanne·Philadelphia의 urban form을 군집·비교한 연구다.**

![원문 대표 그림]({{ '/assets/figures/2026-10-23-urban-forms-across-continents-a-data-driven-comparison-of.png' | relative_url }})

*원문에서 발췌 — Arthur Carmès 외, Transportation Research Interdisciplinary Perspectives, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

OpenStreetMap에서 street network, multimodality, green space, points of interest 관련 feature를 추출해 두 도시의 urban form을 비교한다. 각 도시를 hexagonal grid 기반 Basic Spatial Unit(BSU)으로 나누고 Gaussian Mixture Model(GMM)로 군집화했다. 도시별로 해석 가능한 urban typology가 도출되었고, 일부 유형은 규모·밀도·문화가 다른 두 도시에서 공통으로 나타났다. 도시별로 grid size를 조정하면 공통 유형 탐지가 개선되었고, degree centrality 단일 feature만으로도 의미 있는 구조 패턴이 포착되었다.

## 주요 차별성

- street network, multimodality, green space, POI를 한 번에 묶은 다차원 feature로 urban form을 latent construct로 다룬다.
- 도시 내부 군집화와 두 도시 feature matrix를 합친 도시 간 공동 군집화를 하나의 framework에서 수행한다.
- 도시별로 grid size를 따로 최적화하는 adaptive resolution이 cross-city 비교에 미치는 영향을 직접 검증한다.
- 31개 feature 전체 군집화와 degree centrality 단일 feature 군집화를 대비해 최소 feature set의 설명력을 확인한다.

## 주요 기여점

- OSM만으로 다른 도시에 위치만 바꿔 적용할 수 있는 open-source urban form 분류 framework를 제시한다.
- 대륙이 다른 두 도시에서 도심·환승 거점·주거지 등 공통 neighborhood typology가 존재함을 보인다.
- cross-city 비교에서 spatial scale, 즉 BSU 크기 선택이 결과를 좌우한다는 방법론적 근거를 제공한다.
- 저연결·저밀도 군집을 인프라·녹지·이동성 투자 우선지역으로 진단하는 계획 도구로서의 활용 방향을 제안한다.

## 연구의 배경

urban form은 가로망, 토지이용, 공공공간, 편의시설 분포를 포괄하며 walkability, 접근성, well-being에 영향을 준다. 서로 다른 국가·대륙의 도시가 공통된 urban form을 갖는지는 도시연구의 오래된 질문이다. 기존 연구는 street network나 building footprint 같은 단일 데이터 유형으로 도시나 동네를 군집화하는 경우가 많았다.

## 필요성

building density, land use mix, 도로망 구조 등 일부 지표만 쓰면 건조환경 요소 간 상호작용이 가려진다. 도시 간 비교는 데이터 가용성, 도시 규모 차이, 다차원 특성 포착의 어려움이 걸림돌이다. 도시 내부 군집을 찾으면서 도시 간 비교도 가능한 유연한 data-driven 방법이 필요하다.

## 목적

OSM 기반 urban form feature에 군집 기법을 적용해 지리·문화적으로 다른 도시의 neighborhood typology를 체계적으로 식별·비교할 수 있는지 검증한다. 공통 유형의 존재, grid size의 영향, feature 분포 유사성의 역할을 4개 research question과 hypothesis로 다룬다.

## 방법론

연구 지역은 스위스 Lausanne과 미국 Philadelphia이며 OpenStreetMap에서 Topography(가로 유형·walk network degree centrality), Multimodality(대중교통 정류장·cycleway·crossing·subway entrance), Points of Interest(건물 유형·음식점·병원 등 amenity), Natural elements의 4개 범주 31개 feature를 추출했다. 행정경계를 hexagonal grid BSU로 나누고 extensive feature는 합계, intensive feature는 평균으로 집계했다. grid size는 silhouette score로 정해 Philadelphia 1,500 m, Lausanne 450 m를 썼다. 군집화는 EM 알고리즘으로 추정한 GMM을 쓰고 cluster 수는 BIC 최소화로 결정했다. 결과는 feature 분포 해석, 멀리 떨어진 동일 cluster cell의 위성영상 비교, 두 도시 feature matrix를 합친 공동 군집화(균일 grid vs 도시별 grid), degree centrality 단일 feature 군집화로 검토했다.

## 결과

BIC 기준 최적 cluster 수는 Lausanne 5개, Philadelphia 7개였다(Table 2·4 기준이며 일부 그림 캡션에는 8개로 표기돼 있다). Lausanne의 Cluster 2는 hypercenter로 pub 8.433, restaurant 7.510 등 정규화 값이 가장 높았고, Cluster 4는 중앙역·선착장 주변으로 train station 값이 9.055였다. Philadelphia의 Cluster 7은 단일 cell의 hypercenter로 commercial building 13.435, cinema 12.628, subway entrance 11.202를 보였다. 두 도시 공동 군집화에서 균일 grid는 Lausanne 중심부 cluster가 Philadelphia에 나타나지 않았지만, 도시별 grid size를 적용하자 두 도심을 포함해 공통 cluster가 늘었다. degree centrality만 쓴 공동 군집화에서는 매우 높은 street network degree 유형이 주로 Lausanne에 나타났고, Philadelphia 유형은 약 5개 cluster에서 BIC 국소 최솟값으로 포착되었다.

## 논의

약 6,300 km 떨어진 두 도시에서 공통 유형이 나타난 것은 CBD, mixed-use 지역, transit-rich corridor의 functional convergence를 시사하며, 저자들은 H1~H4가 지지된다고 해석한다. 한계로 OSM 데이터의 완결성 편차, 보도 품질·조명·체감 안전 같은 질적 요소의 부재, GMM의 Gaussian 분포 가정, grid size·cluster 수 결정의 주관성, 두 도시에 국한된 일반화를 든다. 정량적 군집 품질 지표의 구체적 값은 본문에 제시되지 않고 검증은 위성영상 기반 정성 비교에 머문다. 후속 연구로 sensor·survey·이미지 데이터 통합, DBSCAN·hierarchical clustering 등 비모수 기법, multi-scale 군집화, Global South 도시 확장, 시계열 분석, 주민 참여형 human-centered validation을 제안한다.

## 왜 읽을 만한가

OSM만으로 재현 가능한 neighborhood typology 분류 절차를 제시해 국내 도시 간 비교나 walkability 진단에 바로 응용할 수 있다. 도시 간 비교에서 BSU 크기를 도시별로 조정해야 공통 유형이 드러난다는 점을 실증으로 보여준다.

## 원문 키워드

`Walkability`, `Clustering`, `Cities`, `Urban Forms`

## 원문 링크

- 원문: [https://doi.org/10.1016/j.trip.2025.101823](https://doi.org/10.1016/j.trip.2025.101823)
- DOI: [https://doi.org/10.1016/j.trip.2025.101823](https://doi.org/10.1016/j.trip.2025.101823)
