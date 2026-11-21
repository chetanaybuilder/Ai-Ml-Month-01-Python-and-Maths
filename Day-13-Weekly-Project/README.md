# 📊 Day-13 Weekly Project — Sales Data Analysis & Vectorization Benchmark

> **Course:** AI-ML Month 01 — Python and Maths  
> **Folder:** `Day-13-Weekly-Project`  
> **Author:** chetanaybuilder  
> **Status:** ✅ Complete & Verified

---

## 📖 Overview

This project performs exploratory data analysis (EDA) on a retail sales dataset and benchmarks the performance difference between a **pure Python loop** and **NumPy vectorization**. It demonstrates:

* Data cleaning and preprocessing with **pandas**
* Statistical summarization and grouping
* Revenue analysis by product
* Execution-time benchmarking (Python vs NumPy)
* Visualization with **matplotlib**

---

## 🗂 Project Structure

```text
Day-13-Weekly-Project/
│
├── data/
│   └── dataset.csv            # Raw retail sales dataset
│
├── charts/                    # Generated chart outputs (gitignored)
│   ├── revenue_by_product.png
│   └── vectorization_benchmark.png
│
├── analysis.py                # EDA: cleaning, grouping, revenue summary
├── vectorization.py           # Benchmark: Python loop vs NumPy vectorization
├── visualization.py           # Charts: revenue bar chart + benchmark bar chart
├── main.py                    # Entry point — runs the full report
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 🚀 Getting Started

### Prerequisites

Python 3.11+ is recommended.

### Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/chetanaybuilder/Ai-Ml-Month-01-Python-and-Maths.git
cd Ai-Ml-Month-01-Python-and-Maths/Day-13-Weekly-Project
```

Create and activate a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

You will see the full data analysis report printed to the console, and two charts will be saved to the `charts/` directory:

| Chart | Description |
|-------|-------------|
| `revenue_by_product.png` | Total revenue grouped by product |
| `vectorization_benchmark.png` | Python loop vs NumPy execution time |

---

## 📊 Sample Output

```text
========== DATA ANALYSIS REPORT ==========

Dataset Preview:
        Date   Product     Category  Units_Sold  Unit_Price  Revenue Region
0 2026-01-01    Laptop  Electronics           5       50000   250000  North
1 2026-01-02     Mouse  Accessories          20         500    10000  South
...

Dataset Shape:
(15, 7)

Missing Values:
Date          0
Product       0
Category      0
Units_Sold    0
Unit_Price    0
Revenue       0
Region        0
dtype: int64

Revenue Analysis:
             sum      mean     max     min
Product
Keyboard   52800   13200.0   16800    9600
Laptop    700000  175000.0  250000  100000
Monitor   288000   96000.0  120000   72000
Mouse      39000    9750.0   12500    7500

========== REPORT COMPLETED ==========
```

Benchmark output (from `vectorization.py`):

```text
python loop time: 0.67s
numpy vectorization time: 0.01s
speedup: 66.46x
```

---

## 🧠 Key Learnings

* **pandas** — Reading CSVs, checking dimensions/dtypes/missing values/duplicates, string cleaning (`.str.strip()`), datetime conversion, `.groupby()` and `.agg()` for aggregations.
* **NumPy vectorization** — Vectorized operations are orders of magnitude faster than equivalent Python `for` loops (≈66× speedup in this benchmark).
* **matplotlib** — Creating bar charts, labeling axes, rotating tick labels, saving figures to disk.
* **Project hygiene** — `requirements.txt` for reproducibility, `.gitignore` to exclude caches/env/outputs, modular script design.

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| [Python 3](https://www.python.org/) | Core language |
| [pandas](https://pandas.pydata.org/) | Data manipulation & analysis |
| [NumPy](https://numpy.org/) | Numerical computing & vectorization |
| [matplotlib](https://matplotlib.org/) | Data visualization |

---

## 📜 License

This project is part of the **AI-ML Month 01 — Python and Maths** course repository.

---

## 🤝 Contributing

This is a course project. Feel free to open issues or submit pull requests in the main repository to suggest improvements.

---

<p align="center">
  Built with ❤️ for the AI-ML Month 01 Python & Maths journey.
</p>