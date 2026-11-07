---
id: "manufacturing-ai-week5/ARCHITECTURE.md"
title: "Repository Architecture Pointer"
repo: "joseki-korea/manufacturing-ai-week5"
device_scope: "all"
doc_type: "architecture"
tags:
  - "architecture"
  - "pointer"
status: "DRAFT"
updated: "2026-11-07"
source_of_truth: "docs/ARCHITECTURE.md"
---

# Repository Architecture — manufacturing-ai-week5

본 문서는 `joseki-korea/manufacturing-ai-week5` 레포지토리의 아키텍처 및 디렉토리 구조에 대한 상위 요약 및 포인터입니다.

## 1. 아키텍처 요약
- **핵심 역할**: 충북대학교 제조 AI 실제 5주차 실습 및 과제 저장소.
- **주요 구성**:
  - `docs/`: 표준 규칙, 멀티에이전트 역할, 아키텍처 설계 및 마이그레이션 계획.
  - `docs/agents/`: Claude, Codex Terra, Antigravity 에이전트별 전담 역할 및 행동 강령.
  - `assets/`: 이미지, 바이너리, 비디오 및 UI 컴포넌트 관리.
  - `handoffs/`: 세션 인수인계 기록 보관소.

## 2. 정본 문서 안내
상세한 디렉토리 레이아웃, Current→Target 매핑, 시맨틱 재구성 설계 및 롤백 계획은 아래 정본 문서를 참고하십시오:
👉 **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**
