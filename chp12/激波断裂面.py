import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
# 求解Burgers方程。
# 初始条件为exp(-(x-1)^2)之间的正弦函数,加了耗散项
L = 10
nx = 201
dx = L/(nx-1)
dt = 0.05

x = np.linspace(0, L, nx)
un = np.empty(nx)

# initial condition
u = np.array(np.exp(-(x-3)**2))

plt.figure(figsize=(8, 6), dpi=100)
plt.plot(x, u, marker='o', lw=2, label='Initial Condition')
plt.xlim([0, L])
plt.legend()
plt.xlabel("X")
plt.ylabel("u")
plt.show()

# 特征线

plt.figure(figsize=(8, 6), dpi=100)
i0 = 0
plt.plot(x, (x-x[i0])/u[i0])
i0 = 20
plt.plot(x, (x-x[i0])/u[i0])
i0 = 40
plt.plot(x, (x-x[i0])/u[i0])
i0 = 60
plt.plot(x, (x-x[i0])/u[i0])
i0 = 80
plt.plot(x, (x-x[i0])/u[i0])
i0 = 100
plt.plot(x, (x-x[i0])/u[i0])
i0 = 120
plt.plot(x, (x-x[i0])/u[i0])
i0 = 140
plt.plot(x, (x-x[i0])/u[i0])
plt.ylim(0, 10)
plt.xlim(0, 10)
plt.xlabel("X")
plt.ylabel("t")
plt.show()


# keep using shift+Enter to evolve this shock wave.
plt.figure(figsize=(11, 7), dpi=100)
#plt.plot(x,u, marker='o', lw=2, label='nt = 0')

nt = 300
print("nt =  ", nt)
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

    u[0] = 0
    u[-1] = 0
    if (n % 10) == 0:
        plt.plot(x, u, marker='o', lw=2, label='t = %5.2f' % (n*dt))
# 't = %6f'%t+'    i = %6f'%i)\n
plt.xlim([0, 10])
#plt.ylim([-1, 1])
plt.xlabel("X")
plt.ylabel("u")
plt.legend()
