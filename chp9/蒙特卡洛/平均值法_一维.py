# 练习：请编程使用平均值法来求上面撒点法要求的积分。
# 蒙特卡罗积分 参考程序
from math import sin
from random import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (np.sin(1/(x*(2-x))))**2


N = 10
xs = []
tot = 0
for i in range(N):
    x = 2*random()
    xs.append(x)
    tot += f(x)

plt.plot(xs, '.')
plt.ylabel("X")
plt.show()
I = 2*tot/N
print(I)  # 打印出积分值
