import numpy as np

# Exercise 2: Conceptual Question 
#   If you have an audio signal and you convolve it with an impulse 
#   response h[n] that represents an echo, you get an audio signal with an echo. 
#   Based on the commutative property of convolution, what would you expect 
#   to get if you convolved the echo impulse response with the audio 
#   signal? Explain your reasoning.

# Answer:   
#           You’d still get the same echoed audio. 
#           Commutativity ensures the audio with echo doesn’t change, no matter which way you order the convolution.

#  Exercise 3

def convolve1d(x, h):
    
    Lx = len(x)
    Lh = len(h)
    Ly = Lx + Lh - 1
    y = np.zeros(Ly)

    # Convolution sum
    for n in range(Ly):
        for k in range(Lx):
            if 0 <= n - k < Lh:
                y[n] += x[k] * h[n - k]
    return y


x = np.array([1, 2, 3])
h = np.array([0.5, 0.5])

print("x:", x)
print("h:", h)
print("y:", convolve1d(x, h))