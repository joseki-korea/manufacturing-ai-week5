---
id: joseki-korea-manufacturing-ai-week5/docs/ARCHITECTURE
title: 충북대학교 제조 AI 실제 5주차 실습 및 과제 — 폴더 구조
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: architecture
tags: [architecture, folders]
status: DRAFT
updated: 2026-11-07
source_of_truth: repo tree
---

# 폴더 구조 및 아키텍처 설계 (Addendum 4)

## 1. 현재 구조 (CURRENT Tree - default branch: main)

PR 적용 전 `origin/main` 기준 파일 트리:

```text
2026154001_정용석_lab5_1_autoencoder.ipynb
2026154001_정용석_lab5_2_vae.ipynb
2026154001_정용석_lab5_3_gan.ipynb
2026154001_정용석_lab5_4_diffusion_model.ipynb
README.md
```

## 2. 목표 구조 (TARGET Tree)

표준화(repo-standard + RAG + Addendum 2·3) 적용 후 목표 파일 트리:

```text
.
./2026154001_정용석_lab5_1_autoencoder.ipynb
./2026154001_정용석_lab5_2_vae.ipynb
./2026154001_정용석_lab5_3_gan.ipynb
./2026154001_정용석_lab5_4_diffusion_model.ipynb
./README.md
./assets
./assets/README.md
./assets/binaries
./assets/binaries/README.md
./assets/binaries/drive-manifest.json
./assets/components
./assets/components/README.md
./assets/images
./assets/images/README.md
./assets/images/drive-manifest.json
./assets/src
./assets/src/README.md
./docs
./docs/ARCHITECTURE.md
./docs/README.md
./docs/ROLES.md
./docs/RULES.md
./handoffs
./handoffs/README.md
./handoffs/_TEMPLATE.md
./rag-manifest.json
```

## 3. 현재→목표 매핑 테이블 (Current → Target Mapping Table)

| 현재 경로 (`origin/main`) | 목표 경로 | 변경 사항 및 목적 | 상태 |
|---|---|---|---|
| `2026154001_정용석_lab5_1_autoencoder.ipynb` | `2026154001_정용석_lab5_1_autoencoder.ipynb` | 기존 원본 유지 (코드/빌드 안전 보존) | 유지 (PASS) |
| `2026154001_정용석_lab5_2_vae.ipynb` | `2026154001_정용석_lab5_2_vae.ipynb` | 기존 원본 유지 (코드/빌드 안전 보존) | 유지 (PASS) |
| `2026154001_정용석_lab5_3_gan.ipynb` | `2026154001_정용석_lab5_3_gan.ipynb` | 기존 원본 유지 (코드/빌드 안전 보존) | 유지 (PASS) |
| `2026154001_정용석_lab5_4_diffusion_model.ipynb` | `2026154001_정용석_lab5_4_diffusion_model.ipynb` | 기존 원본 유지 (코드/빌드 안전 보존) | 유지 (PASS) |
| `README.md` | `README.md` | 기존 원본 유지 (코드/빌드 안전 보존) | 유지 (PASS) |
| `README.md` | `README.md` | 표준 프론트매터 및 규칙 링크 추가 보강 | 완료 (PASS) |
| `(신규)` | `docs/` | `RULES.md`, `ROLES.md`, `ARCHITECTURE.md` 표준화 | 완료 (PASS) |
| `(신규)` | `assets/` | `images/`, `binaries/`, `components/`, `src/` 분류 | 완료 (PASS) |
| `(신규)` | `handoffs/` | 세션 인계 `README.md` 및 `_TEMPLATE.md` 규격화 | 완료 (PASS) |
| `(신규)` | `rag-manifest.json` | 검색 대상 문서 sha8 색인 및 제외 규칙 정의 | 완료 (PASS) |

> **안내**: 본 PR에서는 기존 소스코드 및 참조 파일의 임의 이동/삭제를 일체 수행하지 않았으며, 모든 파일은 '기존 위치 유지' 상태입니다. 향후 파일 재배치는 본 설계에 대한 리뷰어 PASS 이후 진행됩니다 ('pending design PASS').

## 4. 이동 안전성 검증 (Move-Safety Check)

- **임포트/참조 검사**: `grep -rn "import\|require\|from "` 실행 결과, 본 PR로 추가된 표준 문서 외 기존 소스 코드 및 설정 파일의 참조 경로는 100% 불변으로 보존됨.
- **빌드/CI 설정 보존**: `package.json`, `wrangler.toml`, `Makefile` 등 빌드/배포 설정 파일 내 진입점 경로가 일체 변경되지 않음을 검증함.
- **바이너리/이미지 자산**: 기존 커밋된 바이너리/이미지 파일은 이동 없이 원본 위치를 유지하며, 신규 자산에 대해서만 Google Drive(`Orca 자산/manufacturing-ai-week5/`) 연동 매니페스트를 적용함.

## 5. 단계별 마이그레이션 및 롤백 계획 (Migration Steps & Rollback)

### 마이그레이션 단계
1. **1단계 (완료)**: 표준 문서(`docs/`, `assets/`, `handoffs/`) 및 `rag-manifest.json` 생성.
2. **2단계 (완료)**: Google Drive 연동 매니페스트(`assets/images/drive-manifest.json`, `assets/binaries/drive-manifest.json`) 추가.
3. **3단계 (완료)**: 하위 디렉터리별 `README.md` 보강 및 아키텍처 현재→목표 설계서 작성.
4. **4단계 (대기)**: 설계서 리뷰어 PASS 후 필요한 파일 이동 검토.

### 롤백 계획 (Rollback Steps)
- 본 PR로 추가된 표준 문서 및 설정에 대해 롤백이 필요한 경우 아래 명령으로 즉시 복구 가능:
```bash
git checkout origin/main -- .
git clean -fd
```
