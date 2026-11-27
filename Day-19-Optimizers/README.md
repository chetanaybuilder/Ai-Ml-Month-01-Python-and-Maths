# 🏁 Day-19 Optimizers — Optimizer Race on the Rosenbrock Function

A from-scratch Python implementation and visual comparison of four classic optimization algorithms — **Gradient Descent**, **Stochastic Gradient Descent (SGD)**, **Momentum**, and **Adam** — racing to minimize the Rosenbrock function.

---

## 📖 Overview

This project demonstrates how different first-order optimizers behave when minimizing the non-convex Rosenbrock function (the classic "banana valley" test function). Each optimizer is implemented manually using only `numpy`, with **`matplotlib`** used to plot their loss trajectories over training iterations.

### What's inside
* `main.py` — Optimizer implementations, training loop, and comparison plots
* `req.txt` — Python dependencies

---

## 🚀 Features

| Optimizer | Description |
|-----------|-------------|
| **Gradient Descent** | Full-batch gradient descent with fixed learning rate |
| **SGD** | Stochastic gradient descent — samples one component of the gradient per step |
| **Momentum** | Accumulates a velocity vector to damp oscillations and accelerate convergence |
| **Adam** | Adaptive moment estimation with bias correction for per-parameter learning rates |

### Visual output
* Log-scale loss curves for all four optimizers on a shared plot
* Final position and final loss printed for each optimizer

---

## 🛠 Installation

### Prerequisites
* Python 3.7 or higher
* `pip`

### Install dependencies
```bash
# Clone or navigate to the project directory
cd Day-19-Optimizers

# Install required packages
pip install -r req.txt
```

---

## ▶️ Usage

Run the optimizer comparison:

```bash
python main.py
```

### What happens when you run it
1. Initializes all optimizers at `p = [-1.2, 1.0]` on the Rosenbrock landscape.
2. Trains each optimizer for 20,000 iterations using its configured learning rate.
3. Prints the final position and final loss for each optimizer.
4. Displays a log-scale plot comparing loss vs. iterations for all four methods.

---

## ⚙️ Configuration

Edit the `optimizers` dictionary in `main.py` to change learning rates or add optimizers:

```python
optimizers = {
    "Gradient Descent": 0.001,
    "SGD": 0.0005,
    "Momentum": 0.0005,
    "Adam": 0.01,
}
```

To adjust training length, modify the `steps` argument (default: `20000`).

---

## 📦 Requirements

| Package | Minimum version |
|---------|-----------------|
| `numpy` | `>=1.21.0` |
| `matplotlib` | `>=3.4.0` |

See [`req.txt`](./req.txt) for the exact pinned list.

---

## 🧠 How it works

1. **Objective** — Rosenbrock function:  
   `f(x, y) = (1 − x)² + 100(y − x²)²` — global minimum at `(1, 1)` with value `0`.

2. **Gradient** — Analytical gradient computed by hand for full-batch updates.

3. **Update rule (generic)** — `p = p − lr · g` where `g` is the (possibly modified) gradient.

4. **Algorithm-specific modifications:**
   * **Momentum:** `velocity = 0.9 · velocity + g`; uses `velocity` as the effective gradient.
   * **Adam:** Maintains first (`m`) and second (`v`) moment estimates with bias correction:
     `g = m_hat / (sqrt(v_hat) + ε)`.

---

## 📊 Example output

```
Gradient Descent
Final position: [0.9976 0.9952]
Final loss: 5.1e-06
----------------------
SGD
Final position: [0.9951 0.9904]
Final loss: 2.4e-05
----------------------
Momentum
Final position: [0.9992 0.9984]
Final loss: 1.1e-06
----------------------
Adam
Final position: [0.9999 0.9998]
Final loss: 2.3e-08
----------------------
```

*(Exact values vary slightly between runs due to SGD randomness.)*

---

## 🗂 Project structure

```
Day-19-Optimizers/
├── main.py      # Optimizer implementations, training loop, and plots
├── requirement.txt      # Python package dependencies
└── README.md    # This file
```

---

## 📄 License

This project is provided for educational purposes. Feel free to use, modify, and distribute it.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new optimizers, improve the visualizations, or fix issues, please open a pull request or issue.

---

**Built with ❤️ using Python, NumPy, and Matplotlib**