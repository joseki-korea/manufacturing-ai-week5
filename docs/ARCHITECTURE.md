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

# 폴더 구조

## 폴더 트리

기존 코드 폴더는 그대로 두고 아래 표준 폴더만 필요한 만큼 추가한다. 실제 트리로 채운다.

```text
.
./2026154001_정용석_lab5_1_autoencoder.ipynb
./2026154001_정용석_lab5_2_vae.ipynb
./2026154001_정용석_lab5_3_gan.ipynb
./2026154001_정용석_lab5_4_diffusion_model.ipynb
./README.md
./assets
./assets/binaries
./assets/components
./assets/images
./assets/src
./docs
./docs/ROLES.md
./docs/RULES.md
./handoffs
```

## 표준 폴더와 목적

| 폴더 | 목적 | 넣으면 안 되는 것 |
|---|---|---|
| `docs/` | 규칙·역할·구조 문서 | 비밀, 생성 산출물 |
| `handoffs/` | 에이전트 세션 핸드오프 노트(파일당 1건) | 비밀, 전체 로그 |
| `assets/images/` | 이미지 + alt-text/캡션 md | 개인정보 사진, 대용량 원본 |
| `assets/src/` | 소스코드 조각·스니펫 | 앱 본체 코드, 비밀 |
| `assets/components/` | 재사용 컴포넌트 | 빌드 산출물 |
| `assets/binaries/` | 바이너리 안내(실파일은 .gitignore 또는 LFS) | 비밀, 대용량 파일 커밋 |

## 기존 폴더 설명

| 폴더/경로 | 설명 |
|---|---|
| 루트 (`/`) | 제조 AI 5주차 실습 노트북(Autoencoder, VAE, GAN, Diffusion) 및 프로젝트 문서 |
