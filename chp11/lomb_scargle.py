# 练习上面的问题.
# 举例：读入视向速度数据，使用lomb-scargle算法求离散且非均匀采样数据的周期功率谱
# 然后找出其中最强的周期性信号的周期。
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

# load data
datum = np.loadtxt('../../data/10/data_fitting_planet1.txt')
#datum = np.loadtxt('data_fitting_planet2.txt')

x = datum[:, 0]
y = datum[:, 1]
yerr = datum[:, 2]

plt.figure()
plt.plot(x, y)
plt.show()

f = np.linspace(0.1, 10, 1000)  # 要搜寻的频率域
pgram = signal.lombscargle(x, y, f, normalize=True)  # FOCUS!
# 找到功率最高的地方，计算出对应周期，in orginal 时间的单位
period_max = 2.0*np.pi/f[np.argmax(pgram)]
print("New Period =  ", period_max)
plt.figure(figsize=(6, 6))
plt.plot(2.0*np.pi/f, pgram)
plt.xlim(0, 10)
plt.xlabel("Period (day)")
plt.ylabel("Power")
plt.show()
