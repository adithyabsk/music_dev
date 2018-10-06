import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave

import pickle

data1 = None
with open('data.pkl', 'rb') as fopen:
    data1 = pickle.load(fopen)

plt.figure()
print(data1)
plt.plot(np.arange(data1.size), data1)
plt.figure()

rate, data = wave.read('delme_rec_unlimited_i9c2rjkt.wav')
plt.plot(np.arange(data.size), data)
plt.show()

quit()
# print(rate)
# print(data)
# spectre = np.fft.fft(data)
# freq = np.fft.fftfreq(data.size, 1/rate)
# mask = freq > 0   
# # plt.plot(freq[mask], np.abs(spectre[mask]))
# plt.show()
# 