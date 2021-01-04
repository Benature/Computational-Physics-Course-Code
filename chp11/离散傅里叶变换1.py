# 练习傅氏变换和逆变换calculate FFT of a sine curve
# and the inverse FFT
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

N = 32  # how about 31? 必须取偶数
xs = np.arange(N)
ts = xs/(N-1)*6*np.pi
ys = np.sin(ts)


# 进行傅里叶和逆傅里叶变换
F_y = rfft(ys)
y_new = irfft(F_y)

N = len(ys)
xs = np.arange(len(F_y))
fs = xs/N  # frequency

plt.figure()
plt.plot(fs, abs(F_y))
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.show()

plt.figure()
plt.plot(ts, ys, 'bo')
plt.plot(ts, y_new, 'r.')
plt.xlabel("t")
plt.ylabel("y")
plt.show()
