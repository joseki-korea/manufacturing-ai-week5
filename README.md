---
id: joseki-korea-manufacturing-ai-week5/README.md
title: 충북대학교 제조 AI 실제 5주차 실습 및 과제 — 프로젝트 개요
repo: joseki-korea-manufacturing-ai-week5
device_scope: all
doc_type: readme
tags: ["manufacturing-ai", "unsupervised-learning", "generative-models", "autoencoder", "vae", "gan", "diffusion"]
status: DRAFT
updated: 2026-11-07
source_of_truth: README.md
---

# 충북대학교 제조 AI 실제 (8884023-01) - 5주차 실습 및 과제

- **작성자**: 2026154001 정용석
- **교과목**: 제조 AI 실제 (8884023-01, 충북대학교 산업인공지능연구센터 김영진 교수)
- **주제**: 비지도 학습 및 생성 모델 (Unsupervised Learning & Generative Models)

---

## 📚 5주차 실습 노트북 목록

| 번호 | 실습 노트북 | 핵심 내용 및 실습 과제 |
|:---:|:---|:---|
| **Lab 5-1** | [lab5_1_autoencoder.ipynb](./2026154001_정용석_lab5_1_autoencoder.ipynb) | Autoencoder 기초 잠재공간(Latent Space) t-SNE 시각화, Denoising Autoencoder(DAE) 노이즈 제거, Reconstruction Error 기반 비지도 이상치 탐지(Anomaly Detection) |
| **Lab 5-2** | [lab5_2_vae.ipynb](./2026154001_정용석_lab5_2_vae.ipynb) | Variational Autoencoder(VAE) 재매개변수화 트릭(Reparameterization Trick), ELBO 손실함수(Reconstruction + KL Divergence), 2D 잠재공간 매니폴드 연속 생성 |
| **Lab 5-3** | [lab5_3_gan.ipynb](./2026154001_정용석_lab5_3_gan.ipynb) | GAN(Generative Adversarial Network) Generator vs Discriminator 적대적 학습 구조, Minimax Game, MNIST 손글씨 신규 이미지 생성 |
| **Lab 5-4** | [lab5_4_diffusion_model.ipynb](./2026154001_정용석_lab5_4_diffusion_model.ipynb) | DDPM(Denoising Diffusion Probabilistic Model) 순방향 가우시안 노이즈 확산 및 역방향 노이즈 예측 U-Net 복원 샘플링, 생성 모델 4대 패밀리 비교 |

---

## 🎯 주요 실습 및 질문 답변 요약

### 1. Autoencoder의 잠재 공간과 비선형 차원 축소
- 선형 투영에 국한되는 전통적 PCA와 달리, 심층 오토인코더는 비선형 활성화 함수를 통해 복잡한 고차원 매니폴드를 저차원 잠재 공간($z$)에 압축·보존.
- Denoising Autoencoder(DAE)는 의도적인 가우시안 노이즈 주입($x_{noisy}$) 후 깨끗한 원본($x_{clean}$)을 복원하도록 학습하여 현장 센서 글리치 및 비전 잡음에 강건한 특징 추출기 역할 수행.

### 2. Reconstruction Error 기반 비지도 이상치 탐지(Anomaly Detection)
- 정상 데이터로만 학습된 Autoencoder는 정상 패턴 복원에 최적화되어, 미지의 불량/이상치 입력 시 높은 재구성 오차(Reconstruction MSE)를 발생시킴.
- Validation 정상 데이터의 재구성 오차 평균+표준편차($\mu + 3\sigma$) 또는 IQR 기반으로 임계값(Threshold)을 수립하여 라벨이 희소한 제조 공정 불량 탐지에 탁월한 성능 발휘.

### 3. VAE(Variational Autoencoder)의 확률적 생성과 잠재 공간 연속성
- 표준 Autoencoder의 잠재 공간이 이산적이고 군집 간 빈 공간(Hole)이 존재하는 문제를 극복하기 위해 잠재 변수를 평균($\mu$)과 분산($\sigma$)의 확률 분포로 정규화($\mathcal{N}(0, I)$).
- 역전파를 가능케 하는 재매개변수화 트릭($z = \mu + \sigma \odot \epsilon$)과 KL Divergence 규제항을 결합하여 매끄러운 2D 잠재 매니폴드 보간(Interpolation) 및 신규 샘플 생성 달성.

### 4. GAN과 Diffusion Model의 생성 메커니즘 비교
- **GAN**: Generator와 Discriminator의 2인 제로섬 게임(Minimax)을 통해 정교하고 선명한 이미지를 1-step으로 고속 생성하나, Mode Collapse 및 학습 불안정성 존재.
- **Diffusion(DDPM)**: 전진 과정에서 점진적으로 가우시안 노이즈를 주입하고, U-Net 신경망이 각 스텝의 노이즈를 예측·제거하는 다단계 마르코프 체인 역확산을 수행하여 모드 붕괴 없이 극도로 안정적이고 다양한 고품질 생성 달성.


## 실행 방법

- Python 3.10+ 및 Jupyter 환경에서 실습 노트북 실행.
- 필수 라이브러리: `torch`, `torchvision`, `numpy`, `matplotlib`, `scikit-learn`.
- 실습 노트북 순서대로 실행 (`lab5_1_autoencoder.ipynb` ~ `lab5_4_diffusion_model.ipynb`).


## 규칙 요약

- 규칙 단일 정본은 vault `main`의 `rules/INDEX.md`와 Rule 00·01·02·04이다. 이 레포 규칙은 `docs/RULES.md`에 있다.
- 세션 역할(PM·작업·janitor)은 `docs/ROLES.md`에 있다.
- 폴더 구조와 폴더별 목적은 `docs/ARCHITECTURE.md`에 있다.
- 비밀·토큰·개인정보는 어떤 파일에도 평문으로 기록하지 않는다. force push 금지, main 직접 push 금지.

## 문서 링크

| 문서 | 경로 | 내용 |
|---|---|---|
| 규칙 | [docs/RULES.md](docs/RULES.md) | 레포 규칙 + vault 정본 포인터 |
| 역할 | [docs/ROLES.md](docs/ROLES.md) | PM·작업·janitor 세션 |
| 구조 | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | 폴더 트리와 목적 |
| 핸드오프 | [handoffs/README.md](handoffs/README.md) | 에이전트 세션 인계 노트 |
| 에셋 | [assets/](assets/) | images · src · components · binaries |
| RAG 목록 | [rag-manifest.json](rag-manifest.json) | 검색 대상 문서 목록 |
