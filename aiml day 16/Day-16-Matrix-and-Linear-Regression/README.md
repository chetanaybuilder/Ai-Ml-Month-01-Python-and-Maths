# AIML Day 16 Projects

A collection of foundational Artificial Intelligence & Machine Learning implementations built with **Python** and **NumPy**. This repository contains hands-on mini-projects covering matrix operations and linear regression from scratch.

---

## 📂 Project Structure

```text
aiml-day-16/
├── .gitignore
├── README.md
├── requirements.txt
├── Project-01-Matrix-Multiplication/
│   └── Matrix.py
└── Project-02-Linear-Regression/
    └── Linear.py
```

---

## 🚀 Projects

### Project-01: Matrix Multiplication (`Project-01-Matrix-Multiplication/Matrix.py`)

Performs matrix multiplication of two 2×2 matrices using `numpy.matmul`.

**Input matrices:**

A = [[1, 2], [3, 4]]

B = [[5, 6], [7, 8]]

**Output:** The resulting product matrix computed via NumPy.

### Project-02: Linear Regression (`Project-02-Linear-Regression/Linear.py`)

Implements a simple linear regression model using the normal equation
(`θ = (XᵀX)⁻¹Xᵀy`) with NumPy, including:

- Bias/intercept term augmentation via `np.column_stack`
- Parameter estimation using `np.linalg.solve`
- Predictions on training data
- Prediction for a new input (house price in Lakh)
- Total squared error calculation

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/aiml-day-16.git
   cd aiml-day-16
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run any project script directly with Python:

```bash
# Project 01: Matrix Multiplication
python Project-01-Matrix-Multiplication/Matrix.py

# Project 02: Linear Regression
python Project-02-Linear-Regression/Linear.py
```

---

## 📋 Requirements

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical computing, linear algebra, and array operations |

Install all dependencies at once:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.14+
- **Library:** NumPy

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve these implementations.

---

*Built for AIML Day 16 learning and practice.*