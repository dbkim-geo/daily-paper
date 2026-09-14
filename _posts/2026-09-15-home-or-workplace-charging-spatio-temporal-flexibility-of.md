---
layout: post
title: "Home or workplace charging? Spatio-temporal flexibility of electric vehicles within Swiss electricity system"
date: 2026-09-15 08:30:00 +0900
topic: "탄소중립"
topic_key: "carbon-neutral"
one_liner: "EV 직장 충전이 스위스 전력계통 유연성에 주는 효과를 분석했다"
authors: "Zongfei Wang, Jan-Philipp Sasse, Evelina Trutnevyte"
venue: "Energy"
published: "2025-03-04"
doi: "https://doi.org/10.1016/j.energy.2025.135452"
paper_url: "https://doi.org/10.1016/j.energy.2025.135452"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "electric vehicles"
  - "workplace charging"
  - "sector coupling"
  - "spatio-temporal flexibility"
  - "electricity system optimization"
  - "solar PV"
---

## 한 줄 요약

**EV 직장 충전이 스위스 전력계통 유연성에 주는 효과를 분석했다**

## 초록 요약

이 연구는 2035년 스위스를 대상으로 electric vehicle(EV) 충전 부하를 집에서 직장으로 옮길 때 전력계통에 미치는 영향을 분석했다. 2,169개 municipality 해상도의 spatially-explicit 전력계통 최적화 모델 EXPANSE에 vehicle commuting matrix를 결합했다. 직장 충전은 재생에너지 비중이 이미 높지 않은 한 전력 수입과 저장 수요를 줄이고 solar PV 통합을 촉진했다. 모든 자가용이 EV일 때 계통 관점의 최적 직장 충전 비율은 90% 이상이었고, 스위스 북부와 서부에서 일관되게 선호됐다.

## 주요 차별성

- EV를 시간적 가용성이 제한된 배터리로만 보던 기존 대규모 계통 모델과 달리, 같은 EV가 충전 위치를 집에서 직장으로 바꾸는 spatio-temporal flexibility를 다뤘다.
- 저자들이 아는 한 처음으로 EV 모델링을 국가 규모 전력계통 모델과 결합해 거시 수준에서 EV의 공간적 유연성을 분석했다.
- 전력계통 모델과 통근 교통망을 모두 2,169개 municipality 해상도로 맞춰 결합했다.

## 주요 기여점

- EXPANSE에 EV module을 추가해 통근 EV의 충전 위치를 계통 전체 비용 최적화 안에서 결정하도록 확장했다.
- 원전 단계적 폐지 수준과 재생에너지 목표 조합별로 직장 충전이 solar PV, 전력 수입, pumped hydropower storage(PHS)에 미치는 영향을 정량화했다.
- 직장 충전 선호 지역(북부·서부)과 PV 증가 지역(중부·남부)의 공간적 불일치를 밝혀, 국가 단위 고해상도 모델링의 필요성을 제시했다.

## 연구의 배경

EU에서 도로 교통은 2021년 CO2 배출의 28%를 차지했고, 그중 여객 교통이 64%를 차지한다. EV 확산은 교통과 전력 부문을 결합하며, 비제어 충전은 저녁 피크와 국지적 계통 병목을 유발할 수 있다. 반면 긴 주차 시간과 조절 가능한 충전 전력은 계통에 유연성을 제공할 수 있다.

## 필요성

기존 controlled charging 연구는 주로 언제 충전할지라는 시간적 측면만 다뤘다. 공간적 유연성 연구는 배전망·교통망 연계 같은 미시 수준에 머물러 계통 전체에 대한 영향을 보여주지 못했다. 스위스는 2035년 신규 재생에너지 확대와 2050년 탄소중립을 목표로 하고, 통근자의 절반 이상이 자가용을 이용해 이 분석에 적합하다.

## 목적

집 충전과 직장 충전의 선택이 재생에너지 통합, 저장 기술 수요, 전력 부문 전체를 어떻게 바꾸는지 규명한다. 또한 전력 부문 관점에서 직장 충전 인프라가 어디에 입지하는 것이 최적인지 찾는다.

## 방법론

Swiss Statistical Office의 commuter transport matrix(약 7만 2천 개 경로)와 Mobility and Transport Microcensus(MTMC, 약 8천 개 경로)를 결합해 municipality 간 통근 차량 수를 추정했다. 매칭되지 않은 경로는 9개 municipality 유형과 4단계 거리 기준으로 군집화해 보완했다. EXPANSE는 Pyomo 기반 linear programming 비용 최적화 모델이며, 이 연구에서는 6시간 시간 해상도로 운영했다. 충전 프로파일은 260만 건의 실측 충전 데이터에서 도출했고, 100% 자가용 EV 가정 하에 EV 476만 대, 통근 EV 183만 대, EV 수요 11.4 TWh/year를 설정했다. 시나리오는 원전 용량 100%·50%·0%(N10·N5·N0), 재생에너지 목표 없음·17·25·35 TWh/year(Rx·R17·R25·R35), 비제어 충전(V0)·최적 제어 충전(Vx)·직장 충전 강제 비율 20~100%(V2~V10)로 구성했다.

## 결과

모든 시나리오에서 통근 EV의 90% 이상(164만 대 이상)이 직장 충전으로 전환하는 것이 비용 최적이었다. 평일 기준 직장 충전은 저녁 피크를 약 9%(1.13 GW) 낮추고 정오 수요를 16%(1.55 GW) 높였다. solar PV 발전의 유의한 증가는 N5Rx, N0Rx, N0R25 시나리오에서만 나타났고, 재생에너지 목표가 R25·R35로 높을 때 PHS 이용이 크게 줄었다. N0R25 시나리오에서 직장 충전은 solar PV 통합을 최대 1.6 TWh/year 늘렸으며, 이는 스위스 연간 수요의 2.3% 이상이다. 직장 충전은 인구가 많은 북부·서부 canton에서 선호됐지만, PV 증가는 설비이용률이 높은 중부·남부에서 나타나 공간적 불일치가 확인됐다.

## 논의

직장 충전이 PV를 늘린다는 기존 미시적 분석과 달리, 계통 전체 최적화에서는 그 효과가 원전 폐지 수준과 재생에너지 목표에 따라 조건부로 나타났다. 저자들은 국지적 최적화가 전국적 편익으로 이어지지 않을 수 있어 인프라 계획에 높은 공간 해상도가 필요하다고 본다. 한계로는 도착 즉시 충전만 가정해 지연 충전 같은 시간적 유연성을 다루지 않은 점, EV 보급률·지역별 충전 패턴·공공 충전 비중의 대표성이 제한된 점, 충전 인프라와 배전망 비용을 목적함수에 넣지 않은 점을 들었다. 후속 연구로 smart charging 전략과 heat pump 같은 다른 demand-side flexibility의 통합을 제안했다.

## 왜 읽을 만한가

통근 OD 데이터를 municipality 단위 전력계통 최적화 모델에 결합한 사례로, 교통·에너지 부문 결합 탄소중립 계획에 공간 해상도가 왜 중요한지 보여준다. 충전 인프라 입지와 재생에너지 입지를 함께 검토하려는 도시·에너지 계획 연구에 참고할 만하다.

## 원문 링크

- 원문: [https://doi.org/10.1016/j.energy.2025.135452](https://doi.org/10.1016/j.energy.2025.135452)
- DOI: [https://doi.org/10.1016/j.energy.2025.135452](https://doi.org/10.1016/j.energy.2025.135452)
