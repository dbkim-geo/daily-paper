---
layout: post
title: "Interpreting core forms of urban morphology linked to urban functions with explainable graph neural network"
date: 2026-11-15 08:30:00 +0900
topic: "도시계획"
topic_key: "urban-planning"
one_liner: "explainable GNN으로 도시형태의 핵심 패턴과 도시기능의 연결을 해석한다."
authors: "Dongsheng Chen, Yu Feng, Xun Li, Mingyue Qu, Peng Luo, Liqiu Meng"
venue: "Computers Environment and Urban Systems"
published: "2025-02-24"
doi: "https://doi.org/10.1016/j.compenvurbsys.2025.102267"
paper_url: "https://doi.org/10.1016/j.compenvurbsys.2025.102267"
pdf_url: ""
source: "openalex"
basis: "full_text"
keywords:
  - "urban morphology"
  - "urban function"
  - "graph neural network"
  - "GNNExplainer"
  - "explainable AI"
  - "Delaunay triangulation"
paper_keywords:
  - "Urban morphology"
  - "urban function"
  - "building configuration"
  - "graph neural network"
  - "explainable AI 2"
figure: "/assets/figures/2026-11-15-interpreting-core-forms-of-urban-morphology-linked-to-urban.png"
---

## 한 줄 요약

**explainable GNN으로 도시형태의 핵심 패턴과 도시기능의 연결을 해석한다.**

![원문 대표 그림]({{ '/assets/figures/2026-11-15-interpreting-core-forms-of-urban-morphology-linked-to-urban.png' | relative_url }})

*원문에서 발췌 — Dongsheng Chen 외, Computers Environment and Urban Systems, 2025. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

이 연구는 복잡한 도시형태를 사람이 해석할 수 있는 core urban morphology representation으로 기호화하는 explainable deep learning 프레임워크 CoMo를 제안한다. 보스턴을 대상으로 건물·블록·근린 수준에서 도시기능별 핵심 도시형태를 분석했고, 학습된 모델의 weighted F1-score는 89.14%다. 주거 핵심형태는 urban spine을 따라 도심-도시-교외 전이와 일치하는 점진적 패턴을 보인다. 도시형태가 land use efficiency에 직접 영향을 주며, land use efficiency는 입지와 강한 상관(R²=0.721, p<0.001)을 보인다.

## 주요 차별성

- spatial graph의 가장 대표적인 부분집합만 추려 공간 기호로 바꾸는 core urban morphology representation 개념을 제안했다.
- GNNExplainer로 도시기능 예측에 핵심인 subgraph와 morphometrics를 추출해 GNN의 black-box 한계를 보완했다.
- 추출 결과를 UMAP과 K-Means로 기호화해 건물·블록·근린의 3단계 bottom-up 해석 체계로 연결했다.

## 주요 기여점

- graph construction-learning-interpretation의 3단계로 도시형태와 도시기능의 high-order relationship을 해석하는 CoMo 프레임워크를 제시했다.
- 보스턴에서 데이터 기반의 8개 핵심 건물 유형과 기능별 핵심 building configuration을 도출했다.
- 주거 핵심형태와 도심 거리의 power function 관계를 보여 Alonso의 bid-rent 기반 urban location theory에 실증 근거를 더했다.
- GCN, 차원축소, 군집화 모듈을 다른 기법으로 교체할 수 있는 확장형 구조를 제공한다.

## 연구의 배경

도시형태와 도시기능은 도시 시스템 작동을 설명하는 두 축이다. 둘은 서로를 형성하는 high-order relationship을 가지며, 이를 이해하는 것은 digital twin의 메커니즘 모델링에 중요하다. 기존 연구는 도시형태 지표로 도시기능을 예측하는 데 집중해 왔다.

## 필요성

statistic 기반 표현은 해석은 쉽지만 공간 패턴 정보가 부족하다. computer vision 기반 격자 표현은 주변의 무관한 요소가 섞인다. Delaunay triangulation과 GNN을 결합한 spatial graph 방식은 정확하지만 그래프 정보가 풍부해 도시기능과의 연결을 해석하기 어렵다.

## 목적

복잡한 도시형태를 정확하면서도 사람이 해석할 수 있는 핵심 형태 표현으로 기호화하는 것이 목적이다. 이를 통해 도시형태와 도시기능의 관계를 설명하고자 한다.

## 방법론

연구 지역은 미국 보스턴이며, 2019년 블록 단위 land use 데이터(6개 기능)와 OpenStreetMap 건물 footprint 98,331동을 사용했다. 건물이 4동 이상인 4,695개 블록마다 size·shape·orientation·density의 22개 morphometrics를 노드 속성으로, constrained Delaunay triangulation을 엣지로 하는 urban morphological graph를 구성했다. hierarchical graph pooling 기반 GCN으로 블록 기능을 분류하고 stratified 10-fold cross validation으로 평가했다. 올바르게 예측된 표본에 GNNExplainer(feature 임계값 0.950, edge 임계값 0.900)를 적용해 핵심 subgraph와 지표를 추출했다. 핵심 건물은 UMAP과 K-Means(K=8)로 유형화하고, 블록은 지배 유형 비율(일반 50%, 주거 60%)로 dominant/diverse configuration으로 기호화한 뒤 근린 단위로 집계했다.

## 결과

GCN의 weighted F1-score는 0.891(±0.006), Micro F1-score는 0.907, overall accuracy는 0.908이고 주거 기능 정확도는 0.988이다. 다만 Macro F1-score는 0.438로 industrial과 mixed use 기능은 정확도가 0이었다. 22개 지표 중 10개가 핵심 지표로 선정됐고 그중 8개가 shape 관련 지표였다. 주거 핵심형태는 dominant type 42%, diverse type 58%였으며, 도심에는 매우 길쭉한 건물 중심의 T8-Dom, 남서부 교외에는 단독주택형 T5-Dom이 주로 분포했다. 도심 거리와 land use efficiency의 power function 회귀에서 R²는 원래 형태 대신 근린 대표 핵심형태를 쓸 때 건물 면적 기준 0.576에서 0.721로, 건물 수 기준 지표는 0.296에서 0.478로 높아졌다.

## 논의

저자들은 도심에 가까울수록 주거 형태가 land use efficiency를 높이는 방향으로 바뀐다는 결과가 Alonso의 residential bid-price curve를 뒷받침한다고 해석한다. class balancing 실험 결과 일부 기능의 낮은 예측 성능은 class imbalance보다 표본 부족(industrial)과 형태-기능 간 약한 관계(mixed use) 때문으로 본다. 건물 위치 오차 2 m에서 F1-score가 약 0.005, 5 m에서 약 0.015 감소해 데이터 품질 점검이 권장된다. 형태 외 외부 요인을 반영하지 않았고 보스턴 한 도시에만 적용한 점이 한계이며, 다중 데이터 결합과 다도시 적용이 후속 과제다.

## 왜 읽을 만한가

GeoXAI를 도시형태 해석에 적용해 예측 정확도와 해석 가능성을 함께 다룬 사례다. 건물 footprint만으로 도시기능과 입지 이론을 연결하는 분석 절차를 참고할 수 있다.

## 원문 키워드

`Urban morphology`, `urban function`, `building configuration`, `graph neural network`, `explainable AI 2`

## 원문 링크

- 원문: [https://doi.org/10.1016/j.compenvurbsys.2025.102267](https://doi.org/10.1016/j.compenvurbsys.2025.102267)
- DOI: [https://doi.org/10.1016/j.compenvurbsys.2025.102267](https://doi.org/10.1016/j.compenvurbsys.2025.102267)
