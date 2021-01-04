# 读入pitch.dat数据，共然后使用python自带的 numpy.fft.rfft来进行离散傅里叶变换和逆变换的练习
from cmath import rect, pi
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

# 读入数据
y = np.loadtxt("../../data/11/pitch.dat", float)
# y = np.loadtxt("pitch.dat", float)
plt.figure()
plt.plot(y)
plt.xlabel("t")
plt.ylabel("y")
plt.show()

# 使用rfft进行离散傅里叶变换，并画出功率频谱图
plt.figure()
F_y = rfft(y)
N = len(y)
xs = np.arange(len(F_y))
fs = xs/N  # frequency
plt.plot(fs,  abs(F_y))
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.show()
# zoom in频谱图。
plt.figure()
plt.plot(fs,  abs(F_y))
plt.ylabel("Power")
plt.xlabel("Frequency")
plt.xlim(0.01, 0.1)
plt.show()

# 逆傅里叶变换
y_new = irfft(F_y)
plt.figure()
plt.plot(y, 'bo')  # 蓝色点代表原始数据
plt.plot(y_new, 'r.')  # 红色点代表傅氏逆变换恢复的数据
plt.xlabel("t")
plt.ylabel("y")
plt.show()
# 最后可以看到，逆变换确实可以恢复我们的原始数据，红色和蓝色点基本重合到了一起
