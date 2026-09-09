---
layout: post
title: "An open-source GIS user interface for the TARGET climate model in the Urban Multi-scale Environmental Predictor (UMEP) tool"
date: 2026-09-10 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "TARGET 도시기후모델을 QGIS의 UMEP 플러그인에 통합한 open-source 인터페이스"
authors: "Jixuan Chen, Peter M. Bach, Matthias Demuzere, JoÃ£o P. LeitÃ£o, Fredrik Lindberg, Kerry A. Nice, Nils Wallenberg"
venue: "Environmental Modelling & Software"
published: "2026-05-26"
doi: "https://doi.org/10.1016/j.envsoft.2026.107043"
paper_url: "https://doi.org/10.1016/j.envsoft.2026.107043"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "TARGET"
  - "UMEP"
  - "QGIS plugin"
  - "urban heat island"
  - "blue-green infrastructure"
  - "urban climate model"
---

## 한 줄 요약

**TARGET 도시기후모델을 QGIS의 UMEP 플러그인에 통합한 open-source 인터페이스**

## 초록 요약

TARGET(Air-temperature Response to Green/blue-infrastructure Evaluation Tool)은 intra-urban 기온을 예측하고 도시 cooling 전략을 평가하는 경량 urban climate model이다. 그동안 user interface가 없어 활용이 제한적이었다. 이 연구는 QGIS 기반 UMEP(Urban Multi-scale Environmental Predictor) 플러그인 안에 TARGET을 통합한 open-source 인터페이스를 제시한다. 입력자료 준비, 시뮬레이션 실행, 결과 시각화까지 전 workflow를 지원하며, Zurich 사례에서 thermal hotspot을 식별하고 개입 시나리오의 cooling 효과를 정량화했다.

## 주요 차별성

- stand-alone Java 및 command-line Python 형태로만 제공되던 TARGET을 QGIS 안의 graphical user interface로 처음 제공한다.
- UMEP의 기존 pre-processor를 재사용해 Land Cover Fraction Calculator에 TARGET 전용 land cover 분류를 확장하고, Morphometric Calculator와 ERA5 다운로드 기능을 그대로 연결했다.
- TARGET Prepare, TARGET Processor, TARGET Analyser 세 모듈로 입력 구성부터 spatial map, time-series plot 생성까지 QGIS 안에서 끝나도록 했다.
- UMEP에 이미 있던 SOLWEIG, SUEWS, UWG가 다루지 않던 city-scale blue-green infrastructure 시나리오 비교 기능을 채웠다.

## 주요 기여점

- TARGET을 PyPI 패키지로 배포하고 UMEP 플러그인에 모듈로 결합해 reference implementation과의 일관성을 유지했다.
- Zurich 도심 28.8 km2를 대상으로 입력자료 준비부터 시나리오 비교까지의 end-to-end workflow를 실증했다.
- hotspot 셀에 대해 simple mean, land cover-weighted mean, severity-weighted mean 세 가지 cooling 지표를 정의해 시나리오 간 정량 비교 절차를 제시했다.
- 코드를 GNU GPL v3로 GitHub의 UMEP 저장소에 공개하고 매뉴얼과 tutorial을 함께 제공한다.

## 연구의 배경

도시는 기후변화와 도시화가 겹치면서 극한 고온에 점점 더 노출되고 있다. tree cover 확대, 녹지 irrigation, 수변 시설 도입 같은 완화 전략을 설계하려면 도시 내부 기온의 공간적 변이를 정량적으로 파악해야 한다. ENVI-met 같은 CFD 모델이나 WRF 같은 mesoscale 모델은 계산 부담과 전문성 요구가 커서 city-scale 시나리오 테스트에는 적합하지 않다.

## 필요성

TARGET은 물리 기반 현실성과 계산 효율을 절충해 이 공백을 메우려 설계됐지만, 실제 사용은 소수 전문가에 머물렀다. 초기 배포본은 stand-alone Java 코드였고, 이후 Python 버전도 command-line 실행과 프로그래밍 능력을 요구했다. 도시계획가, 환경 컨설턴트처럼 모델을 실제 의사결정에 쓸 수 있는 실무자는 이런 진입장벽 때문에 접근하지 못했다.

## 목적

TARGET을 QGIS의 UMEP 플러그인 안에 통합해 입력자료 준비, 시뮬레이션 실행, 결과 시각화를 하나의 인터페이스에서 수행할 수 있게 하는 것이 목적이다. Zurich 사례를 통해 이 workflow가 hotspot 식별과 개입 시나리오 평가에 실제로 쓰일 수 있음을 보인다.

## 방법론

TARGET은 roof, concrete, asphalt, dry grass, irrigated grass, tree, water의 land cover fraction, 건물 형상, 기상 강제력을 입력으로 받아 sky view factor 기반 radiation balance와 energy balance를 계산한다. ground storage flux는 Objective Hysteresis Model(OHM)의 변형을 써서 추정하고, 격자별 결과를 합쳐 2 m 높이 기온의 2D 지도를 만든다. 사례 지역은 Zurich 도심 28.8 km2로, 100 m 해상도 polygon grid에서 시뮬레이션했다. land cover는 공식 계획 vector 자료를 TARGET 7개 범주로 재분류해 2 m raster로 변환했고, 건물 형상은 swissALTI3D의 DEM과 swissSURFACE3D의 DSM(둘 다 0.5 m)에서 Morphometric Calculator로 산출했다. 기상 자료는 인근 Fluntern 관측소(해발 556 m)의 10분 평균값을 썼고, 일 최고기온이 30도를 넘은 2023년 7월 6~9일 4일을 대상으로 첫날은 spin-up으로 제외했다.

## 결과

baseline 시뮬레이션에서 urban-rural 기온차가 양수인 격자 125개를 hotspot으로 식별했고, 도심부와 주요 교통축에 집중됐다. hotspot 셀의 concrete와 dry grass를 전면 치환하는 세 시나리오 가운데 tree cover expansion이 가장 효과적이어서 hotspot을 21개로 83% 줄였고 평균 기온 감소 0.60도, 최대 감소 1.60도를 기록했다. greening and irrigation은 hotspot을 57% 줄이며 평균 0.27도, water features는 46% 줄이며 평균 0.19도 낮췄다. tree cover expansion의 severity-weighted 평균 감소는 0.76도로 단순 평균보다 커서, 과열이 심한 격자일수록 수목의 냉각 효과가 컸다. 4일 시뮬레이션은 전처리를 포함해 일반 데스크톱에서 한 시간 이내에 끝났다.

## 논의

이 인터페이스는 물리 기반 도시기온 모델링을 지자체 계획부서와 컨설턴트가 쓸 수 있는 수준으로 낮추고, 상세 모델을 어디에 투입할지 정하는 first-order screening 도구 역할을 한다. 다만 시나리오는 concrete와 dry grass를 100% 치환한 이상적 가정이라 냉각량은 상한값에 해당하고, 물리적, 재정적, 제도적 제약을 반영하지 않았다. 정량 결과는 Zurich의 도시 형태와 해당 heatwave 조건에 특정되므로 다른 도시로 그대로 옮길 수 없다. horizontal advection과 anthropogenic heat flux는 모델에 없고 시나리오 설계용 point-and-click 도구도 아직 없어, 사용자는 QGIS Raster Calculator로 직접 편집해야 하며 향후 자동 시나리오 생성과 URock 연계, mean radiant temperature 및 UTCI 출력 확장이 예정돼 있다.

## 왜 읽을 만한가

도시 열환경 완화 대안을 city-scale에서 빠르게 비교해야 하는 연구자와 실무자가 코딩 없이 쓸 수 있는 open-source workflow다. GIS 자료만 갖춰지면 국내 도시에도 곧바로 적용해 hotspot과 녹지 개입 효과를 정량화할 수 있다.

## 원문 링크

- 원문: [https://doi.org/10.1016/j.envsoft.2026.107043](https://doi.org/10.1016/j.envsoft.2026.107043)
- DOI: [https://doi.org/10.1016/j.envsoft.2026.107043](https://doi.org/10.1016/j.envsoft.2026.107043)
