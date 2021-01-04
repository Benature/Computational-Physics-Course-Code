# 二阶差分格式解法:
# 尝试周期性边界条件？
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math
import numpy as np
# %matplotlib notebook

# fixed parameters
c = 300.0  # speed of propagation, m/s
L = 1.0  # length of wire, m
x0 = 0.5  # initial pulse location, m
s = 0.03  # initial pulse width, m

# input parameters
alpha = 1.0  # 库兰特数
dx = L*0.002
dt = dx/c*alpha
tmax = L/c*1.2

# construct initial data
N = int(L/dx)
N2 = int(tmax/dt)
x = [0.0]*(N+1)
u0 = [0.0]*(N+1)
u1 = [0.0]*(N+1)
u2 = [0.0]*(N+1)
utmp = [0.0]*(N+1)

for j in range(N+1):
    x[j] = j*dx
    u0[j] = math.exp(-0.5*((x[j]-x0)/s)**2)  # 0.0
    u1[j] = math.exp(-0.5*((x[j]-x0)/s)**2)  # 0.0
# for j in range(1,N):
#    u0[j] = u1[j]+1/2*alpha**2.0*(u1[j+1]+u1[j-1]-2*u1[j])

# for j in range(1, N):
#    u1[j] = u0[j]+dt**2*c**2*(u0[j+1]+u0[j-1]-2*u0[j])/2.0/dx**2

# preform the evolution

plt.figure()
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
i = 0.0


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
                                  interval=1, repeat=False, blit=False)
#pam_ani.save('heat_ftcs.gif', writer='pillow',fps=100)
plt.show()
