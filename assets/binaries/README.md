---
id: joseki-korea-manufacturing-ai-week5/assets/binaries/README
title: "바이너리 에셋"
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: asset-index
tags: [assets, binaries]
status: DRAFT
updated: 2026-11-07
source_of_truth: docs/ARCHITECTURE.md
---

# assets/binaries/

## 목적

바이너리 파일 보관 안내 및 Google Drive 연동. 실파일은 git에 직접 커밋하지 않고 Google Drive와 연동하여 관리한다.

## Google Drive 연동 경로

- Google Drive 경로: `Orca 자산/manufacturing-ai-week5/binaries`
- 동기화 담당: `login-context-cards` 기준 유효한 Google Drive 로그인이 유지된 기기에서 수행.
- 신규 파일 전용 동기화 (기존 git 추적 파일은 보존).
- 메타데이터 색인: `drive-manifest.json`

## 이름 규칙

`<이름>-<버전>.<확장자>`. 이 폴더엔 README, drive-manifest.json 및 색인 md만 커밋한다.

## 넣으면 안 되는 것

비밀, 토큰, 키, 개인정보, 계정 정보. 대용량·서명·라이선스 제한 파일 직접 커밋. RAG 수집에서도 제외된다.
