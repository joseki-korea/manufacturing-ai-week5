---
id: "joseki-korea-manufacturing-ai-week5/assets/videos/README"
title: "비디오 에셋"
repo: "joseki-korea-manufacturing-ai-week5"
device_scope: all
doc_type: asset-index
tags: ["assets", "videos", "drive"]
status: DRAFT
updated: 2026-11-07
source_of_truth: "docs/ARCHITECTURE.md"
---

# assets/videos/

## 목적

프로젝트 비디오/영상 에셋 안내 및 Google Drive 연동. 영상 파일 실물은 git에 직접 커밋하지 않고 Google Drive와 연동하여 관리한다.

## Google Drive 연동 경로

- Google Drive 경로: `Orca 자산/manufacturing-ai-week5/videos`
- 동기화 담당: `login-context-cards` 기준 유효한 Google Drive 로그인이 유지된 기기에서 수행.
- 신규 파일 전용 동기화 (기존 git 추적 파일은 보존).
- 업로드 시 파일 크기(size) 및 SHA-256 검증 필수.
- 덮어쓰기(overwrite), 삭제(delete), 공유 권한 변경(sharing change) 절대 금지.
- 메타데이터 색인: `drive-manifest.json`

## 이름 규칙

`kebab-case.<ext>` (예: `demo-walkthrough.mp4`). 각 영상마다 설명 md 파일을 둘 수 있다.

## 넣으면 안 되는 것

비밀, 토큰, 키, 개인정보, 계정 정보. 대용량 원본 파일의 git 직접 커밋.
