---
id: joseki-korea-manufacturing-ai-week5/docs/ROLES
title: 충북대학교 제조 AI 실제 5주차 실습 및 과제 — 세션 역할
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: roles
tags: [roles, sessions]
status: DRAFT
updated: 2026-11-07
source_of_truth: vault main rules/INDEX.md (Rule 01)
---

# 세션 역할

## 관제 및 모니터링 세션 (Claude 전용)

Claude는 관제·모니터링 및 라우팅 전용 세션입니다. 직접 코드를 구현하지 않고 전체 작업 배차, 진행 점검, 맥락 관리 및 상위 보고를 전담합니다.

- **PM 세션 (Claude)**: 작업을 쪼개 배차하고 진행을 점검하며 기획, 설계, 검증 및 상위 보고(허브)를 담당합니다.
- **Janitor 세션 (Claude)**: 맥락 과적 방지 와치독 전용으로, 세션 맥락 사용량 30% 도달 시 핸드오프 작성과 `/clear`를 요청합니다.

## 작업 세션 (Codex Terra / Antigravity 전용)

작업 세션은 PM이 배정한 한 가지 구현/리팩터링 작업만 독립된 워크트리에서 수행합니다. Claude(Sonnet/Haiku 포함)는 작업 세션에서 완전히 제외되며 작업 실행기는 아래 2종만 허용됩니다.

| 실행기 | 용도 |
|---|---|
| Antigravity (AGY) | 주 실행. 격리 워크트리에서 작업 |
| Codex Terra | 코드 작업·리팩터 |

작업 세션 불변식:
- 격리된 워크트리에서만 작업하며 main 직접 push 및 force push를 절대 하지 않는다.
- 기존 코드 임의 삭제 및 비밀(token/key/password) 취급을 금지한다.
- 작업 완료 시 결과 경로와 sha8을 관제 세션(PM)에 보고한다.

## janitor 세션

janitor는 맥락 과적 방지 와치독 전용이다. 다른 작업은 하지 않는다.

- 세션 맥락 사용량이 30%에 도달하면 해당 세션에 핸드오프 작성과 `/clear`를 요청한다.
- 핸드오프 파일은 `handoffs/`에 규칙대로 남긴다.
- 코드 수정·배포·보고 등 그 외 작업은 금지한다.
