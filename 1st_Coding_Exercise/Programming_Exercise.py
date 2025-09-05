import numpy as np
import matplotlib.pyplot as plt

fs = 8000   # frequency sample
dur = 0.5   # duration
f = 440    # frequency

N = int(fs * dur)
n = np.arange(N)
x = np.sin(2*np.pi*f*n/fs)

noise_strenght = 0.5
noise = noise_strenght * np.random.randn(N)
x_noisy = x + noise

# Moving average with window length 𝐿 = 5:
𝐿 = 5
h = np.ones(L) / L
y = np.convolve(x_noisy, h, mode='same')

plt.figure(figsize=(10, 4))
plt.plot(n[:200], x_noisy[:200], label="Noisy Signal", alpha=0.6)
plt.plot(n[:200], y[:200], label="Smoothed Signal", linewidth=2)
plt.xlabel("Sample number")
plt.ylabel("Amplitude")
plt.title("Discrete-time Sine Wave")
plt.grid(True)
plt.show()