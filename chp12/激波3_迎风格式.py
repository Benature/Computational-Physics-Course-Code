# 参考答案
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
# 求解Burgers方程, 初始条件为x=[-1,1]之间的正弦函数,迎风格式，保证稳定。
################SYSU#####
########################
##########initial#########
nx = 201
nt = 30
dx = 2 * np.pi / (nx - 1)
nu = 0.0  # .07
#dt = dx * nu
dt = dx*0.5

x = np.linspace(0, 2 * np.pi, nx)
un = np.empty(nx)
t = 0

# initial condition
u = np.array([np.sin(x0) for x0 in x])

# keep using shift+Enter to evolve this shock wave.
nt = int(np.pi/2/dt)  # 200
plt.figure(figsize=(11, 7), dpi=100)
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        if x[i] < np.pi:
            u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])  # 后差分
        if x[i] >= np.pi:
            u[i] = un[i] - un[i] * dt / dx * (un[i+1] - un[i])  # 前差分
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 * \
        (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]
    if (n % 20) == 0:
        plt.plot(x, u, marker='o', lw=2, label='t = %5.2f' % (n*dt))

plt.xlim([0, 2 * np.pi])
plt.ylim([-1, 1])
plt.legend()
plt.xlabel("X")
plt.ylabel("u")
plt.show()
