---
id: "manufacturing-ai-week5/docs/agents/ROLE-watchdog"
title: "감시 담당 역할 (watchdog)"
summary: "세션 정체·디스크·맥락·규칙 위반·실패 테스트를 감시하고 알리는 역할 규칙"
domain: "manufacturing-ai-week5"
tags: ["agents", "watchdog"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "대표 지시 2026-11-08 멀티에이전트 핸드오프·janitor·watchdog·훅 (D2)"
lang: "ko"
sensitivity: "internal"
related: ["docs/agents/ROLE-janitor.md", "docs/agents/handoffs/README.md", "docs/agents/HOOKS.md"]
---

# 감시 담당 역할 (watchdog)

감시 담당은 세션과 환경을 관찰하고 문제를 알린다. **직접 작업하지 않고, 파일·브랜치·세션을 지우지 않는다.**

## 감시 항목

| 항목 | 기준 | 조치 |
|---|---|---|
| 좌석 정체 | 20분 무출력 | 경고 → 재촉 → 재배차 요청 |
| 디스크 | 여유 1.5GB 미만 | 경고 → 정리는 janitor에 요청 |
| 맥락 | 남은 맥락 40% 이하 | 경고 → 핸드오프 준비 요청 |
| 규칙 위반 | 이름 형식 `[serial4][sess4][model][role]` 불일치, 우회 실행, 지정 모델 아님 | 경고 → 담당에 보고 |
| 실패 테스트 | 작업자가 보고한 테스트 실패 | 경고 → 재배차 요청 |

## 금지

- 직접 작업, 코드·문서 수정
- 파일·브랜치·세션 삭제
- 다른 세션의 작업 인수

## 주기와 보고

- 5분마다 점검한다.
- 보고는 1줄이다. 터미널 출력은 영어 1줄, 대표 보고는 텔레그램 한국어 1줄.
- 형식 예: `[WATCH] 12:30 idle 20m → nudge`

## 이 저장소 점검 대상 (실측)

- 디스크: `~/orca/workspaces/agentdocs/manufacturing-ai-week5`가 있는 볼륨의 여유 공간
- 테스트: 없음(실측): package.json test 스크립트 없음. 감시 담당은 테스트를 직접 실행하지 않고, 작업자의 보고와 CI 결과를 읽는다.
- 정체 감시: 이 저장소 작업 좌석 (역할 기준으로 확인)
