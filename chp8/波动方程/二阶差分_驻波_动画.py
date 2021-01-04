# 二阶差分格式解法:
# 尝试周期性边界条件？

import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math
# %matplotlib notebook

# fixed parameters
c = 1.0  # speed of propagation, m/s
L = 1.0  # length of wire, m

# input parameters
dx = 0.02
dt = 0.02
alpha = c*dt/dx  # 库兰特数
tmax = L/c*1.0

# construct initial data
N = 50
N2 = int(tmax/dt)
x = np.zeros(N+1)
u0 = np.zeros(N+1)
u1 = np.zeros(N+1)
u2 = np.zeros(N+1)

for i in range(N+1):
    x[i] = i*dx
    u0[i] = np.sin(i*dx*np.pi)  # 0.0
    u1[i] = np.sin(i*dx*np.pi)  # 0.0

# preform the evolution
plt.figure()
# plt.plot(x, u[0, :])
plt.plot(x, u0)
plt.ylim(-1.2, 1.2)
plt.xlabel('x (m)')
plt.ylabel('u')
plt.show()

# prepare animated plot
fig, ax = plt.subplots()
line, = ax.plot(x, u0, '-k', animated=False)
ax.grid()

plt.ylim(-1.2, 1.2)
plt.xlabel('x (m)')
plt.ylabel('u (t, x)')

# preform the evolution
t = 0.0
i = 0


def update(frame):
    global u0
    global u1
    global u2
    global t
    global i
    if t < tmax:
        for j in range(1, N):  # skip the bound,
            u2[j] = 2*u1[j] - u0[j]+alpha**2.0*(u1[j+1]-2.0*u1[j]+u1[j-1])

        u2[0] = 0
        u2[N] = 0
        # swap old and new lists
        u0 = u1
        u1 = np.copy(u2)  # 这里要注意用np.copy，否则u2改变，则u1改变,所有引用u1[j-1]都会出问题.

        t += dt
        i += 1
        plt.title('t = %6f' % t+'    i = %6f' % i)
        line.set_data(x, u2)
    return line,


pam_ani = animation.FuncAnimation(fig, update, frames=range(N2),
                                  interval=100, repeat=False, blit=False)
#pam_ani.save('heat_ftcs.gif', writer='pillow',fps=100)
plt.show()
