---
id: joseki-korea-manufacturing-ai-week5/assets/images/README
title: 이미지 에셋
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: asset-index
tags: [assets, images]
status: DRAFT
updated: 2026-11-07
source_of_truth: docs/ARCHITECTURE.md
---

# assets/images/

## 목적

프로젝트 문서·화면에 쓰는 이미지 보관.

## 이름 규칙

`kebab-case.png`. 이미지마다 같은 이름의 `.md` 설명 파일(alt-text + 캡션)을 둔다. 검색(RAG)은 이 설명 파일로 한다.

## 넣으면 안 되는 것

비밀, 토큰, 키, 개인정보, 계정 정보. 사람 얼굴 등 개인정보 사진. 대용량 원본.

## alt-text 설명 파일 예시

```markdown
---
id: joseki-korea-manufacturing-ai-week5/assets/images/example
title: 예시 이미지
doc_type: asset-index
---
alt: 대시보드 첫 화면 캡처
caption: 2026-11 기준 메인 대시보드
```
