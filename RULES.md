---
id: "manufacturing-ai-week5/RULES.md"
title: "Repository Global Rules Pointer"
repo: "joseki-korea/manufacturing-ai-week5"
device_scope: "all"
doc_type: "rules"
tags:
  - "rules"
  - "pointer"
status: "DRAFT"
updated: "2026-11-07"
source_of_truth: "docs/RULES.md"
---

# Repository Global Rules — manufacturing-ai-week5

본 문서는 `joseki-korea/manufacturing-ai-week5` 레포지토리 전역에서 준수해야 할 개발 및 세션 운영 규칙 포인터입니다.

## 1. 핵심 전역 규칙 요약
1. **기획 우선 및 설계 검토 통과 원칙**: 사전 승인 없는 임의 파일 이동(`git mv`) 및 파괴적 변경 절대 금지.
2. **세션 위생 및 30% 핸드오프**: 컨텍스트 30% 도달 시 `handoffs/`에 인수인계 기록 작성 후 정리.
3. **비밀정보 보호 (Zero Secret Leaks)**: API 키, 토큰, 환경변수 파일(.env)의 커밋 절대 금지.
4. **엄격한 다중 에이전트 검증**: Strict Mode 90점 이상 획득 시에만 배포/머지 단계 진입.

## 2. 정본 문서 안내
프로젝트 전용 상세 개발 수칙, Git 워크플로우 및 테스트 가이드는 아래 정본 문서를 참고하십시오:
👉 **[docs/RULES.md](docs/RULES.md)**
