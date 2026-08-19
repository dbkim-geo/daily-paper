---
layout: post
title: "GIS and Remote Sensing-Based Assessment and Mapping of Industrial Pollution Impacts: A Case Study of the Kafue River, Zambia"
date: 2026-08-19 08:30:00 +0900
topic: "Remote Sensing"
topic_key: "remote-sensing"
one_liner: "위성 NDTI·NDVI로 광미댐 붕괴의 환경 영향을 추적하고 조기경보 설계를 제안했다"
authors: "Stanley Kapota, Dabwitso Miti, Musoka Nyongolo, Penjani Hopkins Nyimbili, Erastus Mwanaumo, Wellington Didibhuku Thwala, Masauso Sakala"
venue: "Smart Design Policies"
published: "2026-08-15"
doi: "https://doi.org/10.38027/smart.v3n1-10"
paper_url: "https://doi.org/10.38027/smart.v3n1-10"
pdf_url: "https://smartdpj.com/sdp/article/download/33/43"
source: "openalex"
basis: "full_text"
keywords:
  - "NDTI"
  - "NDVI"
  - "tailings dam failure"
  - "Sentinel-2"
  - "Landsat 8/9"
  - "water quality monitoring"
paper_keywords:
  - "GIS"
  - "Remote Sensing"
  - "Water Pollution"
  - "Kafue River"
  - "NDVI"
  - "NDTI"
  - "Smart Environmental Monitoring"
  - "Zambia"
figure: "/assets/figures/2026-08-19-gis-and-remote-sensing-based-assessment-and-mapping-of.png"
---

## 한 줄 요약

**위성 NDTI·NDVI로 광미댐 붕괴의 환경 영향을 추적하고 조기경보 설계를 제안했다**

![원문 대표 그림]({{ '/assets/figures/2026-08-19-gis-and-remote-sensing-based-assessment-and-mapping-of.png' | relative_url }})

*원문에서 발췌 — Stanley Kapota 외, Smart Design Policies, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

2025년 2월 Zambia Kafue River에서 발생한 Sino-Metals 광미댐(tailings dam) 붕괴의 환경 신호를 Landsat 8/9과 Sentinel-2로 추적한 연구다. 사건 전 3회, 사건 후 3회 총 6개 시점에 대해 NDTI로 수체의 탁도를, NDVI로 하안 식생의 활력을 계산했고 NDWI는 수역과 육상을 가르는 이진 마스크로만 사용했다. 평균 NDTI는 2025년 3월 +0.210까지 급등했다가 6월 −0.009로 맑은 물 수준을 회복한 반면, 평균 NDVI는 2024년 12월 0.345에서 2025년 3월 0.313으로 떨어진 뒤 5개월이 지나도 기준선을 회복하지 못했다. 저자들은 두 지수의 회복 속도 차이를 ZEMA와 WARMA를 위한 이중 지수 위성 조기경보 체계의 설계 요소로 제안한다.

## 주요 차별성

- 단일 사건을 중심으로 NDTI와 NDVI를 sub-monthly 해상도로 짝지어, 수질과 식생의 회복 속도가 다르다는 점을 분리해 보였다.
- 위성 지수 증거를 지수 조합·재방문 주기·경보 임계값·기관 대응 절차라는 구체적 설계 파라미터로 옮겼다. Sub-Saharan Africa 하천 유역에서는 첫 사례다.
- 위성 지수를 화학적 수질의 직접 대리 변수로 다루지 않고, 통계·검증의 한계를 본문에 명시해 해석 강도를 '일관성' 수준으로 낮췄다.

## 주요 기여점

- 2025년 2월 Sino-Metals 광미댐 붕괴에 대해 사건 전후 6개 시점의 NDTI·NDVI 정량 기록을 남겼다.
- 탁도는 1~2개월 내 회복하고 하안 식생은 5개월간 미회복이라는 비대칭 회복 신호를 확인했다.
- ZEMA·WARMA용 설계 요소 네 가지를 제시했다. NDTI를 급성 트리거로, NDVI를 확인 지표로 병행하고, 수일 단위 revisit을 활용하며, NDTI가 +0.15를 지속적으로 넘는 식의 site-specific 임계값을 두고, 자동 이상 탐지에서 현장 검증을 거쳐 규제 조치로 가는 단계적 워크플로를 둔다.
- 위성 감시를 현장 화학 분석의 대체가 아니라, 부족한 현장 검증 역량을 어디에 투입할지 정하는 triage 도구로 자리매김했다.

## 연구의 배경

Kafue River는 Zambia를 1,500 km 넘게 흐르며 약 1,200만 명, 전체 인구의 약 60%를 지탱하고 Lusaka를 포함해 약 500만 명에게 식수를 공급한다. 2025년 2월 18일 Sino-Metals Leach Zambia 구리 시설의 광미댐이 무너져 산성 오염수 약 5,000만 리터가 Mwambashi Stream을 거쳐 이 강으로 흘러들었고, 대규모 어류 폐사와 Kitwe시 상수도 중단이 뒤따랐다. 이는 15개월 사이 Copperbelt에서 발생한 세 번째 광산 폐기물 재해였다.

## 필요성

기존 수질 감시는 현장 채수와 실험실 분석에 의존해 갑작스러운 유출 직후 즉시 가동하기 어렵고, 유역 전체가 아니라 지점 관측만 제공한다. 광미댐 붕괴를 다룬 원격탐사 연구는 대부분 탁도의 급성 반응에 머물러, 같은 사건에 대한 하안 식생의 더 긴 회복 궤적을 sub-monthly 해상도로 함께 본 사례가 드물다. 그런 증거를 규제기관이 실제로 쓸 수 있는 운영 설계 파라미터로 옮긴 연구는 Sub-Saharan Africa 하천 유역에 아직 없었다.

## 목적

Kafue River 100 km 구간을 대상으로 NDTI와 NDVI의 시공간 변화를 파악하고, 그 위성 신호를 ZEMA와 WARMA가 채택할 수 있는 위성 기반 조기경보 정책의 설계 요소로 번역하는 것이 목적이다.

## 방법론

연구 지역은 Mwambashi 합류점 상류 20 km를 오염 전 대조 구간으로 삼고 하류 80 km를 영향권으로 포함한 총 100 km 구간이다. 자료는 USGS Earth Explorer의 Landsat 8/9(30 m)과 Copernicus Open Access Hub의 Sentinel-2(10~20 m)이며, 운량 10% 미만 장면만 골라 사건 전 2024년 8·9·12월, 사건 후 2025년 3·4·6월의 6개 시점을 구성했다. 전처리는 SNAP의 Sen2Cor 대기보정, Landsat 복사보정과 surface reflectance 변환, 하천 중심선 5 km 버퍼 클립, QA pixel band와 Scene Classification Layer를 이용한 cloud masking으로 이뤄졌고, 센서 간 비교를 위해 Sentinel-2를 30 m 격자로 resampling했으나 BRDF·bandpass harmonisation은 적용하지 않았다. 지수는 QGIS raster calculator로 계산했고, NDWI > 0.1을 개방 수면으로 분류해 물 픽셀에는 NDTI를, 하안 육상 픽셀에는 NDVI를 적용했다. 시점별 합성값이 6개뿐이라 paired t-test 같은 모수 검정이나 Mann-Kendall 검정은 수행하지 않고 기술적 비교에 그쳤다.

## 결과

평균 NDVI는 2024년 8월 0.160, 9월 0.173에서 우기인 12월 0.345로 올랐다가 사건 직후인 2025년 3월 0.313으로 0.032 낮아졌다. 4월에 0.334로 일부 회복했으나 12월 기준선 0.345에는 미치지 못했고, 6월에는 건기 진입과 함께 0.239로 떨어졌다. 평균 NDTI는 2024년 8월 −0.013, 9월 −0.008, 12월 +0.042였다가 2025년 3월 +0.210으로 급등했고, 이때 NDTI가 0.20을 넘는 고탁도 구역이 Mwambashi 합류점 하류로 길게 이어졌다. 이후 4월 +0.018로 기준선 부근까지, 6월 −0.009로 맑은 물 수준까지 되돌아왔다. 즉 탁도는 1~2개월 만에 회복했지만 식생은 5개월이 지나도 회복하지 못한 비대칭이 나타났다.

## 논의

NDTI는 빠르게 되돌아오는 급성 수질 신호를, NDVI는 느리게 움직이는 잔류 영향을 담아 서로 보완적이며, 한쪽만 보면 사건의 환경 발자국을 절반만 보게 된다는 것이 핵심 함의다. 저자들은 식생 저하의 원인으로 하안 토양에 남은 중금속을 유력한 가설로 들지만, in-situ 수질·토양 시료가 없고 가뭄 스트레스도 같은 신호를 만들기 때문에 인과가 확정된 것이 아니라 증거와 '일관될 뿐'이라고 명시한다. 우기 사전 관측이 2024년 12월 단 1회뿐인 점, Landsat과 Sentinel-2를 섞어 쓴 데서 오는 잔여 불확실성, NDTI가 용존 오염물질에는 둔감하다는 점도 한계로 함께 적었다. 후속 과제로는 현장 채수·중금속 분석 병행, 여러 해로 관측을 늘려 Mann-Kendall과 Theil-Sen을 적용하는 것, 그리고 제안한 경보 임계값과 대응 절차를 ZEMA·WARMA와 함께 특정 구간에서 시범 운영하는 것을 제시한다.

## 왜 읽을 만한가

무료 위성 자료만으로 오염 사건의 급성 영향과 잔류 영향을 나누어 보는 방법, 그리고 그것을 실제 규제 절차로 옮기는 설계가 함께 담겨 있다. 환경 모니터링 체계나 이상 탐지 파이프라인을 설계할 때, 지수 선택과 임계값 설정의 근거뿐 아니라 위성 지수로는 말할 수 없는 것의 경계까지 참고할 만하다.

## 원문 키워드

`GIS`, `Remote Sensing`, `Water Pollution`, `Kafue River`, `NDVI`, `NDTI`, `Smart Environmental Monitoring`, `Zambia`

## 원문 링크

- 원문: [https://doi.org/10.38027/smart.v3n1-10](https://doi.org/10.38027/smart.v3n1-10)
- PDF: [https://smartdpj.com/sdp/article/download/33/43](https://smartdpj.com/sdp/article/download/33/43)
- DOI: [https://doi.org/10.38027/smart.v3n1-10](https://doi.org/10.38027/smart.v3n1-10)
