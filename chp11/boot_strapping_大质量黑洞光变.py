# 上面问题的程序。
# 举例：读入大质量黑洞的光变数据，使用lomb-scargle算法求离散且非均匀采样数据的周期功率谱
# 然后找出其中最强的周期性信号的周期。
# 同时使用boot strapping算法来测试周期信号强度
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

datum = np.loadtxt("../../data/11/catalina_PKS0157+011.csv",
                   delimiter=',', skiprows=1)
#datum = np.loadtxt("catalina_um234.csv", delimiter=',',skiprows=1)
x = datum[:, 5]  # observing time
y = datum[:, 1]  # magnitude of AGN

# 画出时间-光变曲线图
plt.figure()
plt.plot(x, y, '.')
plt.show()

f = np.linspace(0.002, 0.1, 1000)  # 要搜寻的频率域
pgram = signal.lombscargle(x, y, f, normalize=False)
period_max = 2.0*np.pi/f[np.argmax(pgram)]  # in day
print("New Period =  ", period_max)
plt.figure(figsize=(6, 6))
plt.plot(2.0*np.pi/f, pgram)
plt.xlabel("Period (day)")
plt.ylabel("Power")
plt.xlim(0, 3000)
plt.show()

# boot strapping算法
index = np.random.permutation(len(y))
x_new = x[index]
y_new = y

plt.figure()
plt.plot(x_new, y_new, '.')
plt.show()

f = np.linspace(0.002, 0.1, 1000)  # 要搜寻的频率域
pgram2 = signal.lombscargle(x_new, y_new, f, normalize=False)
period_max = 2.0*np.pi/f[np.argmax(pgram2)]  # in day
print("New  Period =  ", period_max)
plt.figure(figsize=(6, 6))
plt.plot(2.0*np.pi/f, pgram2)
plt.plot(2.0*np.pi/f, pgram)

plt.xlabel("Period (day)")
plt.ylabel("Power")
plt.xlim(0, 3000)
plt.show()
