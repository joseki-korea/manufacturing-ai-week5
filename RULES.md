---
id: "manufacturing-ai-week5/RULES.md"
title: "Repository rules"
summary: "Repository-wide collaboration rules"
domain: "manufacturing-ai-week5"
tags: [repository, documentation]
owner: repository-maintainers
status: draft
created: 2026-11-08
updated: 2026-11-08
source: "RULES.md"
lang: en
sensitivity: internal
related: ["README.md", "RULES.md"]
repo: "manufacturing-ai-week5"
device_scope: all
doc_type: documentation
source_of_truth: "RULES.md"
---
# Repository rules

Follow the [vault rules index](https://github.com/joseki-korea/solucionemos-vault/blob/main/rules/INDEX.md) and existing project documentation. Use topic branches, normal pushes, draft PRs, and independent review. Never commit credentials, personal data, or new media binaries. Preserve existing content. Propose asset moves in the asset map before changing references. Do not change sharing or merge without authorization.

## 멀티에이전트 핸드오프 절차

- 인계는 `docs/agents/handoffs/`에 양식(`TEMPLATE.md`)을 복사해 남긴다. 이름과 원칙은 [핸드오프 규칙](docs/agents/handoffs/README.md)을 따른다.
- 받은 쪽은 ACK 줄을 추가하고, 끝나면 `archive/`로 옮긴다.
- 정리·감시 역할: [정리 담당](docs/agents/ROLE-janitor.md), [감시 담당](docs/agents/ROLE-watchdog.md). 훅 목록: [HOOKS](docs/agents/HOOKS.md).
- 기록은 append-only, 비밀 금지. 상위 안전·권한 경계를 완화하지 않는다.
