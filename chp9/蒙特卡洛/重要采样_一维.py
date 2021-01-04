# 请练习使用important sampling的方法来求解上面的积分，并且把结果和平均值法作比较
# 参考答案在下面的单元。
# important sampling
# 使用重要抽样法来求积分
import scipy.integrate as integrate
from math import sin, exp
from random import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2.0/(np.exp(x)+1)


def p():
    # x = random()*(np.sqrt(2)-1) + 1
    # x = random() + 1
    x = random()
    x = x**2
    return x


xs = []
N = 1000
# for j in range(1):
xs = []
tot = 0
for i in range(N):
    x = p()
    xs.append(x)
    tot += f(x)
I = tot/N
print(I)  # 打印出积分值


plt.figure()
plt.plot(xs, '.')
plt.ylabel("Xs")
plt.show()


# def f0(x):
#     return (x**(-0.5) / (np.exp(x)+1))


# a = integrate.quad(f0, 1, 2)
# print(a)
