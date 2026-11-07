---
id: joseki-korea-manufacturing-ai-week5/docs/RULES
title: 충북대학교 제조 AI 실제 5주차 실습 및 과제 — 규칙
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: rules
tags: [rules, safety]
status: DRAFT
updated: 2026-11-07
source_of_truth: vault main rules/INDEX.md
---

# 규칙

## 정본 포인터

이 레포의 규칙 정본은 vault `main` 브랜치의 `rules/INDEX.md`와 Rule 00(안전·승인), Rule 01(토폴로지·소유권), Rule 02(수송·배차), Rule 04(표현·출처)이다. 이 문서는 정본을 복제하지 않고 레포 고유 규칙만 추가한다. 상태는 DRAFT이며 임의로 FINAL로 승격하지 않는다.

## 안전 불변식

- force push 금지. main 직접 push 금지. 변경은 작업 가지 + PR로만 한다.
- 기존 dirty·untracked 변경은 사용자 소유로 보존한다. 삭제·이동은 승인 없이 하지 않는다.
- 비밀·token·key·계정 ID·개인정보를 평문으로 기록하지 않는다.
- 신원·대상·권한이 불명확하면 중단하고 상향한다(fail-closed).

## 레포 고유 규칙

- 교육 실습 및 모델 실습 전용 레포지토리로 대용량 데이터셋 및 가중치 파일은 커밋하지 않는다.
- 노트북 실행 출력물 내 개인정보 및 API 키 등 민감정보 포함 여부를 점검한다.

## 보고와 증거

- 완료 보고에는 경로·sha8·판정·건수를 포함한다. 실측과 추정을 구분한다.
- 감사 기록·receipt는 append-only로 남긴다.
