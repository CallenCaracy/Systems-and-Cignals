import numpy as np
import matplotlib.pyplot as plt

# Convolution by hand (but in Python so it doesn't whine)
# System: y[n] = 0.5*(x[n] + x[n-1])
# Impulse response: h[n] = 0.5*delta[n] + 0.5*delta[n-1] -> h = [0.5, 0.5] for n=0,1
x = [1, 2, 3]   # x[0], x[1], x[2]
h = [0.5, 0.5]  # h[0], h[1]

len_y = len(x) + len(h) - 1
y = [0.0] * len_y

print("Impulse response: h[n] = 0.5·δ[n] + 0.5·δ[n-1]  ->  h = [0.5, 0.5]\n")
print("Convolution sum steps (y[n] = sum_k x[k] * h[n-k]):\n")

for n in range(len_y):
    terms = []
    y_n = 0.0
    kmin = max(0, n - (len(h)-1))
    kmax = min(len(x)-1, n)
    for k in range(kmin, kmax + 1):
        hk = h[n - k]
        term = x[k] * hk
        terms.append(f"x[{k}]·h[{n-k}] = {x[k]}·{hk} = {term}")
        y_n += term
    y[n] = y_n
    if terms:
        print(f"n = {n}: " + " + ".join(terms) + f"  =>  y[{n}] = {y_n}")
    else:
        print(f"n = {n}: no overlap (all zeros)  =>  y[{n}] = 0.0")

print("\nFull output signal y[n] (n=0..{0}): {1}".format(len_y-1, y))
