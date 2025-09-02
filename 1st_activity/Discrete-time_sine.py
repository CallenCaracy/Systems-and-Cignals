import numpy as np
import matplotlib.pyplot as plt

fs = 8000   # frequency sample
dur = 0.5   # duration
f = 4500    # frequency

# If (f * 2) is greater than fs it violates fs >= 2fmax thus the cignal is meaningless
# “If the signal frequency f exceeds fs/2, it violates the Nyquist criterion, causing aliasing. The sampled signal will not correctly represent the original sine wave.”

N = int(fs * dur)
n = np.arange(N)
x = np.sin(2*np.pi*f*n/fs)

plt.figure(figsize=(10, 4))
plt.plot(n[:50], x[:50])
plt.xlabel("Sample number")
plt.ylabel("Amplitude")
plt.title("Discrete-time Sine Wave")
plt.grid(True)
plt.show()