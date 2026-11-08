---
id: manufacturing-ai-week5-wiki-schema
title: "위키 작성 규칙"
summary: "위키 작성 규칙"
domain: repository
tags: [wiki]
owner: repository-maintainers
status: draft
created: 2026-11-08
updated: 2026-11-08
source: "docs/wiki/SCHEMA.md"
lang: ko
sensitivity: internal
related: []
---

# 위키 작성 규칙

원본은 저장소의 코드와 문서이며 복사하지 않는다. 위키는 `docs/wiki/`에 두고 벡터 색인은 저장소에 커밋하지 않는다.

## Ingest

원본을 읽고 민감 정보를 제외한다. 주제별 개요·모듈·개념·엔터티·실행 방법·FAQ 페이지를 작성하고 각 주장에 `[source: path#Lline @sha8]`로 원본 커밋과 줄을 기록한다. 한 페이지에 한 주제를 담고 필수 정보칸을 채운다. 목록을 갱신하고 로그 끝에 ingest 기록을 추가한다.

## Query

목록에서 관련 페이지를 찾고 원본 줄과 커밋을 확인한다. 근거가 없는 답은 추측하지 않는다.

## Lint

`python3 scripts/wiki-lint.py`로 정보칸, 출처, 변경된 원본, 목록 연결과 상대 링크를 점검하고 사람이 주장과 민감 정보를 검토한다. `python3 scripts/rag-manifest.py`로 마크다운 청크 목록을 갱신한다.

## 페이지와 정보칸

파일과 디렉터리 이름은 영문 소문자 kebab-case로 정하고 한글 제목을 정보칸에 둔다. 각 페이지에는 id, title, summary, domain, tags, owner, status, created, updated, source, lang, sensitivity, related를 기재한다.

제목은 의미 단위로 계층화하고 한 절은 A4 한 장을 넘기지 않는다. 표에는 머리줄을 두고 그림에는 한 줄에서 세 줄의 설명을 덧붙인다. 비밀, 개인정보, 회사 내부 수치는 위키에 넣지 않으며 secret 자료의 페이지는 만들지 않는다.

위키 정보칸 id는 레포 슬러그와 wiki, 상대 경로 슬러그를 결합한다. 청크 id도 레포 슬러그로 구분한다. 관리 파일 `SCHEMA.md`는 표준 대문자 이름 예외다.
