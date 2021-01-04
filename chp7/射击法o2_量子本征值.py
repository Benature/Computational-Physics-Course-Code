import matplotlib.pyplot as plt
import numpy as np

m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
L = 5.2918e-11     # Bohr radius

# 注意,解析解，能量本征值 = 0.5*hbar**2*np.pi**2/L**2/m/e， 单位是电子伏.
print('E的基态能量解析解 =  ', 0.5 * hbar**2 * np.pi**2 / L**2 / m / e, 'ev')

N = 1000
h = L/N


# def rk4(t, x, f, dt, arg=None):
#     '''RK4'''
#     dx1 = f(t, x, *arg)*dt
#     dx2 = f(t+0.5*dt, x+0.5*dx1, *arg)*dt
#     dx3 = f(t+0.5*dt, x+0.5*dx2, *arg)*dt
#     dx4 = f(t+dt, x+dx3, *arg)*dt
#     return x+dx1/6.0+dx2/3.0+dx3/3.0+dx4/6.0


V0 = 100 * e


def V(x):  # 势能方程
    # return 0.0
    return V0 * (x/L) * (x/L - 1)


def f(r, x, E):  # 薛定谔加速方程
    psi, phi = r
    fpsi = phi
    fphi = (2*m/hbar**2) * (V(x)-E)*psi
    return np.array([fpsi, fphi], float)

# Calculate the wavefunction for a particular energy
# 右边边界


def solve(E):
    psi = 0.0
    phi = 1.0
    r = np.array([psi, phi], float)
    for x in np.arange(0, L, h):
        # r += rk4(r, x, f, h, arg=[E])
        k1 = h * f(r, x, E)
        k2 = h * f(r + 0.5 * k1, x + 0.5*h, E)
        k3 = h * f(r + 0.5 * k2, x + 0.5*h, E)
        k4 = h * f(r + k3, x + h, E)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return r[0]


# Main progress to find the energy using the secant method
E1 = 0.0 * e
E2 = 200 * e
target = e/10000

# method 1
# 用差分替代导数的牛顿法
psi2 = solve(E1)
while abs(E1-E2) > target:
    psi1, psi2 = psi2, solve(E2)
    E1, E2 = E2, E2 - psi2*(E2-E1)/(psi2-psi1)

# # method 2
# psi1 = solve(E1)
# psi2 = solve(E2)
# while abs(E2-E1) > target:
#     E = (E1 + E2)/2
#     # print(E/e, '\t', E1/e, '\t', E2/e)
#     psi = solve(E)
#     if psi1 * psi > 0.:
#         psi1, E1 = psi, E
#     else:
#         psi2, E2 = psi, E

print(E2/e)
print(E1/e)

xs = np.arange(0, L, h)
ys = np.arange(0, L, h)
E = E2*4
total_probability = 0.0
i = 0
psi0 = 0.0
phi0 = 1.0
r = np.array([psi0, phi0], float)

for x in np.arange(0, L, h):
    k1 = h * f(r, x, E)
    k2 = h * f(r + 0.5 * k1, x+0.5*h, E)
    k3 = h * f(r + 0.5 * k2, x+0.5*h, E)
    k4 = h * f(r + k3, x+h, E)
    r += (k1 + 2 * k2 + 2*k3 + k4)/6
    ys[i] = r[0]

    total_probability += abs(ys[i])**2*h
    i = i+1

ys = ys/np.sqrt(total_probability)
plt.figure(figsize=(8, 8))
plt.plot(xs/L, ys, 'o-')
plt.xlabel('x(L)')
plt.ylabel(r'$\Psi$')
plt.grid()

plt.figure(figsize=(8, 8))
plt.plot(xs/L, ys*ys, 'o-')
plt.xlabel('x(L)')
plt.ylabel('probability')
plt.grid()
plt.show()
