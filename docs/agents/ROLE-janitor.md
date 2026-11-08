---
id: "manufacturing-ai-week5/docs/agents/ROLE-janitor"
title: "정리 담당 역할 (janitor)"
summary: "임시 파일·끝난 작업 흔적을 되돌릴 수 있는 방식으로 정리하는 역할 규칙"
domain: "manufacturing-ai-week5"
tags: ["agents", "janitor"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "대표 지시 2026-11-08 멀티에이전트 핸드오프·janitor·watchdog·훅 (D2)"
lang: "ko"
sensitivity: "internal"
related: ["docs/agents/ROLE-watchdog.md", "docs/agents/handoffs/README.md", "docs/agents/HOOKS.md"]
---

# 정리 담당 역할 (janitor)

정리 담당은 작업자가 남긴 임시 파일과 끝난 작업의 흔적을 안전하게 치운다. **되돌릴 수 있는 것만** 다룬다.

## 대상 (허용)

- 작업자가 만든 복제본·작업트리 중 **깨끗하고 푸시 완료된** 것 (미커밋 변경 0, 원격과 같은 상태)
- 병합된 작업 브랜치의 **로컬** 사본 (원격 브랜치는 건드리지 않는다)
- 오래된 핸드오프: `docs/agents/handoffs/active/`에서 상태가 `done`이고 14일 지난 파일 → `archive/`로 이동
- 임시 파일: 아래 "이 저장소 대상"의 재생성 가능한 파일

## 금지

- 사용자가 수정 중인 파일 삭제·이동
- 드라이브(디스크 볼륨) 삭제·포맷
- 원격 브랜치·태그·PR 삭제
- 미커밋 변경이 있는 작업트리 정리
- `archive/`의 파일 삭제 (보존)

## 절차: 목록 → 기록 → 실행 → 영수증

1. **목록**: 대상 후보를 경로·크기와 함께 나열한다.
2. **기록**: 목록을 `docs/agents/handoffs/active/`에 `YYYYMMDD-HHMM-janitor-to-owner-cleanup-list.md`로 남긴다.
3. **실행**: 되돌릴 수 있는 방식만 쓴다. 영구 삭제 대신 `~/orca/_trash-janitor/<날짜>/`로 옮기고, 재생성 가능한 캐시만 영구 삭제한다. 핸드오프는 `git mv`로 이동한다.
4. **영수증**: 실행한 항목·건수·실패 항목을 `YYYYMMDD-HHMM-janitor-to-owner-cleanup-receipt.md`로 남긴다.

## 이 저장소 대상 (실측)

- 재생성 가능한 후보 (`.gitignore` 실측): 없음(실측)
- 임시 경로: `tmp/`, `temp/`, `*.tmp`, `.DS_Store` (추적 중인 파일은 제외)
- 보존 — 삭제 금지, 목록만 보고: `reports/`
- 큰 디렉터리: 크기 1GB 초과 시 목록에만 올린다 (삭제 대상 아님)
