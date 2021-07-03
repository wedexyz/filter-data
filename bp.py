

import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read('ecg.wav')
times = np.arange(len(data))/sampleRate
print(sampleRate,data.shape)
print(times)


# apply a 3-pole lowpass filter at 0.1x Nyquist frequency
b, a = scipy.signal.butter(3, 0.1)
filtered = scipy.signal.filtfilt(b, a, data)

b, a = scipy.signal.butter(3, 0.05, 'lowpass')
filteredLowPass = scipy.signal.filtfilt(b, a, data)

b, a = scipy.signal.butter(3, 0.05, 'highpass')
filteredHighPass = scipy.signal.filtfilt(b, a, data)

b, a = scipy.signal.butter(3, [.01, .05], 'band')
filteredBandPass = scipy.signal.lfilter(b, a, data)



# plot the original data next to the filtered data

plt.figure(figsize=(10, 4))

plt.subplot(151)
plt.plot(times, data)
plt.title("ECG Signal with Noise")
plt.margins(0, .05)

plt.subplot(152)
plt.plot(times, filtered)
plt.title("Filtered ECG Signal")
plt.margins(0, .05)

plt.subplot(153)
plt.plot(times, filteredLowPass)
plt.title("Filtered lowpass")
plt.margins(0, .05)
plt.tight_layout()

plt.subplot(154)
plt.plot(times, filteredHighPass)
plt.title("filteredHighPass")
plt.margins(0, .05)
plt.tight_layout()

plt.subplot(155)
plt.plot(times,filteredBandPass)
plt.title("filteredBandPass")
plt.margins(0, .05)
plt.tight_layout()



plt.show()