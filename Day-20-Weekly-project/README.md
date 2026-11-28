# Day 20 Weekly Project — Eigenfaces: PCA Face Recognizer

A small educational machine-learning experiment that uses **Principal Component
Analysis (PCA)** and **K-Nearest Neighbors (KNN)** on the public Olivetti Faces
benchmark dataset.

## What it does

1. Loads 400 grayscale face images from 40 classes.
2. Splits the dataset into training and testing sets.
3. Trains a PCA + KNN pipeline using 10, 20, 30, 50, and 100 PCA components.
4. Measures test accuracy for each configuration.
5. Saves a graph showing **accuracy vs. number of PCA components**.

## Project structure

```text
Day-20-Weekly-project/
├── main.py
├── requirements.txt
├── README.md
└── results/
    └── (generated images appear here after running)
```

## Setup

Python 3.9+ is recommended.

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The first run downloads the Olivetti Faces dataset through scikit-learn.
An internet connection is needed for that initial download. Later runs can
use the local dataset cache.

## Results

The program prints the test accuracy for each PCA component count and saves:

- `results/sample_faces.png`
- `results/accuracy_vs_components.png`

The accuracy values are produced by your run; they are not hard-coded.
Results can vary with the train/test split and model settings.

## Core concepts

- **PCA:** reduces the number of input features while retaining directions
  with high variance.
- **Eigenfaces:** principal components learned from face-image data; each
  component can be visualized as a face-like pattern.
- **KNN:** predicts a class using the labels of nearby training examples.
- **Components:** the number of principal directions retained by PCA.

## Important note

This is a learning exercise on a public benchmark dataset. It is not designed
or validated for real-world identity verification, surveillance, or decisions
about people. Test accuracy on this small dataset does not establish real-world
reliability.

## Dataset credit

Olivetti Faces dataset, distributed through `sklearn.datasets.fetch_olivetti_faces`.
