# 模拟退火法求函数极值1
import numpy as np
from random import random, randrange
from math import exp, pi, cos
import matplotlib.pyplot as plt


def f(x):
    return x**2-cos(4*pi*x)


N = 1000
xs = np.linspace(-3, 3, N)
ys = np.zeros(N)
xss = []
yss = []

for i in range(N):
    ys[i] = f(xs[i])

# initial guess red dot
x1 = 2.0
f1 = f(x1)
plt.figure()
plt.plot(xs, ys)
plt.plot(x1, f(x1), 'ro')
plt.xlabel("X")
plt.ylabel("f(x)")

Tin = 10  # initial temperature
tstep = 15
mu, sigma = 0, 0.3
nstep = 100
for j in range(tstep):
    for i in range(nstep):
        s = np.random.normal(mu, sigma, 1)
        f2 = f(x1+s)
        df = f2 - f1
        if df < 0 or random() < exp(-df/Tin):
            xss.append(x1)
            yss.append(f1)
            x1 = x1+s  # update current x value
            f1 = f2  # update current f value
    Tin = Tin/1.5  # slowly dropping temperature

plt.plot(x1, f1, 'bo')
plt.show()
plt.figure()
plt.plot(yss, 'o-')
plt.xlabel("Trials")
plt.ylabel("f(x) values")
plt.show()
plt.figure()
plt.plot(xss, 'o-')
plt.xlabel("Trials")
plt.ylabel("Xs values")
plt.show()
