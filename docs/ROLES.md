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

## PM 세션

PM 세션은 작업을 쪼개 배차하고 진행을 점검한다. 라우팅과 기획만 하며 직접 코드를 수정하지 않는다. 결과 검증과 상위 보고(허브)를 맡는다.

## 작업 세션

작업 세션은 PM이 배정한 한 가지 작업만 수행한다. 허용 실행기는 다음과 같다.

| 실행기 | 용도 |
|---|---|
| Antigravity (AGY) | 주 실행. 격리 워크트리에서 작업 |
| Codex Terra | 코드 작업·리팩터 |
| Claude Haiku | 가벼운 기계적 작업 |

작업 세션은 격리된 워크트리에서만 작업하고, 삭제·force push·main 변경·비밀 취급을 하지 않는다. 완료 시 결과 경로와 sha8을 PM에 보고한다.

## janitor 세션

janitor는 맥락 과적 방지 와치독 전용이다. 다른 작업은 하지 않는다.

- 세션 맥락 사용량이 30%에 도달하면 해당 세션에 핸드오프 작성과 `/clear`를 요청한다.
- 핸드오프 파일은 `handoffs/`에 규칙대로 남긴다.
- 코드 수정·배포·보고 등 그 외 작업은 금지한다.
