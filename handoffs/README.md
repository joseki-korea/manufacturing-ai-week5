---
id: joseki-korea-manufacturing-ai-week5/handoffs/README
title: 핸드오프 폴더 안내
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: handoff
tags: [handoff, sessions]
status: DRAFT
updated: 2026-11-07
source_of_truth: docs/ROLES.md
---

# handoffs/

## 목적

에이전트 세션이 /clear 또는 교체되기 전에 다음 세션이 이어받을 정보를 남기는 폴더이다.

## 규칙

- 파일 하나에 핸드오프 한 건. 이름은 `YYYYMMDD-<session4>-<topic>.md`.
- append-only. 기존 파일은 수정하지 않고 새 파일을 추가한다.
- 맨 위 frontmatter에 session id, device, date, status를 적는다. 템플릿은 `_TEMPLATE.md`.
- 비밀·토큰·계정 ID·개인정보·전체 로그를 넣지 않는다. 경로와 sha8만 적는다.
