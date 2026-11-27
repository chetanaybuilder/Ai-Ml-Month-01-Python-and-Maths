#importing required modules
import numpy as np
import matplotlib.pyplot as plt

# 1. Rosenbrock function
def rosenbrock(p):
    x, y = p
    return (1 - x)**2 + 100 * (y - x**2)**2


# 2. Gradient of Rosenbrock function
def gradient(p):
    x, y = p
    dx = -2 * (1 - x) - 400 * x * (y - x**2)
    dy = 200 * (y - x**2)
    return np.array([dx, dy])


# 3. Run an optimizer
def optimize(name, lr, steps=20000):

    p = np.array([-1.2, 1.0])
    velocity = np.zeros(2)
    m = np.zeros(2)
    v = np.zeros(2)
    losses = []

    for t in range(1, steps + 1):

        # SGD: randomly select one function component
        if name == "SGD":
            x, y = p

            if np.random.rand() < 0.5:
                g = 2 * np.array([-2 * (1 - x), 0.0])
            else:
                g = 2 * np.array([
                    -400 * x * (y - x**2),
                    200 * (y - x**2)
                ])
        else:
            g = gradient(p)

        # Momentum
        if name == "Momentum":
            velocity = 0.9 * velocity + g
            g = velocity

        # Adam
        if name == "Adam":
            m = 0.9 * m + 0.1 * g
            v = 0.999 * v + 0.001 * (g**2)

            m_hat = m / (1 - 0.9**t)
            v_hat = v / (1 - 0.999**t)

            g = m_hat / (np.sqrt(v_hat) + 1e-8)

        # Update position
        p = p - lr * g

        losses.append(rosenbrock(p))

    return p, losses


# 4. Race the four optimizers
optimizers = {
    "Gradient Descent": 0.001,
    "SGD": 0.0005,
    "Momentum": 0.0005,
    "Adam": 0.01
}

results = {}

for name, lr in optimizers.items():
    position, losses = optimize(name, lr)
    results[name] = losses

    print(name)
    print("Final position:", position)
    print("Final loss:", rosenbrock(position))
    print("----------------------")


# 5. Compare their performance
for name, losses in results.items():
    plt.plot(losses, label=name)

plt.yscale("log")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("4 Optimizers Racing on Rosenbrock Function")
plt.legend()
plt.grid()
plt.show()