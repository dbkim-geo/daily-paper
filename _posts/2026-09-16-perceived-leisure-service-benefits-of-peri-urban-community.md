---
layout: post
title: "Perceived leisure service benefits of peri-urban community green Spaces: Impact of visual environment during day and night"
date: 2026-09-16 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "주야간 street view 영상으로 본 근교 커뮤니티 녹지의 여가 편익 인식"
authors: "Chongxian Chen, Xinyue Feng, Jing Yao, Xinrui Xiong"
venue: "Landscape and Urban Planning"
published: "2025-03-12"
doi: "https://doi.org/10.1016/j.landurbplan.2025.105338"
paper_url: "https://doi.org/10.1016/j.landurbplan.2025.105338"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "street view image"
  - "semantic segmentation"
  - "geographically weighted regression (GWR)"
  - "ResNet50"
  - "peri-urban green space"
  - "leisure service benefits perception (LSBP)"
---

## 한 줄 요약

**주야간 street view 영상으로 본 근교 커뮤니티 녹지의 여가 편익 인식**

## 초록 요약

중국 광저우 Huadu District의 peri-urban 커뮤니티 녹지를 대상으로 낮과 밤의 leisure service benefits perception(LSBP)을 평가한 연구다. 보행자 시점의 panoramic street view image에 deep learning을 적용해 시각 환경 지표와 LSBP 점수를 산출했다. LSBP의 공간 분포를 지도화하고, 시각 환경과 LSBP의 관계는 geographically weighted regression(GWR)으로 분석했다. LSBP는 대체로 낮이 밤보다 높았고, 시각 요소와 LSBP의 관계는 공간과 시간대에 따라 달랐다.

## 주요 차별성

- 낮에 한정되던 기존 녹지 여가 편익 연구를 야간(19:00~22:30)까지 확장했다.
- 도심 녹지가 아닌 peri-urban 커뮤니티 녹지를 사례 지역으로 삼았다.
- 야간 영상 분석을 위해 ADE20K와 함께 야간 전용 NightCity dataset을 semantic segmentation에 사용했다.
- 전역 회귀 대신 GWR을 써서 시각 요소와 LSBP의 관계가 공간적으로 달라지는 양상을 주야로 나누어 제시했다.

## 주요 기여점

- 낮 58,088장, 밤 49,590장의 보행자 시점 panoramic image 데이터셋을 구축했다.
- physiological·psychological·social·cognitive 4개 범주 9개 지표로 LSBP를 정의하고 ResNet50으로 예측하는 절차를 제시했다.
- green view, sky visibility, landscape diversity, walkability, visual crowdedness 다섯 시각 요소의 영향이 주야로 뒤바뀌는 구간을 실증했다.
- 야간 조명 설계, 저품질 주거지 녹지 정비 등 24시간 여가 서비스 계획을 위한 정책·설계 시사점을 도출했다.

## 연구의 배경

커뮤니티 녹지는 접근성이 좋아 휴식과 사회적 교류의 장으로 기능하며, cultural ecosystem service의 한 축인 여가 서비스를 제공한다. 녹지의 시각 환경은 이용자가 그 공간에서 느끼는 경험을 좌우하는 핵심 요인으로 알려져 있다. 최근에는 설문과 위성영상 대신 street view image와 deep learning으로 시각 환경을 정량화하는 방식이 확산됐다.

## 필요성

기존 연구는 대부분 주간의 여가 편익만 다뤘으나, 근무 시간 때문에 또는 더위를 피해 저녁과 밤에 녹지를 찾는 이용자가 적지 않다. 또한 연구 대상이 도심 녹지에 치우쳐, 도시와 농촌 사이에서 빠르게 변화하는 peri-urban 녹지의 여가 기능은 거의 검토되지 않았다. 팬데믹 이후 peri-urban 녹지 이용이 늘면서 이 공백을 메울 필요가 커졌다.

## 목적

peri-urban 커뮤니티 녹지의 LSBP가 낮과 밤에 어떻게 달라지는지 파악하고, 녹지의 시각 환경이 시간대별로 LSBP에 미치는 영향을 규명하는 것이 목적이다.

## 방법론

사례 지역은 광저우 북부 peri-urban 지대인 Huadu District로, 면적의 약 40.8%가 녹지다. 2023년 7월 1일부터 10월 30일까지 낮(9:00~18:00)과 밤(19:00~22:30)에 Insta360 ONE X2 panoramic camera를 착용한 조사자가 OSM으로 계획한 주요 커뮤니티 도로를 걸으며 촬영했고, 5 m 간격으로 프레임을 추출해 낮 58,088장, 밤 49,590장(2048×512 px, WGS84)의 panoramic image를 얻었다. 시각 환경은 FCN 기반 semantic segmentation을 ADE20K(주간)와 NightCity(야간) dataset에 적용해 GVI, SVI, landscape diversity, walkability를 산출하고, MS COCO 기반 PP-YOLOE object detection으로 visual crowdedness를 계산했다. LSBP는 physiological·psychological·social·cognitive 4개 범주 9개 지표를 0~100점으로 정의했으며, 18~50세 자원봉사자 40명이 낮 11,606장·밤 9,819장을 평가해 만든 586,950건의 점수 기록으로 ResNet50을 학습시킨 뒤 나머지 영상의 점수를 예측했다. 시각 환경과 LSBP의 관계는 bisquare kernel과 AICc 최적 bandwidth를 적용한 GWR로 분석했고, R의 GWmodel package를 사용했다.

## 결과

ResNet50의 five-fold cross-validation 정확도는 모든 지표에서 MAE 8 미만, RMSE 12 미만이었다. LSBP 평균은 밤보다 낮에 높아 comfort는 낮 43.08 대 밤 32.75, healthfulness는 낮 38.59 대 밤 30.64였다. education과 historicalness는 낮과 밤 모두 평균 30 미만(낮 29.53과 26.42, 밤 25.35와 21.98)으로 가장 낮았다. Ma'anshan Park 같은 community park, Jinhe Bay waterfront 같은 blue space, 일부 고품질 주거지는 낮에 높던 LSBP가 밤에 낮은 수준으로 떨어졌다. 주간 GWR에서는 GVI(계수 평균 0.551~0.626)와 SVI가 LSBP를 높이고 walkability와 visual crowdedness는 낮췄으나, 야간에는 다섯 요소의 계수 평균이 모두 양으로 바뀌었고 landscape diversity는 관측 지점의 95% 이상에서 유의한 반면 SVI의 유의 지점 비율은 주간 90% 이상에서 야간 40% 미만으로 줄었다.

## 논의

낮에는 보도와 사람·차량이 많을수록 번잡해져 회복적 경험이 줄지만, 밤에는 같은 요소가 활기와 안전감을 만들어 LSBP를 높이는 것으로 해석된다. 공원과 blue space의 야간 LSBP 하락은 조명 부족과 수면의 그림자 효과, 야간 활동의 부재와 연결된다. 저자들은 저품질 주거지 녹지의 정비, 주야 격차가 큰 지역의 조명 설계와 야간 프로그램 도입을 정책 방향으로 제시한다. 한계는 LSBP를 시각 지각에만 한정한 점과 평가자 집단에서 노인·아동이 빠진 점이며, 후속 연구로 다감각 데이터 활용, 인구 구성 확대, 실제 이용 행태에 대한 causal inference를 제안한다.

## 왜 읽을 만한가

street view image와 deep learning으로 인지된 생태계 서비스를 정량화하고 GWR로 공간적 이질성을 다루는 전형적인 파이프라인을 상세히 보여준다. 주야 비교라는 시간 축을 더해 녹지 계획 연구의 설계를 확장할 때 참고할 만하다.

## 원문 링크

- 원문: [https://doi.org/10.1016/j.landurbplan.2025.105338](https://doi.org/10.1016/j.landurbplan.2025.105338)
- DOI: [https://doi.org/10.1016/j.landurbplan.2025.105338](https://doi.org/10.1016/j.landurbplan.2025.105338)
