---
id: joseki-korea-manufacturing-ai-week5/assets/images/README
title: 이미지 에셋
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: asset-index
tags: [assets, images]
status: DRAFT
updated: 2026-11-07
source_of_truth: docs/ARCHITECTURE.md
---

# assets/images/

## 목적

프로젝트 문서·화면에 쓰는 이미지 보관 및 Google Drive 연동.

## Google Drive 연동 경로

- Google Drive 경로: `Orca 자산/manufacturing-ai-week5/images`
- 동기화 담당: `login-context-cards` 기준 유효한 Google Drive 로그인이 유지된 기기에서 수행.
- 신규 파일 전용 동기화 (기존 git 추적 파일은 보존).
- 메타데이터 색인: `drive-manifest.json`

## 이름 규칙

`kebab-case.png`. 이미지마다 같은 이름의 `.md` 설명 파일(alt-text + 캡션)을 둔다. 검색(RAG)은 이 설명 파일로 한다.

## 넣으면 안 되는 것

비밀, 토큰, 키, 개인정보, 계정 정보. 사람 얼굴 등 개인정보 사진. 대용량 원본.
