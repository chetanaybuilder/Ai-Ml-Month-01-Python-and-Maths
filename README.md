# Day-10-Numpy-Vectorization-Benchmark

A reproducible, educational benchmark that compares native Python list operations against NumPy vectorized array operations on one million integers. It measures setup cost, per-operation timings, and overall computation speed to demonstrate the performance advantage of NumPy vectorization.

Part of: Ai-Ml-Month-01-Python-and-Maths - Day 10

## Overview

When working with numerical data in Python, writing explicit `for` loops over lists is convenient but slow. NumPy replaces those loops with vectorized operations implemented in C, which push the iteration down to compiled code and operate on contiguous memory blocks.

This project benchmarks six common operations using a high-resolution timer:

| Category | Python (native list) | NumPy (vectorized array) |
|----------|----------------------|--------------------------|
| Dataset creation | list(range(...)) | np.array(list) |
| Addition | append(number + 10) | arr + 10 |
| Multiplication | append(number * 2) | arr * 2 |
| Squaring | append(number ** 2) | arr ** 2 |
| Filtering | if number > 50: append(...) | arr > 50 (boolean mask) |
| Summation | total += number | np.sum(arr) |

Setup times are reported separately and are excluded from the overall computation comparison, because building a Python list and converting it to a NumPy array are not equivalent work.

## Features

- Side-by-side timing of Python vs NumPy for addition, multiplication, squaring, filtering, and summation.
- High-resolution wall-clock timing via time.perf_counter().
- Clear tabular report with per-operation timings and an overall computation winner.
- Setup (dataset creation) cost shown for context only.
- Clean, well-documented code suitable for learning and demonstration.

## Project Structure

Day-10-Numpy-Vectorization-Benchmark/
|-- main.py              Benchmark script: Python list vs NumPy array timings
|-- README.md            Project documentation (this file)
|-- requirements.txt     Python dependencies (NumPy)
`-- .gitignore           Git ignore rules (venv, caches, OS files)

## Requirements

- Python 3.10 or later
- NumPy 2.x (numpy>=2.0,<3.0)

## Setup

From the Day-10-Numpy-Vectorization-Benchmark directory, create and activate a virtual environment, then install dependencies:

PowerShell (Windows):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS / Linux (bash/zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The .venv/ directory is ignored by git (see .gitignore) and should not be committed.

## Usage

Run the benchmark from the project directory:

```powershell
python main.py
```

Example output:

```
====================================================================
                 PYTHON vs NUMPY PERFORMANCE
====================================================================
Operation                 Python (s)        NumPy (s)         Faster
--------------------------------------------------------------------
Dataset creation          0.023456          0.012345          NumPy
Addition                  0.045678          0.003210          NumPy
Multiplication            0.048912          0.003456          NumPy
Squaring                  0.052341          0.004123          NumPy
Filtering                 0.039876          0.002891          NumPy
Summation                 0.031234          0.001987          NumPy
--------------------------------------------------------------------
Total computation         0.218041          0.015667
Overall winner: NumPy (13.92x faster for computation)
====================================================================
```

Exact numbers depend on your CPU, Python/NumPy versions, and system load. Run the script multiple times when evaluating performance. This is an educational benchmark, not a statistically rigorous one.

## Key Takeaways

1. Vectorization wins. NumPy vectorized operations are typically an order of magnitude (or more) faster than equivalent Python for loops over lists.
2. Avoid Python loops on large arrays. Element-wise Python loops carry interpreter overhead per iteration; NumPy pushes that loop into compiled C.
3. Setup cost differs. Creating a NumPy array from a Python list has a one-time conversion cost; for repeated computations on the same data, that cost is amortized and quickly paid back.
4. Use NumPy for numerical workloads. For data science and machine learning, prefer NumPy arrays and vectorized expressions over native Python lists and loops.

## License

This project is part of the Ai-Ml-Month-01-Python-and-Maths learning repository.

## Author

Chetanay Batta - chetanaybatta361@gmail.com
GitHub: https://github.com/chetanaybuilder