# Model and session rules

## Status
DRAFT.

## Inheritance
Global vault rules → this file. Local rules add context and cannot relax global safety or approval rules.

## Model placement
Main and persona sessions use Claude Opus. Work seats use Codex Terra, Antigravity (AGY), and Claude Haiku in parallel, with one seat per repository or file.

## Naming
Use `<device4>-<session4>-<model>-<role>`, for example `NWKW-a1b2-terra-fix`.

## Context
At >=40% context or after one auto-compaction, write a handoff of at most 2000 tokens in `handoffs/active/`: role, progress, waiting, next, and ledger path. A successor seat resumes it; the old seat stays idle. Do not inject a slash-reset.

## Approval
Merge, force push, deploy, and delete require CEO approval.
