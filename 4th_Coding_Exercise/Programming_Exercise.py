import numpy as np
import matplotlib.pyplot as plt

# Time Array
t = np.linspace(0, 4 * np.pi, 1000)
y = np.zeros_like(t)

# Number of harmonics to add
num_harmonics = 10

# Loop to add harmonics based on the recipe
for i in range(num_harmonics):
    k = 2 * i + 1 # k = 1, 3, 5, ...
    y += (4 / (k * np.pi)) * np.sin(k * t)
    
# Plot the result
plt.plot(t, y)
plt.title(f'Square Wave Synthesis ({num_harmonics} terms)')
plt.show()