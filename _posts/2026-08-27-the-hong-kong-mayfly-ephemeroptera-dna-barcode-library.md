---
layout: post
title: "The Hong Kong mayfly (Ephemeroptera) DNA barcode library: Integrative taxonomy enables regional species inventories and highlights the effect of urbanization on species loss"
date: 2026-08-27 08:30:00 +0900
topic: "환경계획"
topic_key: "env-planning"
one_liner: "홍콩 하루살이 DNA barcode library를 구축하고 도시화에 따른 종 감소를 확인한 연구다."
authors: "Kwan Wong, Wu Han, Chuming Zhang, Hin Fat Tsang, Zhewei Si, Xiaoli Tong, Mathew Seymour"
venue: "Metabarcoding and Metagenomics"
published: "2026-08-12"
doi: "https://doi.org/10.3897/mbmg.10.199829"
paper_url: "https://doi.org/10.3897/mbmg.10.199829"
pdf_url: "https://mbmg.pensoft.net/article/199829/download/pdf/"
source: "openalex"
basis: "full_text"
keywords:
  - "DNA barcoding"
  - "COI"
  - "integrative taxonomy"
  - "eDNA metabarcoding"
  - "urbanization gradient"
  - "freshwater biomonitoring"
paper_keywords:
  - "Biodiversity"
  - "biomonitoring"
  - "China"
  - "COI"
  - "environmental DNA (eDNA)"
  - "integra- tive taxonomy"
  - "land use"
figure: "/assets/figures/2026-08-27-the-hong-kong-mayfly-ephemeroptera-dna-barcode-library.png"
---

## 한 줄 요약

**홍콩 하루살이 DNA barcode library를 구축하고 도시화에 따른 종 감소를 확인한 연구다.**

![원문 대표 그림]({{ '/assets/figures/2026-08-27-the-hong-kong-mayfly-ephemeroptera-dna-barcode-library.png' | relative_url }})

*원문에서 발췌 — Kwan Wong 외, Metabarcoding and Metagenomics, 2026. [CC-BY](https://creativecommons.org/licenses/) 라이선스.*

## 초록 요약

홍콩의 자연-도시화 gradient를 따라 30개 하천에서 하루살이(Ephemeroptera) nymph를 채집했다. 형태 동정과 COI barcoding을 결합한 integrative taxonomy로 45개 morphospecies를 구분하고, 146개 barcode 서열과 53개 BIN으로 구성된 지역 최초의 DNA barcode reference library를 만들었다. 53개 BIN 중 67.3%가 BOLD에 새로 등록됐고, 미기재 추정 lineage 7개와 지역 신기록 4종이 포함됐다. 종 풍부도는 urban intensity(β = –0.308, p = 0.007)와 conductivity(β = –0.427, p = 0.002)가 높아질수록 유의하게 감소했다.

## 주요 차별성

- 홍콩, 나아가 중국 남부 지역에서 하루살이를 대상으로 한 최초의 COI DNA barcode reference library를 구축했다.
- 형태 기반 morphospecies 구분과 BOLD의 BIN 할당을 교차 검증하는 integrative taxonomy 절차를 6가지 판정 규칙으로 명시했다.
- 기존 홍콩 하루살이 연구가 자연 상태의 headwater에 한정됐던 것과 달리, 자연-peri-urban-도시 전 구간의 land use gradient를 다뤘다.
- barcode library 구축과 urbanization 영향 평가, indicator species 탐색을 하나의 데이터셋에서 동시에 수행했다.

## 주요 기여점

- 146개 barcode(평균 626 bp), 53개 BIN, voucher 사진과 trace file을 BOLD에 공개 데이터셋(DS-HKMAYFLY)으로 등록했다.
- 지역 신기록 4종과 미기재 추정 lineage 7개를 보고해 홍콩 checklist를 14% 확장했다.
- urbanization과 conductivity가 하루살이 richness를 낮추는 주요 환경 필터임을 negative binomial GLM으로 정량화했다.
- land use 등급별 indicator species를 제시해 eDNA metabarcoding 기반 biomonitoring의 참조 자료를 마련했다.

## 연구의 배경

담수 생물다양성은 도시화와 서식지 변형으로 빠르게 감소하고 있으며, 동남아시아는 정확한 종 목록 자체가 부족하다. 하루살이는 어류·조류의 먹이원이자 수질 biomonitoring 지표로 쓰이는 대형 저서 무척추동물이다. 홍콩은 인구밀도가 매우 높지만 영토의 약 70%가 미개발 상태여서, 좁은 범위 안에 뚜렷한 자연-도시화 gradient가 존재한다.

## 필요성

중국의 하루살이 유전 정보는 공개 저장소에서 학명과 연결되지 않은 채 흩어져 있어 taxonomic impediment가 크다. 홍콩의 하루살이 목록은 Tong(2001)의 56종 기록 이후 갱신되지 않았고, cryptic diversity를 판별할 barcode reference library도 없었다. 참조 서열이 없으면 eDNA metabarcoding 같은 분자 기반 biomonitoring의 종 동정 정확도가 확보되지 않는다.

## 목적

integrative taxonomy로 홍콩 하루살이의 공개 COI barcode library를 구축하는 것이 목적이다. 아울러 도시화와 하루살이 생물다양성의 관계를 평가하고 land use 등급별 indicator species를 찾고자 했다.

## 방법론

2022년 9월 22개 지점과 2023년 11월 30개 지점에서 D-frame kick net(500 μm)으로 3분간 표준화된 kick sampling을 수행해 nymph를 채집했다. 각 지점은 반경 100 m 내 land use 조성을 2023년 Land Utilization Raster Grids(Hong Kong Planning Department)로 분석해 natural, peri-urban, urbanized 세 등급으로 분류했고, pH·conductivity·dissolved oxygen·TDS를 U-50 HORIBA 다항목 측정기로 현장 측정했다. 형태 동정 후 morphospecies당 2~5개체에서 DNA를 추출해 658 bp COI 영역을 LCO1490/HCO2198 및 이 연구에서 설계한 MayF1/R1, MayF2/R2 primer로 증폭하고 Sanger sequencing했다. 서열은 BOLD의 RESL 알고리즘으로 BIN을 할당하고, MEGA 12에서 Kimura-2-Parameter 거리와 1,000회 bootstrap의 neighbor-joining tree로 barcode gap과 monophyly를 확인했으며 GenBank BLAST 95% 유사도를 진단 기준으로 병행했다. 환경 요인 분석은 R v4.5.1의 glmmTMB로 negative binomial GLM을 적합해 VIF > 5 변수 제거와 backward selection을 거쳤고, indicator species는 indicspecies 패키지의 IndVal로 α = 0.05에서 검정했다.

## 결과

30개 하천에서 12,155개체를 채집해 6과 28속 45개 morphospecies를 확인했으며, ACE 추정 지역 종 풀 52종 대비 약 86.5%를 포착했다. 추출한 207개체에서 154개 COI 서열을 얻었고 이 중 146개(94.8%)가 53개 BIN에 할당됐으며, 53개 BIN의 67.3%가 BOLD 신규 기록이었다. 종간 최소 유전 거리 평균은 22.4%, 종내 최대 유전 거리 평균은 1.4%로 뚜렷한 barcode gap이 나타났고, 2.2% 기준을 넘은 분류군은 Bungona fusina(2.8%), Paegniodes cupulatus(4.7%), Isca purpurea(8.2%) 세 종이었다. 종 풍부도는 지점별 최대 26종에서 0종까지(평균 9종) 변했고, urbanization(β = –0.308, p = 0.007)과 conductivity(β = –0.427, p = 0.002)에서 유의한 음의 효과가, elevation(β = –0.210, p = 0.051)에서는 한계 수준의 효과가 확인됐다. IndVal 분석에서는 Choroterpes elliptica HK01이 natural 지점, Tenuibaetis pseudofrequentus와 Caenis lubrica가 peri-urban 지점의 지표종으로 나타났고 urbanized 지점의 지표종은 없었다.

## 논의

conductivity의 효과 크기가 가장 컸다는 점은 도시 유출수와 하수 유입에 따른 이온 오염이 하루살이 군집을 거르는 핵심 환경 필터임을 시사한다. urbanized 지점에서 지표종이 전혀 나오지 않은 것은 민감종과 중간 내성종 모두가 내성 한계를 넘어, 소수의 generalist 중심으로 군집이 단순화되는 biotic homogenization 과정으로 해석된다. 저자들은 658 bp COI 단독으로는 깊은 계통 관계를 해상할 수 없어 Labiobaetis-Bungona-Baetis 복합군의 비단계통 결과가 미해결 계통과 불완전한 표본 추출에서 비롯됐을 수 있다고 보고, multi-marker phylogenomic 재구성이 필요하다고 밝힌다. 또한 시공간 범위가 더 넓은 조사가 있어야 군집 변화 해석을 일반화할 수 있다는 점을 한계로 인정한다.

## 왜 읽을 만한가

도시화 gradient를 land use 조성으로 정량화해 생물다양성 반응을 연결하는 설계가 환경계획·도시계획 연구에 그대로 응용된다. 지역 reference library 없이는 eDNA 기반 모니터링이 성립하지 않는다는 점을 수치로 보여주는 사례다.

## 원문 키워드

`Biodiversity`, `biomonitoring`, `China`, `COI`, `environmental DNA (eDNA)`, `integra- tive taxonomy`, `land use`

## 원문 링크

- 원문: [https://doi.org/10.3897/mbmg.10.199829](https://doi.org/10.3897/mbmg.10.199829)
- PDF: [https://mbmg.pensoft.net/article/199829/download/pdf/](https://mbmg.pensoft.net/article/199829/download/pdf/)
- DOI: [https://doi.org/10.3897/mbmg.10.199829](https://doi.org/10.3897/mbmg.10.199829)
