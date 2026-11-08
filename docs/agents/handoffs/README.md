---
id: "manufacturing-ai-week5/docs/agents/handoffs/README"
title: "핸드오프 규칙"
summary: "멀티에이전트 세션 간 인계 파일의 이름·원칙·ACK·archive 절차"
domain: "manufacturing-ai-week5"
tags: ["agents", "handoff"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "대표 지시 2026-11-08 멀티에이전트 핸드오프·janitor·watchdog·훅 (D2)"
lang: "ko"
sensitivity: "internal"
related: ["docs/agents/handoffs/TEMPLATE.md", "docs/agents/ROLE-janitor.md", "RULES.md"]
---

# 핸드오프 규칙

이 폴더는 멀티에이전트 세션끼리 작업을 넘길 때 쓰는 기록 공간이다. 받은 사람이 같은 맥락으로 바로 이어받을 수 있게 남기는 것이 목적이다.

## 파일 이름

- 형식: `YYYYMMDD-HHMM-<from>-to-<to>-<topic>.md`
- `<from>`, `<to>`: 역할 이름 (예: `claude`, `codex`, `antigravity`, `janitor`, `watchdog`)
- `<topic>`: 소문자 영문·숫자·하이픈
- 예: `20261108-1430-claude-to-codex-docs-review.md`

## 원칙

1. **append-only**: 한 번 쓴 내용은 고치거나 지우지 않는다. 정정은 아래에 새 줄로 덧붙인다.
2. **ACK**: 받은 쪽이 파일 끝에 ACK 줄을 추가한다.
   - 형식: `ACK: [serial4][sess4][model][role] YYYY-MM-DD HH:MM — 확인`
3. **archive**: 작업이 끝나면 `active/`에서 `archive/`로 옮긴다 (`git mv`).
4. **근거 표기**: `경로#줄 @sha8` 형식으로 적는다.
5. **비밀 금지**: 비밀번호·토큰·키·계정 정보는 평문으로 적지 않는다.
6. **한 파일 한 인계**: 여러 주제를 한 파일에 섞지 않는다.

## 폴더

- `active/`: 진행 중이거나 ACK를 기다리는 인계
- `archive/`: 완료된 인계 (정리 담당이 이동한다. [정리 담당](../ROLE-janitor.md) 참고)

## 절차

1. `TEMPLATE.md`를 복사해 `active/`에 새 파일을 만든다.
2. 작업 브랜치에서 커밋·푸시한다. `main`에 직접 병합하지 않는다.
3. 받은 쪽이 ACK 줄을 추가하고 커밋한다.
4. 완료되면 `archive/`로 옮긴다.
