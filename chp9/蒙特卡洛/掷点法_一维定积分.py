# 蒙特卡罗积分参考程序
from math import sin
from random import random
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (np.sin(1/(x*(2-x))))**2


xs = np.arange(0, 2, 0.0001)

plt.figure(figsize=(10, 8))
plt.plot(xs, f(xs))
plt.xlabel("X")
plt.ylabel("Y")
xs1 = []  # 用来存储保存的点坐标
ys1 = []
xs2 = []  # 用来保存舍弃的点坐标
ys2 = []
N = 10000
count = 0
for i in range(N):
    x = 2*random()
    y = random()
    if y < f(x):
        count += 1
        xs1.append(x)
        ys1.append(y)
    else:
        xs2.append(x)
        ys2.append(y)

I = 2*count/N
plt.plot(xs1, ys1, 'r.')
plt.plot(xs2, ys2, 'y.')
plt.show()
print(I)  # 打印出积分值
