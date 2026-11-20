# Day-12-Matplotlib-Profiling

> Professional data visualization and performance profiling with Python's Matplotlib, cProfile, and timeit.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-green.svg)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 Overview

This project demonstrates student performance visualization using Matplotlib, combined with code profiling using `cProfile` and benchmarking using `timeit`. It reads subject-wise marks from a CSV data file, renders a bar chart, profiles the execution, and outputs performance metrics.

## 🚀 Features

- **Data Visualization**: Bar chart of student marks by subject with publication-quality output (300 DPI)
- **Performance Profiling**: CPU profiling with `cProfile` and cumulative statistics output
- **Benchmarking**: Execution time measurement with `timeit` over 1,000 iterations
- **Clean Project Structure**: Separation of source code, data, and generated artifacts
- **Production-Ready**: Includes `.gitignore`, `requirements.txt`, and comprehensive documentation

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Setup

```bash
# Clone the repository
git clone https://github.com/chetanaybuilder/Ai-Ml-Month-01-Python-and-Maths.git
cd Ai-Ml-Month-01-Python-and-Maths/Day-12-Matplotlib-Profiling

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r req.txt
```

## 🏃‍♂️ Usage

```bash
# Run the visualization and profiling script
python main.py
```

### What happens when you run it:

1. **Reads** subject/marks data from `data/data.txt`
2. **Generates** a bar chart (`chart.png`) at 300 DPI
3. **Profiles** the execution using `cProfile` and saves stats to `profile.prof`
4. **Benchmarks** the `sum(marks)` operation over 1,000 iterations
5. **Prints** total marks and execution time to the console

### Expected Output

```
Total: 495
Execution time: 0.000123...
```

And two generated files:
- `chart.png` — Student performance bar chart
- `profile.prof` — cProfile binary stats (viewable with `pstats` or `snakeviz`)

## 📁 Project Structure

```
Day-12-Matplotlib-Profiling/
├── main.py              # Entry point: visualization + profiling
├── req.txt              # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
├── data/
│   └── data.txt         # Subject/marks CSV data
├── chart.png            # Generated bar chart (gitignored)
└── profile.prof         # cProfile output (gitignored)
```

## 🔍 Profiling Details

### cProfile
The script profiles the summation operation using `cProfile.Profile()` and saves detailed statistics sorted by cumulative time to `profile.prof`.

To view the profiling report:

```bash
python -m pstats profile.prof
# or with snakeviz
pip install snakeviz
snakeviz profile.prof
```

### timeit Benchmark
The `sum(marks)` operation is benchmarked over 1,000 iterations to measure average execution time.

## 📊 Sample Data (`data/data.txt`)

```
Maths,85
Physics,78
Chemistry,92
English,88
Biology,81
Computer Science,95
Economics,76
```

## 🛠️ Built With

- [Python 3.10+](https://www.python.org/)
- [Matplotlib 3.7+](https://matplotlib.org/) — Data visualization
- [cProfile](https://docs.python.org/3/library/profile.html) — Built-in profiler
- [timeit](https://docs.python.org/3/library/timeit.html) — Execution timing

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Chetanay Batta** — chetanaybatta361@gmail.com

[![GitHub](https://img.shields.io/badge/GitHub-chetanaybuilder-blue?logo=github)](https://github.com/chetanaybuilder)

## 🙏 Acknowledgments

Part of the **AI-ML Month 01: Python and Maths** learning series.

---

*Crafted with ❤️ by a 20-year veteran software engineer*