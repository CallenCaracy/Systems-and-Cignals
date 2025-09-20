import numpy as np

def median_filter(x):
    y = []
    for i in range(len(x)):
        if i == 0:
            window = [x[i], x[i], x[i + 1]]
        elif i == len(x) - 1:
            window = [x[i - 1], x[i], x[i]]
        else:
            window = [x[i - 1], x[i], x[i + 1]]
        y.append(np.median(window))
    return np.array(y)

# If not equal it is not linear
# x1 + x2 = [0, 1, 100, 0, 0]
#   i = 0 → [0,0,1] → median = 0
#   i = 1 → [0,1,100] → median = 1
#   i = 2 → [1,100,0] → sorted [0,1,100] → median = 1
#   i = 3 → [100,0,0] → sorted [0,0,100] → median = 0
#   i = 4 → [0,0,0] → median = 0

# Test Linearity
x1 = np.array([0, 0, 100, 0, 0])
x2 = np.array([0, 1, 0, 0, 0])

y1 = median_filter(x1)
y2 = median_filter(x2)
y3 = median_filter(x1 + x2)
linear_check = np.allclose(y3, y1 + y2)

print("Linearity test:")
print("y1 + y2:", y1 + y2)
print("y3 (filter(x1+x2)):", y3)
print("Linear?", linear_check)

# Test Time-Invariance
# Shift input by 1 sample
x1_shifted = np.roll(x1, 1)
y_shifted = median_filter(x1_shifted)
y1_delayed = np.roll(y1, 1)
time_invariant = np.allclose(y_shifted, y1_delayed)

print("\nTime-Invariance test:")
print("y_shifted:", y_shifted)
print("y1 delayed:", y1_delayed)
print("Time-Invariant?", time_invariant)

# Test Causality
# Check if output depends on future sample (x[n+1])
# Our filter uses x[n+1] meaning its non-causal
causal = False
print("\nCausality test:")
print("Causal?", causal) 

# Test Stability
# Bounded input leads to bounded output? Yes, median of bounded numbers is bounded
bounded_input = np.array([0, 1, 100, -50, 0])
bounded_output = median_filter(bounded_input)
stable = np.all(np.abs(bounded_output) <= np.max(np.abs(bounded_input)))

print("\nStability test:")
print("Input:", bounded_input)
print("Output:", bounded_output)
print("Stable?", stable) 