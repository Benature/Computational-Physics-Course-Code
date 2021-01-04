# 是用牛顿法，找到能够在复平面上收敛到z^3-1=0的实数根1的初始值位置。最后的结果是一个分型形状（fractal)

from math import exp, sqrt, log
import matplotlib.pyplot as plt
import numpy as np


def func(x):
    y1 = x**3.0-1.0
    return y1


def func_derivative(x):
    y2 = 3*x**2.0
    return y2+1e-15  # 为了避免导数等于0的情况


a = 0.0
b = 1.0
# initial guess
x0s = np.linspace(-2, 2, 1601)
xs, ys = np.meshgrid(x0s, x0s)

xs = xs.flatten()
ys = ys.flatten()
N = len(xs)

true_xs = np.zeros(N)
eps = 1e-3
err = 0.2
for k in range(N):
    x0 = complex(xs[k], ys[k])
    #print("initial guess =  ", x0)
    # use while loop, if root error is small enough,
    # then move on to derive the next root
    while (err > eps):
        x_new = x0 - func(x0)*1.0/func_derivative(x0)
        # update the root error in the last step
        err = abs(x_new-x0)
        x0 = x_new
        # check the iterative results using print
        #print("x0 = ",x0)
    err = 0.2  # reset the initial erro guess
    #print("root          =  ", x_new)
    if (abs(x_new-1.0)) < eps:
        true_xs[k] = 1.0

# 画出收敛到x=1.0的初始值在复空间的位置,可以看出占据了平面上约1/3的位置。另外2/3收敛到exp(i*2pi/3)和exp(-i*2pi/3)
plt.figure(figsize=(16, 16))
plt.plot(xs[true_xs == 1.0], ys[true_xs == 1.0], "k.")
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()
