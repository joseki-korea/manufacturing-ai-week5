---
id: "manufacturing-ai-week5/docs/ASSET-MAP.md"
title: "Asset Mapping and Semantic Migration Plan"
repo: "joseki-korea/manufacturing-ai-week5"
device_scope: "all"
doc_type: "architecture"
tags:
  - "architecture"
  - "assets"
  - "semantic-reorg"
status: "DRAFT"
updated: "2026-11-07"
source_of_truth: "docs/ASSET-MAP.md"
---

# Asset Mapping & Semantic Reorganization Plan — manufacturing-ai-week5

본 문서는 `joseki-korea/manufacturing-ai-week5` 레포지토리의 소스코드 및 에셋을 기능/모듈별로 시맨틱하게 재구성하기 위한 이동 계획 설계 테이블입니다.
**주의: 본 계획은 설계 단계(DESIGN ONLY)이며, 3자 검토자(Reviewer) PASS 이전까지는 실제 `git mv` 이동 작업을 일절 수행하지 않습니다 (0 moves executed).**

## 1. 시맨틱 이동 계획 테이블 (Semantic Move Plan Table)

| 원본 경로 (Source) | 목표 경로 (Target) | 모듈 성격 및 목적 | 진행 상태 |
|---|---|---|---|
| `2026154001_[author]_lab5_1_autoencoder.ipynb` | `src/autoencoders/lab5_1_autoencoder.ipynb` | Autoencoder 이상치 탐지 실습 모듈 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `2026154001_[author]_lab5_2_vae.ipynb` | `src/vae/lab5_2_vae.ipynb` | Variational Autoencoder 생성 실습 모듈 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `2026154001_[author]_lab5_3_gan.ipynb` | `src/gan/lab5_3_gan.ipynb` | GAN 이미지 생성 모델 실습 모듈 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `2026154001_[author]_lab5_4_diffusion_model.ipynb` | `src/diffusion/lab5_4_diffusion_model.ipynb` | 확산 모델(DDPM) 역방향 노이즈 예측 실습 모듈 | **PLANNED (DESIGN ONLY — 0 executed)** |

## 2. 참조 갱신 계획 (Reference-Update Plan)
- **임포트 및 링크 동기화**: 설계 승인 후 대상 파일 이동 시, 소스코드 내 상대 경로 및 문서 간 하이퍼링크를 단독 커밋으로 일괄 갱신합니다.
- **런타임 의존성 보존**: 빌드 도구 및 웹팩/번들러 설정이 `src/` 및 `assets/ui-components/`를 올바르게 인식하도록 설정 동기화를 선행합니다.

## 3. 빌드 및 테스트 검증 계획 (Build/Test Verification)
- 각 단계별 파일 이동 후 즉시 단위 테스트 및 빌드 스크립트를 수행하여 회귀 결함 0건을 확인합니다.
