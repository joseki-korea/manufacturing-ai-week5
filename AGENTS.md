# Codex Terra Agent Guidelines — manufacturing-ai-week5

본 문서는 `manufacturing-ai-week5` 프로젝트에서 Codex Terra 에이전트의 역할과 작업 강령을 정의합니다.

## 1. 역할 범위: Worker Session (작업 세션)
- Codex Terra는 **작업 세션(Work Session)**으로서 비즈니스 로직, 백엔드 알고리즘, 코어 데이터 연산 및 스크립트를 전담 구현합니다.
- 변경 작업 시 기존 코드를 파괴하지 않으며, 단독 커밋 및 철저한 테스트를 수반합니다.

## 2. 운영 지침
- 작업 완료 후 구체적인 코드 실행 증거를 제시합니다.
- 상세 역할 및 규칙: 👉 **[docs/agents/codex-role.md](docs/agents/codex-role.md)** · **[docs/agents/codex-rules.md](docs/agents/codex-rules.md)**

## 규칙 상속 (전역 → 지역)

전역: solucionemos-vault main의 `rules/INDEX.md`, Rule 00·01·02·04와 `~/.claude/CLAUDE.md`, `~/orca/CLAUDE.md`. 지역: [MODEL-SESSION-RULES.md](MODEL-SESSION-RULES.md), [ROLES.md](ROLES.md), [PM.md](PM.md), [ARCHITECTURE.md](ARCHITECTURE.md). 지역 문서는 저장소 맥락만 추가하며 전역 안전·승인 규칙을 완화할 수 없다.
