from scipy import optimize
import math
import numpy as np
from matplotlib import pyplot as plt
from integrate import simpsons, gauss

A = 1.0  # 面积
h = 6.62607004e-34  # m2 kg / s plunk
c = 299792458  # m / s light speed
K_B = 1.38064852e-23  # m2 kg s-2 K-1 玻尔兹曼常数

lambd1 = 390e-9
lambd2 = 750e-9

invphi = (math.sqrt(5) - 1) / 2  # 1/phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1/phi^2


def gssrec(f, a, b, tol=1e-5, h=None, c=None, d=None, fc=None, fd=None):
    (a, b) = (min(a, b), max(a, b))
    if h == None:
        h = b-a
    if h <= tol:
        return (a, b)  # 跳出
    if c == None:
        c = a + invphi2*h
    if d == None:
        d = a + invphi*h
    if fc == None:
        fc = f(c)
    if fd == None:
        fd = f(d)
    if fc < fd:
        return gssrec(f, a, d, tol, h*invphi, c=None, fc=None, d=c, fd=fc)
    else:
        return gssrec(f, c, b, tol, h*invphi, c=d, fc=fd, d=None, fd=None)


def I(lambd, T):
    return 2 * np.pi * A * h * c**2 / lambd**5 / (np.exp(h*c / (lambd*K_B*T)) - 1)


def I2(z, T):
    C1 = K_B * T / (h * c)
    x = z/(1-z)
    return 1 * 2 * np.pi * A * h * c**2 * C1**4 * (x**3 / (np.exp(x)-1)) / (1-z)**2


def get_zeta(T):
    # print(T)
    I_l12 = simpsons(lambda l: I(l, T), lambd1, lambd2, 100)
    I01 = gauss(lambda z: I2(z, T))
    zeta = I_l12 / I01
    return zeta


result = gssrec(lambda t: -get_zeta(t), 4000, 10000)
# result = optimize.minimize_scalar(iget_zeta, (4000, 10000), method='Golden')
print(result)


# Temperature = np.linspace(300, 10000)
# zetas = []
# for T in Temperature:
#     # I_l12 = simpsons(lambda l: I(l, T), lambd1, lambd2, 100)
#     # I01 = gauss(lambda z: I2(z, T))
#     # zeta = I_l12 / I01
#     zeta = get_zeta(T)
#     zetas.append(zeta)

# print("\n\n\n")
# plt.plot(Temperature, zetas)
# plt.show()
