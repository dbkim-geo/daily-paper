---
layout: post
title: "Patterns of Current Urban Expansion in Germany: A Comparative Analysis of Five City Regions"
date: 2026-09-01 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "독일 5개 도시권 transect의 도시 확산 패턴을 GIS로 비교했다."
authors: "Michael Swiacki, Henning Nuissl, Yuri Agista"
venue: "Urban Planning"
published: "2026-08-27"
doi: "https://doi.org/10.17645/up.12067"
paper_url: "https://doi.org/10.17645/up.12067"
pdf_url: "https://www.cogitatiopress.com/urbanplanning/article/download/12067/5238"
source: "openalex"
basis: "full_text"
keywords:
  - "urban expansion"
  - "urban sprawl metrics"
  - "suburbanization"
  - "GIS analysis"
  - "material stock"
  - "accessibility analysis"
paper_keywords:
  - "accessibilityanalysis"
  - "GISanalysis"
  - "suburbanization"
  - "urbanexpansion"
  - "urbansprawl"
---

## 한 줄 요약

**독일 5개 도시권 transect의 도시 확산 패턴을 GIS로 비교했다.**

## 초록 요약

재도시화 이후 독일 대도시권에서 다시 나타난 urban expansion을 다룬 연구다. Berlin, Hamburg, Munich, Frankfurt am Main, Freiburg im Breisgau 5개 도시권에서 대규모 greenfield 사업이 계획된 구역을 transect로 잘라 GIS 분석을 수행했다. 개발 역동성은 사례 간에도, 한 도시권 내부에서도 규모와 건물 유형 면에서 크게 달랐다. 저자들은 German census의 공간 데이터에 urban sprawl 지표, material efficiency 지표, 교통 인프라 접근성 지표를 결합해 이 패턴들이 지속가능성 기준을 충족하는지 평가했다.

## 주요 차별성

- 도시 확산을 suburbanization과 new residential development(NRD) 두 축으로 동시에 개념화해 행정경계 기반 이분법을 벗어났다.
- 행정구역 대신 도심 외곽부터 인접·원거리 교외 기초자치단체까지 가로지르는 wedge 형태의 transect를 5개 도시권에 일관되게 설정했다.
- remote sensing 기반의 공개 material stock 데이터를 도입해 토지 소비 중심의 기존 sprawl 평가에 자원 효율 차원을 추가했다.
- urban sprawl metrics, 철도 기반 대중교통 accessibility, material efficiency를 한 틀에서 함께 적용해 지속가능성을 다차원으로 판정했다.

## 주요 기여점

- 2011~2022년 5개 transect의 인구·정주밀도·건물 유형 변화를 동일한 기준으로 비교한 정량 결과를 제시했다.
- NRD가 발생한 100m 격자 셀을 식별하고 그 안의 우세 건물 유형을 도시권별·기초자치단체별로 분해해 보여줬다.
- SFH 우세 NRD와 MFH-large의 1인당 material mass 격차를 수치로 제시해 건물 유형 선택의 자원 함의를 드러냈다.
- 격자 census 데이터와 GIS 데이터를 결합하는 transect 기반 분석 절차를 후속 연구가 재사용할 수 있는 형태로 정리했다.

## 연구의 배경

독일 대도시권에서는 reurbanization 국면 이후 다시 외연 확산이 관측되며 이를 'fifth suburbanization'이라 부른다. 도시 외곽의 저밀도 single-family housing(SFH) 건설이 계속된다는 지적과 함께, 최근 대규모 주택단지 증가로 밀도 높은 multi-family housing(MFH)이 늘었다는 보고도 함께 나온다. 기존의 도시-교외 이분법으로는 이런 이질적 개발 패턴을 담기 어렵다는 문제 제기가 이어져 왔다.

## 필요성

suburbanization은 보통 행정경계로 나눈 내·외부 지역의 성장률 비교로 정의되는데, 이는 경계 안팎이 균질하다는 가정을 깔고 있다. 실제 도시권은 다핵성, 패치형 정주구조, 중심화와 분산의 동시 진행을 보이므로 확산과 내부 개발을 구분하기조차 어렵다. 또한 신규 불투수면 면적만 보는 평가는 건물 유형에 따른 자원 소비 차이를 놓친다.

## 목적

현재 독일 도시권의 도시 확산 패턴과 그 내부 이질성을 세밀하게 기술하는 것이 목적이다. 나아가 이 확산이 밀도·압축성, 자원 효율, 대중교통 접근성이라는 지속가능성 차원을 이전 교외화 국면보다 더 충족하는지 판정한다.

## 방법론

Berlin, Hamburg, Munich, Frankfurt am Main, Freiburg 5개 도시권에서 대규모 확장 사업이 계획 중인 구역을 포함하도록 transect를 설정했다. 각 transect는 도심 고밀지역을 제외하고 중심도시 외곽부에서 인접 교외 기초자치단체까지 이어진다. 데이터는 2011년·2022년 German census의 100×100m 격자 인구·건물 자료, 2010년·2020년 GHS-BUILT-S(100m), 2009~2018년 Historic Material Stocks(30m), 2025년 OpenStreetMap 대중교통 자료를 사용했다. census의 10개 건물 범주를 SFH-detached, SFH-terraced, MFH-small, MFH-large로 통합하고, 100m 셀 단위 점유 비율 임계값으로 우세 건물 유형 zone을 분류했다. 지속가능성 평가는 Jaeger and Schwick(2014)의 urban sprawl metrics(PBA, LUP, DIS, WUP, WSPC), 궤도계 대중교통 정류장 1,000m 도보 catchment 기반 accessibility 분석, 1인당 material mass 계산 세 가지로 수행했다.

## 결과

2011~2022년 5개 transect 모두에서 인구와 정주밀도가 늘었고, 건물 수는 8.1%에서 15.9%까지 증가했다. 가장 빠르게 증가한 유형은 MFH-large로 Munich 59.2%, Frankfurt 58.8%, Freiburg 53.0%였으며, 정주밀도 증가율은 Munich 10.56%, Frankfurt 8.93%, Berlin 6.97%, Freiburg 3.05%, Hamburg 2.52%로 갈렸다. NRD 셀 수는 Berlin 131개, Hamburg 100개인 반면 Freiburg는 14개에 그쳤고, Freiburg와 Berlin은 NRD의 75% 이상이 SFH 우세인 데 비해 Munich는 60% 이상이 MFH 우세였다. urban sprawl metrics에서는 PBA, DIS, WUP가 모든 transect에서 상승했지만 LUP와 WSPC는 하락해, 인구 증가가 토지 소비를 앞질렀음을 보여줬다. 궤도계 대중교통 1km 내 거주 인구 비율은 Frankfurt 68.8%, Munich 65.2%로 높고 Hamburg는 24.9%에 머물렀으며, NRD 기준 1인당 material mass는 SFH 우세 셀이 평균 222톤, MFH-large가 76톤이었다.

## 논의

외곽부 신규 개발이 예상보다 압축적이고 MFH 비중이 커지고 있어, 확산이 곧 sprawl이라는 통념보다 덜 산발적이라는 것이 저자들의 해석이다. 다만 도시권 간에도, 한 transect 내부의 기초자치단체 간에도 편차가 커서 밀도화·유형 다양화, SFH 지배, NRD 부재라는 서로 다른 지역 전략이 공존하며, 독일 기초자치단체의 강한 계획 자율성이 이 이질성에 기여한 것으로 본다. 한계로는 census가 건물 footprint가 아닌 격자 단위로 제공되어 절대값보다 상대 지표와 공간 패턴 위주로 해석해야 한다는 점, 지역 경제 여건과 지형 제약을 반영하지 못한 점, 대중교통 서비스 빈도와 품질을 배제하고 근접성만 따진 점을 든다. 후속 과제로는 학교·보육시설 등 사회 인프라 포함, 대안적 접근성 가정 검토, NRD 입주 가구의 사회인구학적 구성 연구를 제시한다.

## 왜 읽을 만한가

격자 census, GHS-BUILT-S, material stock, OSM을 결합해 도시 확산의 지속가능성을 다차원으로 계량화한 사례라 GIS 기반 도시계획 연구의 지표 설계에 참고가 된다. transect 방식은 행정경계에 갇히지 않는 도시권 분석 단위를 고민할 때 쓸 만하다.

## 원문 키워드

`accessibilityanalysis`, `GISanalysis`, `suburbanization`, `urbanexpansion`, `urbansprawl`

## 원문 링크

- 원문: [https://doi.org/10.17645/up.12067](https://doi.org/10.17645/up.12067)
- PDF: [https://www.cogitatiopress.com/urbanplanning/article/download/12067/5238](https://www.cogitatiopress.com/urbanplanning/article/download/12067/5238)
- DOI: [https://doi.org/10.17645/up.12067](https://doi.org/10.17645/up.12067)
