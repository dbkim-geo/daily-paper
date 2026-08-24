---
layout: post
title: "Historical Changes and Drivers of Aerosol Acidity in Switzerland under Emission Reduction and Its Implication of Regulation Policies"
date: 2026-08-25 08:30:00 +0900
topic: "탄소저감"
topic_key: "carbon-reduction"
one_liner: "스위스 15년 관측으로 aerosol pH 변화와 그 driver를 규명한 연구다."
authors: "Jun Zhang, Ali Waseem, Andrea Baccarini, Stylianos Kakavas, Christoph Hüglin, Athanasios Nenes"
venue: "Environmental Science & Technology"
published: "2026-07-13"
doi: "https://doi.org/10.1021/acs.est.5c15215"
paper_url: "https://doi.org/10.1021/acs.est.5c15215"
pdf_url: "https://pubs.acs.org/doi/pdf/10.1021/acs.est.5c15215?ref=article_openPDF"
source: "openalex"
basis: "full_text"
keywords:
  - "aerosol pH"
  - "SHAP"
  - "ISORROPIA-lite"
  - "reactive nitrogen deposition"
  - "PM sensitivity regime"
  - "emission control policy"
paper_keywords:
  - "long-term aerosol pH"
  - "driving factor of aerosol acidity"
  - "reactive nitrogen"
  - "emission controls ■"
figure: "/assets/figures/2026-08-25-historical-changes-and-drivers-of-aerosol-acidity-in.png"
---

## 한 줄 요약

**스위스 15년 관측으로 aerosol pH 변화와 그 driver를 규명한 연구다.**

![원문 대표 그림]({{ '/assets/figures/2026-08-25-historical-changes-and-drivers-of-aerosol-acidity-in.png' | relative_url }})

*원문에서 발췌 — Jun Zhang 외, Environmental Science & Technology, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

Aerosol acidity는 PM 조성과 reactive nitrogen(Nr) 침적을 조절하는 핵심 인자다. 유럽의 배출 규제는 SOx와 NOx를 크게 줄였지만 NH3는 거의 줄이지 못해 산성종과 염기성종의 불균형을 만들었다. 이 연구는 스위스 관측소의 2008~2024년 장기 관측자료를 thermodynamic 분석과 SHAP으로 해석해 aerosol pH와 그 driver를 정량화했다. 연평균 pH는 완만한 증가 추세를 보였고, PM은 NH3에 점점 둔감해지고 HNO3에 민감해진 반면 NH3의 빠른 침적은 그대로 남아 NOx와 NH3의 동시 감축이 필요하다는 결론에 이른다.

## 주요 차별성

- SHAP을 aerosol acidity의 driver 정량화에 적용한 첫 사례로 제시했다.
- SHAP을 machine learning 대리모델이 아니라 ISORROPIA-lite thermodynamic 모델에 직접 결합해 물리·화학 관계에 근거한 기여도를 산출했다.
- 스위스 plateau, 남부 사면, semialpine을 아우르는 네 관측소의 15년 자료로 pH 수준·추세·driver를 함께 다뤘다.
- aerosol pH 해석을 PM sensitivity regime과 Nr dry deposition regime 진단까지 연결했다.

## 주요 기여점

- 네 관측소의 장기 aerosol pH 값과 연간 추세를 정량 제시했다.
- temperature, NH3T, SO42- 등 개별 입력 변수가 pH 변동에 기여한 몫을 SHAP으로 분해했다.
- PM이 HNO3-sensitive regime으로 이동하는 장기 변화를 사이트별로 확인했다.
- NH3의 fast deposition이 지속되는 점을 근거로 NOx와 NH3의 동시 감축 정책 필요성을 제시했다.

## 연구의 배경

Aerosol pH는 semivolatile 화학종의 gas-particle partitioning, 이차 aerosol 생성, 미량금속 용해도를 조절한다. NH3, HNO3, NH4+, NO3- 같은 Nr 화학종은 대기 중 수명과 침적 속도가 크게 달라 pH에 따라 거동이 갈린다. 과잉 질소는 식생 생장과 carbon uptake, 지하수 수질에까지 영향을 준다.

## 필요성

유럽은 지난 수십 년간 SOx와 NOx를 크게 줄였지만 농업 기원 NH3 배출은 거의 그대로 두었다. 이런 배출 전환이 aerosol pH를 어떻게 바꾸고, 그 결과 PM의 전구물질 민감도와 질소 침적 regime이 어떻게 달라지는지는 확인되지 않았다. 미국, 캐나다, 중국, 유럽에서 관련 연구가 있었으나 공간적·시간적 coverage의 공백이 남아 있다.

## 목적

스위스 질소 침적 감시망의 장기 자료로 aerosol acidity의 수준, 추세, driver를 규명한다. 이를 통해 PM sensitivity와 질소 침적 regime의 변화를 밝히고 배출 규제 정책의 효과를 평가한다.

## 방법론

스위스 NABEL 관측망의 네 지점, 즉 Payerne(PAY, 489 m), Beromünster(BRM, 797 m), Magadino-Cadenazzo(MAG, 203 m), Rigi-Seebodenalp(RIG, 1031 m)에서 15년간 수집한 자료를 사용했다. NH3, NH4+, HNO3, NO3-는 DELTA-MiniDenuder로 2주 해상도로 포집해 ion chromatography로 분석했고, PAY와 RIG에서는 TSP의 NO3T, NH3T, nonvolatile cations(NVCs)를 일 단위로 확보했다. 기상자료는 MeteoSwiss, 국가 배출량은 EMEP 자료를 썼다. Aerosol pH는 ISORROPIA-lite thermodynamic equilibrium model로 산정했으며, 유기물 수분 흡습과 NVC 크기 보정(PAY 0.2, RIG 0.4)을 적용하고 dust 영향 자료는 PM10/PM2.5 비의 상위 0.05%를 제거해 배제했다. pH driver 분해에는 SHAP을 ISORROPIA-lite에 직접 적용했고, PM sensitivity와 dry deposition regime 분류는 Nenes et al.의 framework를 따랐다.

## 결과

지난 10년간 스위스의 SOx와 NOx 배출은 각각 약 70%, 50% 감소했으나 NH3는 약 10% 감소에 그쳤다. 관측지의 SO42-는 15년간 50~60% 낮아져 최근에는 1 μg m-3 미만이고, NH4+는 50% 이상 줄었으나 기상 NH3는 안정적이거나 오히려 증가했다. 평균 aerosol pH는 BRM 3.68±0.43, MAG 3.48±0.51, PAY 3.34±0.49, RIG 2.99±0.65였고, RIG와 MAG에서 연간 중앙값 pH가 각각 0.012, 0.019 단위/년 증가하는 통계적으로 유의한(p < 0.05) 추세가 나타났다. 월별 pH 변동폭은 BRM, MAG, PAY에서 약 2 단위, RIG에서 약 0.5 단위였다. SHAP 결과 농업지역 관측소에서는 temperature가 1순위, NH3T가 2순위, SO42-가 3순위 driver였고, semialpine 지점 RIG에서는 NH3T가 최대 기여 인자였으며 NO3T의 SHAP 값은 모든 지점에서 낮았다. PM은 시간이 갈수록 HNO3-sensitive regime 비중이 커졌고 MAG에서는 최근 대부분 HNO3-sensitive로 전환됐으며, NH3의 dry deposition은 lowland와 Alpine 모두에서 fast가 우세했다.

## 논의

HNO3 전구물질 감축은 NH3를 줄이지 않고도 PM 저감에 효과적이었으나, NH3의 빠른 침적이 지속되면서 배출원 인근 생태계의 질소 부하가 줄지 않는 문제가 남는다. MAG에서는 NH3 배출이 연 0.4% 감소했음에도 환원질소 침적이 오히려 증가했는데, 이는 fast deposition이 소폭의 배출 감축을 상쇄한 결과로 해석된다. 한계로는 일·2주 평균 자료라 일변화 같은 단기 pH 변동을 포착하지 못하고, NO3- partitioning의 모사-관측 일치도가 NH4+보다 낮으며, MAG와 BRM의 sulfate·NVC·유기물 일부를 인근 지점 자료로 대체했다는 점이 있다. 후속 과제로 저자들은 온난화와 대륙 RH 감소가 pH 상승 추세를 완화하고 HNO3의 fast deposition 비중을 키울 가능성, 그리고 nitrate와 NOx의 비선형 관계를 고려한 감축 수단 분석을 제시한다.

## 왜 읽을 만한가

장기 관측자료에 SHAP을 결합해 배출 규제의 효과를 정량 진단하는 방식은 대기질·탄소중립 정책 평가 연구에 그대로 옮겨 쓸 수 있다. 단일 오염원 감축이 다른 오염원의 거동을 바꿔 정책 효과를 상쇄하는 사례로도 참고할 만하다.

## 원문 키워드

`long-term aerosol pH`, `driving factor of aerosol acidity`, `reactive nitrogen`, `emission controls ■`

## 원문 링크

- 원문: [https://doi.org/10.1021/acs.est.5c15215](https://doi.org/10.1021/acs.est.5c15215)
- PDF: [https://pubs.acs.org/doi/pdf/10.1021/acs.est.5c15215?ref=article_openPDF](https://pubs.acs.org/doi/pdf/10.1021/acs.est.5c15215?ref=article_openPDF)
- DOI: [https://doi.org/10.1021/acs.est.5c15215](https://doi.org/10.1021/acs.est.5c15215)
