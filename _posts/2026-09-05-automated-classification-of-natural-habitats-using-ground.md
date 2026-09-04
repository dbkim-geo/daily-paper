---
layout: post
title: "Automated classification of natural habitats using ground-level imagery"
date: 2026-09-05 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "지상에서 찍은 사진만으로 18개 habitat 유형을 딥러닝으로 분류한다"
authors: "Mahdis Tourian, Sareh Rowlands, Remy Vandaele, Max Fancourt, Rebecca Mein, Hywel T. P. Williams"
venue: "arXiv (preprint)"
published: "2025-08-26"
doi: ""
paper_url: "https://arxiv.org/abs/2508.19314v1"
pdf_url: "https://arxiv.org/pdf/2508.19314v1"
source: "arxiv"
basis: "full_text"
keywords:
  - "habitat classification"
  - "ground-level imagery"
  - "DeepLabV3-ResNet101"
  - "transfer learning"
  - "Living England"
  - "citizen science"
---

## 한 줄 요약

**지상에서 찍은 사진만으로 18개 habitat 유형을 딥러닝으로 분류한다**

## 초록 요약

위성영상 기반 habitat 분류는 생태학자의 현장 검증에 의존해 시간과 비용이 크다. 이 연구는 지상에서 촬영한 사진(ground-level imagery)만으로 habitat 유형을 자동 분류하는 방법을 제시한다. Natural England와 협력해 'Living England' 체계의 18개 클래스를 대상으로 DeepLabV3-ResNet101 분류기를 fine-tuning했다. five-fold cross-validation에서 평균 F1-score 0.61을 얻었고, Bare Soil, Silt and Peat(BSSP)와 Bare Sand(BS) 같이 시각적으로 뚜렷한 클래스는 0.90을 넘었다.

## 주요 차별성

- 위성영상이 아니라 지상 촬영 사진만으로 terrestrial habitat 유형을 분류한 첫 시도다. 저자들은 영국 맥락에서 선행 연구가 없다고 밝힌다.
- semantic segmentation용으로 설계된 DeepLabV3-ResNet101의 segmentation head를 1×1 convolution과 global average pooling으로 교체해 image-level 분류기로 개조했다.
- 국가 단위 보전 정책 체계인 Living England taxonomy에 그대로 정렬된 18개 클래스를 사용해 기존 생태 데이터·정책과 연결되도록 했다.
- 생태학자가 현장 조사 중 직접 촬영하고 라벨링한 43,092장 규모의 데이터셋을 학습에 활용했다.

## 주요 기여점

- Living England 18개 habitat 클래스에 대한 ground-level 이미지 분류 모델을 구축하고 five-fold cross-validation으로 성능을 검증했다.
- 클래스별 precision, recall, F1-score와 confusion matrix를 제시해 어떤 habitat이 서로 혼동되는지 구체적으로 밝혔다.
- Top-1 외에 Top-3 예측과 confidence를 기록해, 모호한 클래스에서도 정답이 상위 후보에 남는다는 점을 정량화했다.
- 실무자가 이미지를 업로드해 Top-3 예측을 받고 피드백을 남길 수 있는 Streamlit 기반 web application을 배포했다.

## 연구의 배경

habitat 분류는 생물다양성 보전, 토지 관리, 생태 모니터링의 기본 도구다. 영국에서는 Living England 프로젝트가 Sentinel-1/2 위성영상과 object-based random forest를 결합해 약 10m 해상도로 전국을 18개 habitat 클래스에 할당하며, 2022–23 버전의 전체 정확도는 약 87–88%다. 그러나 이런 위성 기반 접근은 여전히 훈련된 생태학자의 현장 검증을 필요로 한다.

## 필요성

수작업 분류는 노동집약적이고 시간이 오래 걸리며 사람에 따른 오차가 발생한다. 위성 기반 자동 분류도 이질적이거나 전이대(transitional) 경관에서 세분화된 habitat 구분에 약하고 현장 검증 부담이 남는다. 반면 지상 사진은 스마트폰으로 쉽게 얻을 수 있고 citizen science나 소셜미디어 수집으로 대량 확보가 가능해, 이를 자동 분류할 수 있다면 검증과 확장 문제를 동시에 완화할 수 있다.

## 목적

지상에서 촬영한 habitat 사진만으로 Living England taxonomy의 habitat 유형을 computer vision으로 자동 분류할 수 있는지 확인하는 것이 목적이다. 아울러 클래스별 성능과 오분류 패턴을 분석하고 실무 활용 도구를 제공하는 것을 목표로 한다.

## 방법론

데이터는 Natural England 생태학자들이 Living England 현장 조사 중 촬영한 RGB 지상 사진 43,092장이며, 각 이미지는 현장 위치와 수집일 metadata와 함께 18개 habitat 클래스 중 하나로 라벨링되어 있다. 클래스 분포는 매우 불균형해 Improved and Semi-Improved Grassland(IG)는 10,555장인 반면 Bare Soil, Silt and Peat(BSSP)는 224장이다. 전처리는 224×224 리사이즈와 ImageNet 통계 기반 normalisation을 적용했고, 학습셋에는 random horizontal flip, ±15° 회전, colour jittering, AutoAugment ImageNet policy를 사용했다. 클래스 불균형은 클래스당 학습 이미지를 1,000장으로 맞추는 방식으로 처리했으며, 과대 클래스는 무작위 subsampling, 과소 클래스는 augmentation으로 합성 확장했다. 모델은 ImageNet 사전학습된 DeepLabV3-ResNet101의 segmentation head를 1×1 convolution, global average pooling, flatten으로 교체하고 dropout 0.5를 적용한 transfer learning 구조이며, Cross-Entropy Loss와 AdamW(learning rate 1e-4, weight decay 1e-4), batch size 16, 최대 100 epoch, patience 7의 early stopping, mixed precision training과 gradient checkpointing을 사용해 five-fold cross-validation으로 평가했다.

## 결과

예비 실험의 InceptionV3 기반 모델은 최고 validation accuracy 44%, 평균 precision·recall·F1-score가 각각 0.40, 0.38, 0.39에 그쳤고 학습이 불안정했다. DeepLabV3-ResNet101 모델은 평균 validation accuracy 0.61, 평균 precision 0.63, recall 0.61, F1-score 0.61을 기록했으며 fold별 정확도는 약 59%에서 63% 사이였다. 클래스별로는 BSSP가 F1 0.91, Bare Sand(BS)와 Coniferous Woodland(CW)가 0.88, Water(WAT) 0.86, Built up areas and Gardens(BUAG) 0.83으로 높았고, Multiple 0.22, Unimproved Grassland(UG) 0.26, Fen, marsh and swamp(FMS) 0.39로 낮았다. Top-1 정확도는 59.0–63.0%였으나 Top-3 정확도는 78.0–80.1%로 올라가, 오답인 경우에도 정답이 상위 세 후보 안에 포함되는 경우가 많았다. confusion matrix에서는 BS와 BSSP·Coastal Sand Dunes(CSD), CW와 Broadleaved, Mixed and Yew Woodland(BMYW), UG와 Dwarf Shrub Heath(DSH) 사이의 혼동이 두드러졌다.

## 논의

RGB 지상 사진만으로도 시각적으로 뚜렷한 habitat은 상당한 정확도로 구분되지만, 전이대나 혼합 habitat은 클래스 내 변이와 경계 모호성 때문에 성능이 떨어진다. 저자들은 이런 오류의 상당 부분이 모델의 약점이 아니라 실제 생태적·시각적 모호성에서 비롯되며, multi-label 분류나 추가 metadata가 필요하다고 본다. 후속 방향으로 GPS 좌표, 고도, 토양 유형, 계절 지표 같은 맥락 정보의 통합과 Vision Transformer, ensemble learning, few-shot learning의 적용을 제시한다. 또한 EUNIS, CORINE, Living England 같은 서로 다른 분류 체계 사이의 변환 가능성을 확보해야 기존 생태 데이터·정책과 통합될 수 있다고 지적한다.

## 왜 읽을 만한가

위성영상 중심의 토지피복·habitat 매핑에 지상 사진이라는 보완 데이터원을 어떻게 결합할지 보여주는 사례다. 클래스별 F1과 혼동 패턴을 그대로 공개해, 생태 분류 과제에서 어떤 범주가 자동화의 한계에 부딪히는지 판단하는 데 참고가 된다.

## 원문 링크

- 원문: [https://arxiv.org/abs/2508.19314v1](https://arxiv.org/abs/2508.19314v1)
- PDF: [https://arxiv.org/pdf/2508.19314v1](https://arxiv.org/pdf/2508.19314v1)
