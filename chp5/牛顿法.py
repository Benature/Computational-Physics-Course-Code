# 请练习上面的程序。

# 参考解答。请注意，有时候不恰当的初始值会让程序找不着北在哪里。
from math import exp, sqrt, log
import matplotlib.pyplot as plt
import numpy as np


def func(x):
    y1 = 924.0*x**6-2772.0*x**5+3150.0*x**4 \
        - 1680*x**3+420.0*x**2-42.0*x+1
    return y1


def func_derivative(x):
    y2 = 5544.0*x**5 - 13860.0*x**4 + \
        12600.0*x**3 - 5040.0*x**2 + 840.0*x - 42
    return y2


N = 1000
x = np.linspace(0, 1, N)
y = []
for k in range(N):
    y.append(func(x[k]))
# 画出函数
plt.plot(x, y, "r")
plt.xlabel("x")
plt.ylabel("y")
# plt.ylim(-10,10)

a = 0.0
b = 1.0
# initial guess
x0s = np.array([0.02, 0.13, 0.35, 0.5, 0.8, 0.95])
N = len(x0s)
x_news = np.zeros(N)
y_news = np.ones(N)
eps = 1e-10
err = 0.2
for k in range(N):
    x0 = x0s[k]
    print("initial guess =  ", x0)
    # use while loop, if root error is small enough,
    # then move on to derive the next root
    while (err > eps):
        x_new = x0 - func(x0)*1.0/func_derivative(x0)
        # update the root error in the last step
        err = abs(x_new-x0)
        x0 = x_new
        # check the iterative results using print
        #print("x0 = ",x0)
    x_news[k] = x_new
    y_news[k] = func(x_new)
    err = 0.2  # reset the initial erro guess
    print("root          =  ", x_news[k])
plt.plot(x_news, y_news, "bo")
# 用牛顿法计算函数的根。
plt.show()
