# Day-18-Calculus

> Gradient Verification: Analytical vs Numerical Gradients Using NumPy

---

## 📖 Overview

**Day-18-Calculus** is a hands-on implementation of **gradient checking**, a fundamental technique in calculus and machine learning used to verify the correctness of analytically derived gradients by comparing them against numerically approximated gradients.

The project defines a multivariable loss function, computes its **analytical gradient** using calculus, approximates the **numerical gradient** via the central difference method, and validates that both gradients match within a specified tolerance.

---

## 🧮 Mathematical Background

### Loss Function

The objective function being optimized is:

$$f(x, y) = x^2 + 3y^2 + 2xy$$

### Analytical Gradient

By applying partial differentiation:

$$\frac{\partial f}{\partial x} = 2x + 2y$$
$$\frac{\partial f}{\partial y} = 6y + 2x$$

Thus, the analytical gradient is:

$$\nabla f(x, y) = \begin{bmatrix} 2x + 2y \\ 6y + 2x \end{bmatrix}$$

### Numerical Gradient (Central Difference)

The numerical gradient is approximated using the central difference formula:

$$\frac{\partial f}{\partial x_i} \approx \frac{f(x + h\mathbf{e}_i) - f(x - h\mathbf{e}_i)}{2h}$$

where $h = 10^{-5}$ and $\mathbf{e}_i$ is the unit vector in the $i$-th dimension.

### Gradient Check

The implementation verifies correctness using `np.allclose` with:
- Relative tolerance (`rtol`): `1e-4`
- Absolute tolerance (`atol`): `1e-6`

---

## ✨ Features

- ✅ Multivariable loss function definition
- ✅ Analytical gradient computation (symbolic derivatives)
- ✅ Numerical gradient approximation (central difference method)
- ✅ Gradient verification using `np.allclose`
- ✅ Clear console output showing loss, both gradients, and their difference
- ✅ Pass/fail status for gradient matching

---

## 📁 Project Structure

```
Day-18-Calculus/
├── main.py          # Core implementation: loss function, gradients, and verification
├── README.md        # Project documentation (this file)
└── requirements.txt # Python dependency declarations
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Setup

1. **Clone the repository** (or navigate to the project folder):

   ```bash
   cd Day-18-Calculus
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Run the gradient verification script:

```bash
python main.py
```

### Expected Output

```text
Loss: 43.0
Analytical Gradient: [10. 22.]
Numerical Gradient: [10. 22.]
Difference: [3.31965566e-10 1.22330590e-10]
PASS: Gradients match!
```

*Values may vary slightly due to floating-point precision.*

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Programming language |
| **NumPy** | Numerical computing and array operations |

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details (if applicable).

---

## 👤 Author

**Day-18-Calculus** — Calculus & Gradient Verification Exercise

---

## 🔗 References

- [NumPy Documentation](https://numpy.org/doc/)
- [Wikipedia: Gradient](https://en.wikipedia.org/wiki/Gradient)
- [Wikipedia: Finite Difference](https://en.wikipedia.org/wiki/Finite_difference)

---

<p align="center">
  <b>Built with ❤️ for learning calculus and gradient verification.</b>
</p>