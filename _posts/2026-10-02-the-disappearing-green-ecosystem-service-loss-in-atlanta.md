---
layout: post
title: "The Disappearing Green: Ecosystem Service Loss in Atlanta, Georgia"
date: 2026-10-02 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "30년간 Atlanta의 녹지 손실이 UHI와 PM2.5 악화로 이어졌음을 보인 연구다."
authors: "Kwaku Karikari Manu, Seth Appiah‐Opoku, Madusha Maha Gamage, Kwadwo Nketia Kumankuma Sarpong, Jacob Nchagmado Tagnan"
venue: "Journal of Sustainability"
published: "2025-12-09"
doi: "https://doi.org/10.55845/jos-2025-1289"
paper_url: "https://doi.org/10.55845/jos-2025-1289"
pdf_url: "https://journalofsustainability.net/ojs/JoS/article/download/89/55"
source: "openalex"
basis: "full_text"
keywords:
  - "land use/land cover change"
  - "ecosystem services"
  - "urban heat island"
  - "PM2.5"
  - "Support Vector Machine"
  - "Landsat"
paper_keywords:
  - "Urban Green Spaces"
  - "Land-Use Change"
  - "Biodiversity Loss"
  - "Urban Development"
  - "Green Infrastructure"
figure: "/assets/figures/2026-10-02-the-disappearing-green-ecosystem-service-loss-in-atlanta.png"
---

## 한 줄 요약

**30년간 Atlanta의 녹지 손실이 UHI와 PM2.5 악화로 이어졌음을 보인 연구다.**

![원문 대표 그림]({{ '/assets/figures/2026-10-02-the-disappearing-green-ecosystem-service-loss-in-atlanta.png' | relative_url }})

*원문에서 발췌 — Kwaku Karikari Manu 외, Journal of Sustainability, 2025. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

Atlanta를 대상으로 1995·2005·2015·2025년 Landsat 영상을 Support Vector Machine(SVM)으로 분류해 LULC 변화를 정량화했다. 1995~2025년 동안 forest는 19.94%, water body는 65.17% 줄었고 developed land는 크게 늘었다. 2025년 LST는 식생 지역 21.8°C에서 고밀 시가지 38.4°C까지 분포해 상대 UHI intensity가 16.6°C였다. PM2.5는 시가지에서 18~22 µg/m³로 미개발 지역보다 40% 이상 높았다.

## 주요 차별성

- Landsat-5 TM부터 최신 Landsat-9 OLI-2까지 harmonized 영상으로 Atlanta의 30년 LULC 변화를 추적했다.
- LULC 변화, PM2.5 기반 대기질, UHI 강도를 하나의 분석 틀에서 함께 다뤘다. 저자들은 Atlanta 연구에서 이 조합이 드물다고 밝힌다.
- 토지피복 변화를 ecosystem service 감소라는 기능 중심 관점으로 해석했다.

## 주요 기여점

- 1995~2025년 Atlanta의 forest, developed, water, barren 면적 변화를 10년 단위로 정량화했다.
- UHI hotspot과 고농도 PM2.5 구역이 공간적으로 겹친다는 점을 지도화했다.
- 인구 증가, urban sprawl, 부동산 개발, 교통 인프라 확장을 주요 변화 동인으로 정리했다.
- infill development, green infrastructure, green roof·bioswale 같은 nature-based solutions 등 정책 대안을 제시했다.

## 연구의 배경

Urban green space는 기온 조절, 대기 정화, 우수 관리 등 regulating service를 제공한다. Atlanta Metropolitan Area 인구는 2020년 610만 명에서 2040년 790만 명으로 늘 것으로 전망된다. 이 성장은 자연 지역을 개발지로 전환시키고 있다.

## 필요성

기존 Atlanta 연구는 구형 Landsat 센서나 짧은 기간에 의존한 경우가 많았다. 또 sprawl, 산림 손실, 수문 영향을 따로 분석해 ecosystem service에 미치는 누적 영향을 평가하지 못했다. UHI와 대기오염을 토지피복 변화와 함께 본 연구도 적었다.

## 목적

Atlanta의 녹지 감소 속도, 대기질, UHI 취약성을 평가하는 것이 목적이다. 아울러 변화 동인을 규명하고 정책적 대응을 논의한다.

## 방법론

USGS Earth Explorer에서 Landsat-5 TM(1995), Landsat-7 ETM+(2005), Landsat-8 OLI(2015), Landsat-9 OLI-2(2025) 영상을 받아 LEDAPS와 LaSRC로 surface reflectance를 산출했다. 연구 지역은 Atlanta Regional Commission의 공식 시 경계로 잘랐다. ArcGIS Pro의 SVM으로 Forest, Developed, Water, Barren 4개 클래스를 분류했고, 연도별 클래스당 50개 이상 polygon을 70% 학습, 30% 검증으로 나눠 confusion matrix와 kappa로 평가했다. 2025년 TIRS Band 10과 NDVI 기반 emissivity 보정으로 LST를 산출하고, 최저 LST를 뺀 상대 UHI raster를 만들었다. EPA 관측소 24곳의 PM2.5와 AQI를 Inverse Distance Weighting(IDW)으로 30 m 해상도로 보간해 LULC·LST와 비교했다.

## 결과

Forest는 287,308 ha에서 230,000 ha로 19.94% 줄었고, 10년 단위 감소율은 4.29%, 7.27%, 9.80%로 커졌다. Developed land는 86,107 ha에서 157,125 ha로 82.46% 늘었다(초록에는 83.46%로 표기). Water는 2,585 ha에서 900 ha로 65.17%, barren은 77.45% 감소했다. 2025년 LST는 21.8~38.4°C로 상대 UHI intensity 16.6°C였다. PM2.5는 시가지에서 18~22 µg/m³로 미개발 지역보다 40% 이상 높았고, 고농도 구역은 도심과 북서부에서 UHI hotspot과 겹쳤다.

## 논의

저자들은 sprawl과 인프라 확장이 녹지를 불투수면으로 바꿔 regulating service를 약화시켰다고 해석한다. 피해가 저소득·소외 계층에 집중된다는 점을 urban political ecology와 environmental justice 관점에서 강조한다. 한계로 센서 간 해상도 차이, 유사 분광 클래스 간 혼동, 24개 관측소에 의존한 PM2.5 보간의 불확실성을 든다. 분류 정확도와 PM2.5-LST 상관분석의 구체 수치는 본문에 제시되지 않았다.

## 왜 읽을 만한가

Landsat 장기 시계열, SVM 분류, LST, IDW 보간을 결합한 표준적인 도시 환경 진단 흐름을 한 편에서 볼 수 있다. 녹지 손실을 UHI·대기질과 엮어 green infrastructure 정책 근거로 쓰는 방식을 참고할 만하다.

## 원문 키워드

`Urban Green Spaces`, `Land-Use Change`, `Biodiversity Loss`, `Urban Development`, `Green Infrastructure`

## 원문 링크

- 원문: [https://doi.org/10.55845/jos-2025-1289](https://doi.org/10.55845/jos-2025-1289)
- PDF: [https://journalofsustainability.net/ojs/JoS/article/download/89/55](https://journalofsustainability.net/ojs/JoS/article/download/89/55)
- DOI: [https://doi.org/10.55845/jos-2025-1289](https://doi.org/10.55845/jos-2025-1289)
