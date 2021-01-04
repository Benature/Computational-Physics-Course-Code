# 无量纲化没做
# 把x=0定义为两侧波函数的交汇点，测试不同E值下，交汇点的
# 波函数值psi和其导数phi需要相等。在测试phi是否连续之前需要把两侧
# 的波函数值psi先scale到一样大小。
# 改正后的牛顿法, Anhamonic potential
from numpy import array, arange
import math
import matplotlib.pyplot as plt
# %matplotlib inline

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
a = 1e-11
L1 = -10*a  # 波函数积分左边界
# L2 = 0*a  # 波函数积分交汇点
L2 = 10.0*a  # 波函数积分右边界
N = 1000
h = (L2-L1)/N

# Potential function
V0 = 50*e


def V(x):
    return V0*x**2 / a**2


print('E0 from analytical:', 0.5 * hbar * math.sqrt(2.0*V0/a**2/m)/e)


def f(r, x, E):
    '''薛定谔加速方程'''
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi, fphi], float)

# 从左边界开始积分
# 返回merge点的波函数psi和其导数phi


def solve(E):
    psi = 0.0  # 左边界初始值
    phi = 1.0
    r = array([psi, phi], float)

    for x in arange(L1, L2, h):
        k1 = h*f(r, x, E)
        k2 = h*f(r+0.5*k1, x+0.5*h, E)
        k3 = h*f(r+0.5*k2, x+0.5*h, E)
        k4 = h*f(r+k3, x+h, E)
        r += (k1+2*k2+2*k3+k4)/6
    return r[0]


# Main program to find the energy using the secant method
E1 = 0*e
E2 = 100*e
# E1 = 100*e
# E2 = 300*e
#E1 = 300.0*e
#E2 = 800*e
# E1 = 1000.0*e
# E2 = 1600.0*e

psi2 = solve(E1)

target = e/1000
while abs(E1-E2) > target:
    psi1, psi2 = psi2, solve(E2)
    E1, E2 = E2, E2 - psi2 * (E2-E1)/(psi2-psi1)

print(E1/e)
print(E2/e)

xs = arange(L1, L2, h)
ys = arange(L1, L2, h)
QN = 4
E = E2 * (QN*2+1)
total_probability = 0

i = 0
psi0 = 0.0
phi0 = 1.0
r = array([psi0, phi0], float)

# 下面计算波函数
for x in arange(L1, L2, h):
    k1 = h*f(r, x, E)
    k2 = h*f(r+0.5*k1, x+0.5*h, E)
    k3 = h*f(r+0.5*k2, x+0.5*h, E)
    k4 = h*f(r+k3, x+h, E)
    r += (k1+2*k2+2*k3+k4)/6
    ys[i] = r[0]
    total_probability += abs(ys[i])**2*h
    i = i+1

ys = ys/math.sqrt(total_probability)
plt.figure(figsize=(8, 8))
plt.plot(xs/a, ys, 'o-')
plt.xlabel('x (L)')
plt.ylabel(r'$\Psi$')
plt.grid()
plt.figure(figsize=(8, 8))
plt.plot(xs/a, ys*ys, 'o-')
plt.xlabel('x (L)')
plt.ylabel(r'Probability')
plt.grid()
plt.show()
