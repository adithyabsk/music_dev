import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave

import pickle

# data1 = None
# rate1 = 44100
# with open('data.pkl', 'rb') as fopen:
#     data1 = pickle.load(fopen)

# 
# plt.figure()
# print(data1)
# plt.plot(np.arange(data1.size), data1)
# plt.figure()
# 
rate, data = wave.read('e_harm3.wav')
# plt.plot(np.arange(data.size), data)
# plt.show()
# 
# quit()

print(rate)
print(data)
spectre = np.fft.fft(data)
freq = np.fft.fftfreq(data.size, 1/rate)
mask = freq > 0
print(freq[np.argmax(np.abs(spectre[mask]))])
plt.plot(freq[mask], np.abs(spectre[mask]))

# plt.figure()
# spectre1 = np.fft.fft(data1)
# freq1 = np.fft.fftfreq(data1.size, 1/rate1)
# mask1 = freq1 > 0
# print(np.argmax(np.abs(spectre1[mask1])))
# plt.plot(freq1[mask1], np.abs(spectre1[mask1]))

plt.show()
