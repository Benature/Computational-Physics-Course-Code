# 举例：boot-strapping测试
# 使用lomb-scargle算法求离散且非均匀采样视向速度数据的周期功率谱
# 然后找出其中最强的周期性信号的周期,然后使用boot-strapping算法来测试你找到的信号的强度和周期信号的可靠性
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

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
pgram = signal.lombscargle(x, y, f, normalize=True)
period_max = 2.0*np.pi/f[np.argmax(pgram)]  # in day
print("New Period =  ", period_max)
plt.figure(figsize=(6, 6))
plt.plot(2.0*np.pi/f, pgram)
plt.xlabel("Period (day)")
plt.ylabel("Power")
plt.xlim(0, 5)
plt.show()

# boot strapping算法 FOCUS!
index = np.random.permutation(len(y))
x_new = x[index]
y_new = y

plt.figure()
plt.plot(x_new, y_new, '.')
plt.show()

f = np.linspace(0.1, 10, 1000)  # 要搜寻的频率域
pgram2 = signal.lombscargle(x_new, y_new, f, normalize=True)
period_max = 2.0*np.pi/f[np.argmax(pgram2)]  # in day
print("New Period =  ", period_max)
plt.figure(figsize=(6, 6))
plt.plot(2.0*np.pi/f, pgram2)
plt.plot(2.0*np.pi/f, pgram)

plt.xlabel("Period (day)")
plt.ylabel("Power")
plt.xlim(0, 5)
plt.show()
