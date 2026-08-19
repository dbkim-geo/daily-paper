---
layout: post
title: "Impact comparison of different aerosol types on atmospheric correction of Landsat 8 over land"
date: 2026-08-19 08:30:00 +0900
topic: "Remote Sensing"
topic_key: "remote-sensing"
one_liner: "aerosol type 가정이 Landsat 8 대기보정 정확도를 어떻게 바꾸는지 검증한다"
authors: "Shuning Zhang, Hao Zhang, Bing Zhang, Zhenzhen CUI"
venue: "Atmospheric measurement techniques"
published: "2026-08-12"
doi: "https://doi.org/10.5194/amt-19-5281-2026"
paper_url: "https://doi.org/10.5194/amt-19-5281-2026"
pdf_url: "https://amt.copernicus.org/articles/19/5281/2026/amt-19-5281-2026.pdf"
source: "openalex"
basis: "full_text"
keywords:
  - "atmospheric correction"
  - "Landsat 8"
  - "aerosol optical depth"
  - "surface reflectance"
  - "LaSRC"
  - "AERONET"
figure: "/assets/figures/2026-08-19-impact-comparison-of-different-aerosol-types-on-atmospheric.png"
---

## 한 줄 요약

**aerosol type 가정이 Landsat 8 대기보정 정확도를 어떻게 바꾸는지 검증한다**

![원문 대표 그림]({{ '/assets/figures/2026-08-19-impact-comparison-of-different-aerosol-types-on-atmospheric.png' | relative_url }})

*원문에서 발췌 — Shuning Zhang 외, Atmospheric measurement techniques, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

Landsat 8의 공식 surface reflectance(SR) 산출물은 LaSRC 알고리즘이 Urban Clean이라는 단일 dynamic aerosol type을 가정해 만든다. 이 연구는 2022년 전 지구 100개 AERONET 사이트의 Landsat 8 자료를 이용해 MOD04-based, MOD09-based, Urban Clean 세 가지 dynamic aerosol type이 atmospheric correction(AC) 정확도에 미치는 영향을 비교한다. aerosol optical depth(AOD)에서는 MOD04-based가 가장 정확했고, SR에서는 MOD04-based가 visible and near-infrared(VNIR), LaSRC가 shortwave infrared(SWIR), MOD09-based가 고반사 구간에서 각각 우세했다. 저자들은 이 결과를 근거로 목적별로 aerosol type을 나눠 쓰는 혼합 운영 전략을 제안한다.

## 주요 차별성

- MOD04-based, MOD09-based, Urban Clean 세 dynamic aerosol type이 Landsat 8 대기보정에 미치는 영향을 동일한 AC 프레임 안에서 처음으로 비교한다.
- 전 지구 100개 AERONET 사이트와 634 scene을 사용해, 33개 사이트에 그쳤던 기존 LaSRC 검증보다 넓은 기후대와 대륙을 포괄한다.
- 반사도 0~1 전 구간과 5개 land cover로 나눠 평가해, 저반사 구간에 치우쳐 있던 기존 검증의 사각지대를 메운다.

## 주요 기여점

- 네 가지 SR 산출물의 accuracy(A), precision(P), uncertainty(U)를 전체·밴드별·반사도 구간별로 정량화한다.
- MOD04-based가 AOD와 VNIR SR에서, LaSRC가 SWIR에서 우수함을 permutation test와 bootstrap 기반 유의성 검정으로 확인한다.
- AOD와 VNIR SR은 MOD04-based, 고반사 장면은 MOD09-based, SWIR은 LaSRC를 쓰는 혼합 운영 전략을 제안한다.
- 6SV 기반으로 349 272개 파라미터 조합을 갖는 dynamic aerosol type look-up table(LUT) 구성 절차를 정리한다.

## 연구의 배경

atmospheric correction(AC)은 센서가 받은 복사량을 지표 반사도로 변환하는 원격탐사 전처리의 핵심 단계다. aerosol은 산란과 흡수를 통해 이 과정에 가장 크게 개입하므로, 물리 기반 AC 알고리즘은 aerosol type 가정으로 광학 특성을 대표한다. Landsat 8의 공식 SR을 생산하는 LaSRC는 Urban Clean을 쓰고, MODIS 계열의 MOD04와 MOD09는 서로 다른 subtype 라이브러리와 선택 전략을 쓴다.

## 필요성

널리 쓰이는 dynamic aerosol type들이 동일한 AC 조건에서 비교된 적이 없어, 어떤 가정이 어떤 조건에서 유리한지 알기 어렵다. 기존 LaSRC 검증은 33개 사이트와 저반사 구간에 집중되어, 사막 playa 같은 고반사 지역에서 SR이 과소추정된다는 보고를 설명하지 못한다. 운영 AC에서 적절한 가정을 고르려면 type별 강점과 한계를 체계적으로 확인해야 한다.

## 목적

세 가지 dynamic aerosol type이 Landsat 8의 AOD 및 SR 검색 정확도에 미치는 영향을 전 지구 규모로 정량 비교한다. 이를 바탕으로 장면 특성에 따른 aerosol type 선택 지침을 제시한다.

## 방법론

2022년 한 해 동안 전 지구 100개 AERONET 사이트에서 Landsat 8 OLI Tier 1 Level 1·Level 2 자료를 수집했다. 위성 통과 시각 ±15분 매칭, 사이트 중심 6 km × 6 km 창 절단, CFMask 기반 구름 화소 20% 초과 장면 제외를 거쳐 3800여 scene 중 634 scene을 최종 사용했으며 모든 처리는 Google Earth Engine에서 수행했다. AC에는 6SV로 구축한 349 272개 조합의 LUT를 쓰고 MOD04-based, MOD09-based, Urban Clean 세 dynamic aerosol type을 각각 적용했다. 검증 기준값은 AOD의 경우 AERONET Level 2.0에서 440 nm와 675 nm를 내삽한 AOD550이고, SR의 경우 vector 6S 4.1(6SV)로 모의한 반사도다. 평가는 A, P, U를 전체·밴드별·0.05 폭 반사도 구간별로 계산하고, NDBI·NDSI·BSI·NDVI·NDWI로 추출한 building·snow·soil·vegetation·water 5개 land cover에 대해 RMSE와 bias를 비교하는 방식으로 진행했다.

## 결과

AOD 정확도는 450장의 무운 영상에서 MOD04-based가 가장 높아 R²_AerT 0.7236, RMSE 0.0437, bias 0.0052를 기록했다. Urban Clean은 0.5653/0.0548/0.0106, MOD09-based는 0.4586/0.0612/0.0264로 뒤를 이었고, 세 type 간 RMSE·bias 차이는 Holm 보정 후 p < 0.001, R²_AerT 차이는 p < 0.01 수준에서 유의했다. 634 scene으로 평가한 네 SR 산출물의 A는 −2.9754×10⁻⁴~3.0145×10⁻³, P는 2.3184×10⁻²~2.6020×10⁻², U는 2.3366×10⁻²~2.6040×10⁻² 범위였다. 밴드별로는 MOD04-based가 VNIR의 중저반사 구간에서, LaSRC가 SWIR 특히 Band 7(2.1 µm)에서 가장 정확했고, MOD09-based는 반사도 0.8 이상 고반사 구간에서 오차를 가장 잘 억제했다. land cover별로는 MOD04-based가 snow 전 밴드와 water의 visible(VIS) 밴드에서, LaSRC가 soil과 장파장 밴드에서, Urban Clean이 vegetation·building의 near-infrared(NIR) 대역에서 상대적으로 안정적이었다.

## 논의

MOD04-based의 우위는 계절과 지역 정보를 반영하는 aerosol subtype 선택 방식에서 비롯되며, 잔차 최소화로 subtype을 고르는 MOD09-based는 한 영상 안에서 type이 바뀌어 공간 연속성이 떨어진다. LaSRC의 SWIR 강점은 수증기 등 흡수 기체 처리에 기인하는 것으로 해석되지만, VNIR에서는 체계 오차가 커 물 화소 판별과 cubic spline 내삽이 원인으로 지목된다. 한계로는 1년치 자료와 450개 AOD 표본, AOD 0.2 이하에 치우친 분포, 개활지에 몰린 AERONET 사이트 분포, 지수 기반 land cover 추출의 불확실성이 제시된다. 후속 과제로는 다년 자료 확장, 세분화된 land cover 자료 활용, LaSRC의 SWIR 우위에 대한 메커니즘 규명을 든다.

## 왜 읽을 만한가

Landsat 8 surface reflectance를 시계열 분석이나 지수 산출에 그대로 쓰는 연구자에게 밴드별 오차 구조를 알려준다. VNIR 기반 식생·도시 지수와 SWIR 기반 적설·변화 탐지의 신뢰 수준이 다르다는 점은 전처리 설계에 바로 반영할 수 있다.

## 원문 링크

- 원문: [https://doi.org/10.5194/amt-19-5281-2026](https://doi.org/10.5194/amt-19-5281-2026)
- PDF: [https://amt.copernicus.org/articles/19/5281/2026/amt-19-5281-2026.pdf](https://amt.copernicus.org/articles/19/5281/2026/amt-19-5281-2026.pdf)
- DOI: [https://doi.org/10.5194/amt-19-5281-2026](https://doi.org/10.5194/amt-19-5281-2026)
