---
layout: page
title: 소개
permalink: /about/
---

**Daily Paper**는 매일 아침 8시 30분(KST)에 논문 한 편을 골라 한국어로 요약해 게시하는
자동화 사이트입니다. 출근길에 3~5분 안에 읽을 수 있는 분량을 목표로 합니다.

## 다루는 주제

여덟 개 주제를 하루씩 순환합니다.

| 주제 | 범위 |
| --- | --- |
| GeoAI | geospatial artificial intelligence, spatial deep learning |
| GeoXAI | explainable / interpretable AI in geospatial contexts |
| 환경계획 | environmental planning, land use planning, ecosystem services |
| 도시계획 | urban planning, urban form, built environment, smart city |
| 탄소중립 | carbon neutrality, net-zero, decarbonization pathways |
| 탄소저감 | emission reduction, carbon sequestration, carbon sink |
| GIS | geographic information systems, spatial analysis, spatial statistics |
| Remote Sensing | satellite imagery, earth observation, land cover |

해당 주제에 새 논문이 없으면 다음 주제로 넘어가므로, 매일 한 편이 보장됩니다.

## 논문 수집 방식

세 개의 공개 학술 API에서 후보를 모읍니다.

- **arXiv** — GeoAI·Remote Sensing 계열 preprint, 전문 접근이 용이합니다.
- **OpenAlex** — 저널 게재논문 전반, open access PDF 링크를 제공합니다.
- **Crossref** — 위 두 소스를 보완합니다.

주제 관련도, 발행 최신성, 초록 충실도, 전문 접근 가능 여부를 합산해 점수가 가장 높은
미게시 논문을 선정합니다. 이미 게시한 논문은 DOI · arXiv ID · 제목 해시로 걸러냅니다.

> **Google Scholar 추천 논문은 연동하지 않습니다.** 공개 API가 없고 추천 피드는 개인
> 로그인 세션을 요구하므로 자동화가 불가능합니다. 대신 위 키워드 기반 수집으로 대체합니다.

## 요약 방식

Anthropic의 **Claude Opus 5**가 요약을 생성합니다. Open access PDF를 확보한 경우 논문
전문을 근거로 요약하고, 그렇지 않으면 초록만으로 요약한 뒤 각 글 상단에 근거를 명시합니다.

각 글은 다음 순서로 구성됩니다.

한 줄 요약 → 초록 요약 → 주요 차별성 → 주요 기여점 → 연구의 배경 → 필요성 → 목적 →
방법론 → 결과 → 논의 → 왜 읽을 만한가

서술은 한국어로 하되, 학계에서 통용되는 전문 용어(예: Random Forest, NDVI, Sentinel-2,
SHAP, urban heat island)는 영어 원문 그대로 표기합니다.

## 주의사항

요약은 자동 생성물이며 원문의 뉘앙스나 세부 조건을 놓칠 수 있습니다.
**인용하거나 연구에 활용하기 전에는 반드시 원문을 직접 확인하세요.**
특히 "요약 근거: 초록"으로 표시된 글은 방법론과 결과의 세부 사항이 제한적입니다.

## 문의

[GitHub 저장소]({{ site.repository | prepend: 'https://github.com/' }})에 이슈를 남겨 주세요.
