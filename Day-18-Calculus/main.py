#importing required library
import numpy as np


# Define our mathematical function
def loss_function(x):
    return x[0]**2 + 3 * x[1]**2 + 2 * x[0] * x[1]


# Calculate the analytical gradient
def analytical_gradient(x):
    dx = 2 * x[0] + 2 * x[1]
    dy = 6 * x[1] + 2 * x[0]

    return np.array([dx, dy])


# Calculate the numerical gradient
def numerical_gradient(function, x, h=1e-5):

    gradient = np.zeros_like(x, dtype=float)

    for i in range(len(x)):

        x_plus = x.copy()
        x_minus = x.copy()

        x_plus[i] += h
        x_minus[i] -= h

        gradient[i] = (
            function(x_plus) - function(x_minus)
        ) / (2 * h)

    return gradient


#  Test our gradient checker
x = np.array([2.0, 3.0])

actual_gradient = analytical_gradient(x)
estimated_gradient = numerical_gradient(loss_function, x)

# Compare both gradients
difference = np.abs(actual_gradient - estimated_gradient)

print("Loss:", loss_function(x))
print("Analytical Gradient:", actual_gradient)
print("Numerical Gradient:", estimated_gradient)
print("Difference:", difference)

if np.allclose(actual_gradient, estimated_gradient,
               rtol=1e-4, atol=1e-6):
    print("PASS: Gradients match!")
else:
    print("FAIL: Gradients do not match!")