# 程序一
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
# 求解Burgers方程, 初始条件为x=[0,2]之间的正弦函数
# 该程序中有很多遗漏之处，请大家补全。

nx = 61  # 总的空间格点数目 FOCUS!
nt = 10  # 总的计算时间演化步数 FOCUS!
dx = 2 * np.pi / (nx - 1)
nu = 0.0  # 无粘滞条件，粘滞系数等于0
dt = dx*5  # 时间步长和空间步长的关系
# dt = dx * nu   #如果添加粘滞项，需要把时间步长修改为本公式

x = np.linspace(0, 2 * np.pi, nx)
un = np.empty(nx)
t = 0

# initial condition
u = np.array([np.sin(x0) for x0 in x])

plt.figure(figsize=(8, 6), dpi=100)
plt.plot(x, u, marker='o', lw=2, label='Initial Condition')
plt.legend()
plt.xlabel("x")
plt.ylabel("u")
plt.show()

# keep using shift+Enter to evolve this shock wave.

plt.figure(figsize=(11, 7), dpi=100)
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - \
            un[i] * dt / dx * (un[i] - un[i-1]) + \  # 后差分
        nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])  # 二阶差分

    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
        (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]  # 周期边界条件
    if (n % 20) == 0:  # 每过20个时间步，就在图上多画出一条当前的(u,x)线
        plt.plot(x, u, marker='o', lw=2, label='t = %5.2f' % (n*dt))

# plt.xlim([0, ])
# plt.ylim([, ])
plt.xlabel("X")
plt.ylabel("u")
plt.legend()
plt.show()
