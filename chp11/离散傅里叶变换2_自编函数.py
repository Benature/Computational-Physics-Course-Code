import numpy as np
import matplotlib.pyplot as plt
from cmath import rect, pi


def dft(y):
    N = len(y)
    c = np.empty(N//2, complex)

    for k in range(N//2):
        s = 0.0
        for n in range(N):
            s += rect(y[n], -2*np.pi*k*n/N)
        c[k] = s/N
    return c


# read data
y = np.loadtxt("../../data/11/pitch.dat", float)

plt.figure()
plt.plot(y)
plt.xlabel("t")
plt.ylabel("y")
plt.xlim(0, 200)  # 能着到一些高频言成分
plt.show()

# 进行离傅里叶变换, 并画出功率頭语图
plt.figure()
F_y = dft(y)
N = len(y)
xs = np.arange(len(F_y))
fs = xs/(N-1)  # frequency

plt.plot(fs, abs(F_y))
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.show()

# zoom in 频谱图
plt.figure()
plt.plot(fs, abs(F_y))
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.xlim(0.01, 0.02)
plt.show()

period_max = 1.0/fs[np.argmax(abs(F_y))]  # in year
print('strongest Power Peak at Period =', period_max, 'day')
