---
id: "manufacturing-ai-week5/docs/ARCHITECTURE.md"
title: "Repository Architecture and Current->Target Migration Plan"
repo: joseki-korea/manufacturing-ai-week5
device_scope: all
doc_type: architecture
tags:
  - architecture
  - current-target-tree
  - migration-plan
status: DRAFT
updated: '2026-11-07'
source_of_truth: "docs/ARCHITECTURE.md"
---

# Repository Architecture — manufacturing-ai-week5

본 문서는 `joseki-korea/manufacturing-ai-week5` 레포지토리의 아키텍처 폴더 트리 설계 및 Current→Target 구조를 정의합니다.

## 1. 프로젝트 개요
- **레포지토리**: `joseki-korea/manufacturing-ai-week5`
- **기본 브랜치**: `main`
- **작업 브랜치**: `repo-standard-20261107`
- **목적**: 표준화된 RAG 및 멀티에이전트 협업 체계 수립 (REPO-STANDARD-ALL-20261107)

## 2. CURRENT 트리 (기본 브랜치 `origin/main`, depth ≤ 3)
기본 브랜치 기준 기존 루트 파일 및 폴더 구조:

### 2.1. 루트 추적 파일 (Tracked Root Files)
- `2026154001_정용석_lab5_1_autoencoder.ipynb`
- `2026154001_정용석_lab5_2_vae.ipynb`
- `2026154001_정용석_lab5_3_gan.ipynb`
- `2026154001_정용석_lab5_4_diffusion_model.ipynb`
- `README.md`

### 2.2. 디렉토리 구조 (Directory Tree)
- *(루트 레벨 디렉토리 없음)*

## 3. TARGET 트리 (목표 아키텍처 폴더 구조, depth ≤ 3)
Repo Standard 적용 후 목표 폴더 구조 (추적 대상 파일 기준, `__pycache__` 등 임시 파일 전면 배제):

### 3.1. 루트 추적 및 설정 파일 (Tracked Root & App Config Files)
- `.gitignore`
- `2026154001_정용석_lab5_1_autoencoder.ipynb`
- `2026154001_정용석_lab5_2_vae.ipynb`
- `2026154001_정용석_lab5_3_gan.ipynb`
- `2026154001_정용석_lab5_4_diffusion_model.ipynb`
- `README.md`
- `rag-manifest.json`

### 3.2. 디렉토리 구조 (Directory Tree)
- `assets/`
- `assets/binaries/`
- `assets/components/`
- `assets/images/`
- `assets/src/`
- `assets/videos/`
- `docs/`
- `handoffs/`

## 4. Current → Target 매핑 테이블
기존 위치에서 목표 위치로의 매핑 및 상태:

| 원본 경로 (Current) | 목표 경로 (Target) | 진행 상태 |
|---|---|---|
| *(모든 기존 소스/리소스 파일)* | *(기존 위치 100% 동일 유지)* | **원위치 유지** (설계 검토 PASS 전 파일 이동 전면 중단 원칙 준수) |

> **안내**: 설계 검토(Reviewer PASS) 완료 전 사전 파일 이동이 금지됨에 따라, 이전에 임시 스테이징되었던 모든 기존 파일은 `git mv back`을 통해 원상 복구(Original Location)되었습니다.

## 5. 이동 안정성 검증 (Move-Safety Check & Grep Evidence)
- **파일 이동 상태**: 현재 브랜치에서 이동된 기존 소스코드가 일체 존재하지 않음 (`0 moves active`).
- **런타임 의존성**: 모든 기존 파일이 원래 위치에 보존되어 있으므로 `import`, `require`, 빌드 설정(CI/CD) 영향도 0% (완전 무결).

## 6. 마이그레이션 절차 및 롤백 계획 (Migration Steps & Rollback)
### 6.1. 마이그레이션 실행 절차
1. **설계 사전 검토**: 본 아키텍처 구조에 대해 리뷰어 승인(PASS)을 획득합니다.
2. **단독 git mv 수행**: 승인된 대상에 한해 비즈니스 로직 수정 없이 `git mv` 단독 커밋으로 수행합니다.
3. **참조 갱신**: 상대 경로 import 및 README 링크를 동기화합니다.
4. **빌드/테스트 검증**: 단위 테스트 및 빌드 스크립트를 실행하여 무결성을 최종 검증합니다.

### 6.2. 롤백 계획
현재 활성화된 파일 이동이 없으므로(`git diff -M --summary origin/main` 상 rename 0건), 추가적인 롤백 조치가 불필요합니다.

## 7. 설계 승인 원칙 (Design PASS Rule)
CEO 지침에 따라 본 설계 문서가 리뷰어의 최종 PASS 승인을 받기 전까지는 **일체의 파일 이동(`git mv`)이 엄격히 금지**됩니다.
