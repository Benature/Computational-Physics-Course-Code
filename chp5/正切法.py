# 请练习上面的习题，使用正切法。注意你需要的初始值要比牛顿法多一个。

import numpy as np
import matplotlib.pyplot as plt
G = 6.674e-11  # m^3 kg^-1 s^-2
M = 5.974e24  # kg
m = 7.348e22  # kg
R = 3.844e8  # m
omega = 2.662e-6  # s^-1

# L0 = (G*(M - m)/(omega))**(1/3)
# print(L0)


def f(r):
    return G*M/(r**2) - G*m/((R-r)**2) - omega**2 * r


xs = np.linspace(0, R, 50)

# x0 = R/2 + 1e5
x1 = R/2
for i in range(30):
    x0 = x1 - R*0.001
    delta = f(x1) * (x1 - x0)/(f(x1) - f(x0))
    x2 = x1 - delta

    x0 = x1
    x1 = x2

    # delta = (f(x1)-f(x1-0.001*R))/(0.001*R)
    # x1 = x1-f(x1)/delta
print(x1)
