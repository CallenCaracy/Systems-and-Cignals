import numpy as np

def echo_system(x):
    # y[n] = x[n] + 0.5 ∙ x[n-4]
    # The output is the original signal plus a half-strength echo from 4 samples ago.
    y = np.zeros_like(x, dtype=float)
    for n in range(len(x)):
        y[n] = x[n]
        if n >= 4:
            y[n] += 0.5 * x[n-4]
    return y

# Example input
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = echo_system(x)
print("Input x:", x)
print("Output y:", y)
