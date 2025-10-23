import wave
import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa
from scipy.io.wavfile import write

# 1. Use simpleaudio to play a wav file in python.
# 2. Use import wave to open a wav file in python and extract the sound waveform

waveFile = wave.open('Noisy/Noisy.wav', 'rb')

numChannels = waveFile.getnchannels()
sampleWidth = waveFile.getsampwidth()
frameRate = waveFile.getframerate()
numframes = waveFile.getnframes()

frames = waveFile.readframes(numframes)
waveFile.close()

sound = np.frombuffer(frames, dtype=np.int16)

print(f"Channels: {numChannels}")
print(f"Frame Rate: {frameRate}")
print(f"Total Samples: {len(sound)}")

plt.figure(figsize=(10, 4))
plt.plot(sound[:5000])
plt.title("Waveform (first 5000 samples)")
plt.show()

# 3. Use FFT to determine the frequency of the noisy tone.

fftSpectrum = np.fft.fft(sound)
frequencies = np.fft.fftfreq(len(fftSpectrum), d=1/frameRate)
magnitude = np.abs(fftSpectrum)

plt.figure(figsize=(10, 4))
plt.plot(frequencies[:len(frequencies)//2], magnitude[:len(magnitude)//2])
plt.title("FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()

peakFrequency = frequencies[np.argmax(magnitude[:len(magnitude)//2])]
print("Dominant (noisy) frequency:", peakFrequency, "Hz")

# 4. Remove the noisy tone by replacing its amplitude by zero and do the inverse FFT.
filteredFFT = np.copy(fftSpectrum)

noiseBand = 50
filteredFFT[(frequencies > peakFrequency - noiseBand) & (frequencies < peakFrequency + noiseBand)] = 0
filteredFFT[(frequencies < -peakFrequency + noiseBand) & (frequencies > -peakFrequency - noiseBand)] = 0

# 5. Convert to the wav file

cleaned = np.fft.ifft(filteredFFT)
cleaned = np.real(cleaned).astype(np.int16)

write("Cleaned.wav", frameRate, cleaned)

play_obj = sa.play_buffer(cleaned, numChannels, sampleWidth, frameRate)
play_obj.wait_done()

# 6. Listen to the sound and you will hear the message if you have successfully removed the noisy tone.

# The message is "Congratulations, you have successfully removed the noise!"