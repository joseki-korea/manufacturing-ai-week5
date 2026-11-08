---
id: "manufacturing-ai-week5/RAG.md"
title: "RAG index"
summary: "Document retrieval and exclusions"
domain: "manufacturing-ai-week5"
tags: [repository, documentation]
owner: repository-maintainers
status: draft
created: 2026-11-08
updated: 2026-11-08
source: "RAG.md"
lang: en
sensitivity: internal
related: ["README.md", "RULES.md"]
repo: "manufacturing-ai-week5"
device_scope: all
doc_type: documentation
source_of_truth: "RAG.md"
---
# RAG index

Use `rag-manifest.json` as the inventory of documents introduced by this change. Review sensitivity and access before indexing; do not index secrets, personal data, generated files or binary media. IDs are stable repository-relative paths. Recompute document hashes after changes. Existing legacy documents require separate review before ingestion.

## Wiki

The source-backed wiki lives in `docs/wiki/`; see its `SCHEMA.md` and `index.md`. Run `python3 scripts/wiki-lint.py` and `python3 scripts/rag-manifest.py` after updates. The generated JSONL is a chunk inventory, not a vector index; review sources and sensitivity before indexing.
