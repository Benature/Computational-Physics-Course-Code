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
L2 = 0*a  # 波函数积分交汇点
L3 = 10.0*a  # 波函数积分右边界
N = 2000
h = (L2-L1)/N

# Potential function
V0 = 50*e


def V(x):
    return V0*x**4/a**4


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


def solve1(E):
    psi = 0.0  # 左边界初始值
    phi = 1.0
    r = array([psi, phi], float)

    for x in arange(L1, L2, h):
        k1 = h*f(r, x, E)
        k2 = h*f(r+0.5*k1, x+0.5*h, E)
        k3 = h*f(r+0.5*k2, x+0.5*h, E)
        k4 = h*f(r+k3, x+h, E)
        r += (k1+2*k2+2*k3+k4)/6
    return r


def solve2(E):
    '''从右边界开始积分
    返回merge点的波函数psi和其导数phi'''
    psi = 0.0  # 右边界初始值
    phi = 1.0
    r = array([psi, phi], float)

    for x in arange(L3, L2, -h):
        k1 = -h*f(r, x, E)
        k2 = -h*f(r+0.5*k1, x-0.5*h, E)
        k3 = -h*f(r+0.5*k2, x-0.5*h, E)
        k4 = -h*f(r+k3, x-h, E)
        r += (k1+2*k2+2*k3+k4)/6
    return r


# Main program to find the energy using the secant method
E1 = 1.0*e
E2 = 300*e
#E1 = 300.0*e
#E2 = 800*e
#E1 = 1000.0*e
#E2 = 1600.0*e

psi10, phi10 = solve1(E1)
psi20, phi20 = solve2(E1)
scalefactor = psi20/psi10
psi10 *= scalefactor
phi10 *= scalefactor
delta_phi1 = phi20-phi10
target = e/1000
while abs(E1-E2) > target:
    psi10, phi10 = solve1(E2)
    psi20, phi20 = solve2(E2)
    scale_factor = psi20/psi10
    psi10 *= scalefactor
    phi10 *= scalefactor
    delta_phi2 = phi20-phi10  # 根据交界处的phi值是否相等来确定本征态能量.
    E1, E2 = E2, E2-delta_phi2*(E2-E1)/(delta_phi2-delta_phi1)
    delta_phi1 = delta_phi2

print("E0 from code =", E2/e, "eV")

# 如果你只需要本征能量，可以结束计算了，E2,或者(E1+E2)/2.0就是你的结果。
# 下面都是画图和波函数(概率密度)的计算。
# 利用计算出来的本征能量值，分别求解交汇点左边和右边的波函数，
# 然后利用交汇点的比值scalefactor把两边的波函数归一化,再画图。

# 左边的波函数初始化
xs1 = arange(L1, L2, h)
psis1 = arange(L1, L2, h)
phis1 = arange(L1, L2, h)
# 右边的波函数初始化
xs2 = arange(L3, L2, -h)
psis2 = arange(L1, L2, h)
phis2 = arange(L1, L2, h)

E = E2  # 赋予本征态能量, Eigenvalue of the Energy level from Newton's method
total_probability = 0  # 用来归一化概率密度的总概率值变量
i = 0
psi0 = 0.0
phi0 = 1.0
r = array([psi0, phi0], float)  # 初始的波函数和其导数的值。

# 下面计算左边的波函数
for x in arange(L1, L2, h):
    k1 = h*f(r, x, E)
    k2 = h*f(r+0.5*k1, x+0.5*h, E)
    k3 = h*f(r+0.5*k2, x+0.5*h, E)
    k4 = h*f(r+k3, x+h, E)
    r += (k1+2*k2+2*k3+k4)/6
    psis1[i] = r[0]
    phis1[i] = r[1]
    i = i+1

psim_left = r[0]  # 从左向右积分的交汇处的波函数和导数值
phim_left = r[1]  # 从左向右积分的交汇处的波函数和导数值
psi0 = 0.0
phi0 = 1.0
i = 0
r = array([psi0, phi0], float)   # #初始的波函数和其导数的值。

# 下面计算右边的波函数
for x in arange(L3, L2, -h):
    k1 = -h*f(r, x, E)
    k2 = -h*f(r+0.5*k1, x-0.5*h, E)
    k3 = -h*f(r+0.5*k2, x-0.5*h, E)
    k4 = -h*f(r+k3, x-h, E)
    r += (k1+2*k2+2*k3+k4)/6
    psis2[i] = r[0]
    phis2[i] = r[1]
    i = i+1
psim_rightt = r[0]  # 从右向左积分的交汇处的波函数和导数值
phim_rightt = r[1]  # 从右向左积分的交汇处的波函数和导数值
scale_factor = psim_left/psim_rightt  # 把两侧的波函数乘上一个系数，协调一致
psis2 *= scale_factor
phis2 *= scale_factor

#ys = ys/math.sqrt(total_probability)
plt.figure(figsize=(8, 8))
plt.plot(xs1/a, psis1, 'o-')
plt.plot(xs2/a, psis2, 'o-')
# plt.xlim(-5,5)
plt.xlabel('x (L)')
plt.ylabel(r'$\Psi$')
plt.grid()
plt.figure(figsize=(8, 8))
plt.plot(xs1/a, psis1**2, 'o-')
plt.plot(xs2/a, psis2**2, 'o-')
plt.xlabel('x (L)')
plt.ylabel(r'Probability')
plt.grid()
plt.show()
