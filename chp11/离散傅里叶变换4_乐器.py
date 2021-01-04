# 处理乐器的采样数据
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

y1 = np.loadtxt("../../data/11/piano.txt")
y2 = np.loadtxt("../../data/11/trumpet.txt")

plt.figure()
plt.plot(y1)
plt.xlabel('Time')
plt.ylabel("Strength")
plt.title("Piano Note")
plt.show()

plt.figure()
plt.plot(y2)
plt.xlabel('Time')
plt.ylabel("Strength")
plt.title("Trumpet Note")
plt.show()

F_y = rfft(y1)
N = len(y1)
xs = np.arange(len(F_y))
fs = xs/(N-1)  # frequency
plt.figure()
plt.plot(fs, abs(F_y))
plt.xlim(0, 0.1)
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.title("Piano Frequency")
plt.show()


F_y = rfft(y2)
N = len(y2)
xs = np.arange(len(F_y))
fs = xs/(N-1)  # frequency
plt.figure()
plt.plot(fs, abs(F_y))
plt.xlim(0, 0.1)
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.title("Trumpet Frequency")
plt.show()
