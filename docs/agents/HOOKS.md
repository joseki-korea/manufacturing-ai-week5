---
id: "manufacturing-ai-week5/docs/agents/HOOKS"
title: "훅 목록 (실측)"
summary: "이 저장소에 실제로 있는 훅 목록, 없음 실측 결과, 안전한 추가 방법"
domain: "manufacturing-ai-week5"
tags: ["agents", "hooks"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "대표 지시 2026-11-08 멀티에이전트 핸드오프·janitor·watchdog·훅 (D2)"
lang: "ko"
sensitivity: "internal"
related: ["docs/agents/handoffs/README.md", "docs/agents/ROLE-watchdog.md", "docs/agents/ROLE-janitor.md"]
---

# 훅 목록 (실측)

이 문서는 이 저장소에 **실제로 있는** 훅만 적는다. 기준은 `2026-11-08` 시점의 PR 브랜치 추적 파일이다.

## 실측 결과

| 종류 | 확인한 위치 | 결과 |
|---|---|---|
| Claude Code | `.claude/settings*.json`의 `hooks` | 없음(실측) |
| Codex | `.codex/` | 없음(실측) |
| git | `.githooks/`, `.husky/`, `core.hooksPath`, `.pre-commit-config.yaml`, `lefthook.yml` | 없음(실측) |
| CI | `.github/workflows/` | 없음(실측) |
| package.json | `prepare`, `precommit`, `pre-commit`, `pre-push`, `postinstall` | 없음(실측) |

`package.json`의 `build`·`test` 같은 스크립트는 훅이 아니므로 위 목록에 넣지 않는다.

## 목록

- 없음(실측)

## 추가 방법 (안전)

1. 먼저 이 문서에 계획을 적는다: 이름, 시점(언제 실행되는지), 하는 일, 실패 시 동작(차단 또는 경고).
2. 훅은 검사·읽기 위주로 만든다. 파일 변경과 네트워크 호출은 최소로 한다.
3. 비밀·토큰·키를 훅 파일에 넣지 않는다.
4. 되돌리기 방법을 적는다. 예: 설정 한 줄 제거 또는 훅 파일 삭제로 즉시 끈다.
5. 로컬에서 한 번 실행해 결과를 확인한 뒤 PR에 올린다.
6. 올린 뒤 이 문서의 "목록"에 반영한다.

## 안전 규칙

- 비밀 금지
- 네트워크 최소
- 되돌리기 가능
- 사용자 파일 수정 금지 (검사만)
