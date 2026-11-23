# Day-15-Cosine-Similarity-Search-Engine

> A lightweight semantic sentence search engine built with Python, TF-IDF vectorization, and cosine similarity ranking.

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

This project implements a document-retrieval style search engine that indexes a collection of sentences (`sentences.txt`) using **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization and retrieves the most semantically similar sentences to a user-provided query using **cosine similarity**.

It is designed as a foundational NLP/ML exercise demonstrating:

* Text vectorization with TF-IDF
* Dense vector representation of documents
* Cosine similarity computation for ranking
* Top-K retrieval and result display

---

## Features

* 🔍 **Semantic Search** – Retrieve top-K sentences most similar to a natural-language query.
* 📊 **TF-IDF Vectorization** – Converts raw text into numerical feature vectors weighting rare, informative terms higher.
* 📈 **Cosine Similarity Ranking** – Ranks sentences by angular proximity in vector space.
* 🚀 **Zero Dependencies Beyond NumPy & scikit-learn** – Minimal, production-friendly stack.
* 🧩 **Modular Codebase** – Clean separation of data loading, vectorization, querying, and display logic.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.14 |
| Linear Algebra | NumPy |
| ML / Vectorization | scikit-learn (`TfidfVectorizer`, `cosine_similarity`) |
| Data | `sentences.txt` (1,000 curated sentences) |

---

## Project Structure

```
Day-15-Cosine-Similarity-Search-Engine/
├── main.py              # Entry point: loads data, vectorizes, queries, and displays top-5 matches
├── sentences.txt        # Corpus of 1,000 sentences (one per line)
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules for Python projects
└── README.md            # Project documentation (this file)
```

---

## Installation

### Prerequisites

* Python 3.9 or higher
* `pip` package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/chetanaybuilder/Ai-Ml-Month-01-Python-and-Maths.git
cd Ai-Ml-Month-01-Python-and-Maths/Day-15-Cosine-Similarity-Search-Engine

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# or
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

Run the search engine from the project directory:

```bash
python main.py
```

You will be prompted to enter a search query:

```
Enter your search query: artificial intelligence healthcare
```

### Example Output

```
Top 5 similar sentence:

Rank: 1

Sentence: Machine learning is improving healthcare.
Similarity: 0.8421

Rank: 2

Sentence: Artificial intelligence is transforming medical diagnosis.
Similarity: 0.7913

...
```

The engine returns the **top 5 most similar sentences** from `sentences.txt`, ranked by cosine similarity score (0.0 to 1.0, where higher = more similar).

---

## How It Works

1. **Load Corpus** – Reads `sentences.txt` into a list of cleaned, non-empty strings.
2. **Vectorize** – `TfidfVectorizer` converts each sentence into a TF-IDF weighted vector.
3. **Query** – User input is transformed into the same vector space using the fitted vectorizer.
4. **Score** – `cosine_similarity` computes the cosine of the angle between the query vector and every sentence vector.
5. **Rank** – Sentence indices are sorted in descending order of similarity (`argsort(...)[::-1]`).
6. **Display** – The top 5 sentences are printed with their rank, text, and similarity score.

---

## Customization

* **Change top-K results:** Edit the slice `ranked_indices[:5]` in `main.py` to return more or fewer matches.
* **Expand corpus:** Add new sentences to `sentences.txt` (one per line) and re-run.
* **Tune vectorization:** Pass parameters to `TfidfVectorizer()` (e.g., `ngram_range`, `stop_words`, `max_df`) to alter term weighting behavior.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Chetanay Batta**  
AI/ML Engineer | Python & Mathematics Enthusiast  
Email: chetanaybatta361@gmail.com  
GitHub: [chetanaybuilder](https://github.com/chetanaybuilder)

---

## Acknowledgments

* [scikit-learn](https://scikit-learn.org/) – TF-IDF and cosine similarity implementations
* [NumPy](https://numpy.org/) – Numerical computing foundation