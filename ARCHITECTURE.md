---
id: "manufacturing-ai-week5/ARCHITECTURE.md"
title: "Architecture"
summary: "Observed application structure and data flow"
domain: "manufacturing-ai-week5"
tags: [repository, documentation]
owner: repository-maintainers
status: draft
created: 2026-11-08
updated: 2026-11-08
source: "ARCHITECTURE.md"
lang: en
sensitivity: internal
related: ["README.md", "RULES.md"]
repo: "manufacturing-ai-week5"
device_scope: all
doc_type: documentation
source_of_truth: "ARCHITECTURE.md"
---
# Architecture

## Components and data flow

Four root Jupyter notebooks cover autoencoders, variational autoencoders, GANs and diffusion models. Notebook code loads MNIST with TensorFlow Keras and runs the associated training and visualizations. No separately packaged application or automated test suite is tracked. Open the notebooks in a compatible Jupyter environment after installing their imports; compute and data-download requirements have not been verified.

## Current folders


## Proposed asset organization and migration

See [asset map](docs/ASSET-MAP.md). Existing assets remain in place. Before any migration, inventory references, obtain independent review, use `git mv`, update references, and pass the build and tests. Roll back by reverting the migration commit.
