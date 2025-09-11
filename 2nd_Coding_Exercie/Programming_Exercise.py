import numpy as np
import matplotlib.pyplot as plt

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

x1 = np.array([0, 0, 100, 0, 0])
x2 = np.array([0, 1, 0, 0, 0])

y1 = median_filter(x1)
y2 = median_filter(x2)
y3 = median_filter(x1 + x2)
validate = y1 + y2

print("y3:", y3)
print("y3Validate:", validate)
print("equal?", np.allclose(y3, validate))
# If not equal it is not linear
# x1 + x2 = [0, 1, 100, 0, 0]
#   i = 0 → [0,0,1] → median = 0
#   i = 1 → [0,1,100] → median = 1
#   i = 2 → [1,100,0] → sorted [0,1,100] → median = 1
#   i = 3 → [100,0,0] → sorted [0,0,100] → median = 0
#   i = 4 → [0,0,0] → median = 0

plt.plot(x1, label="x1 original")
plt.plot(y1, label="y1 median filtered")
plt.plot(x2, label="x2 original")
plt.plot(y2, label="y2 median filtered")
plt.legend()
plt.show()