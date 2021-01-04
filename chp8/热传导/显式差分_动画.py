#FTCS, 热传导动画
# %matplotlib notebook
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# fixed parameters
T0 = 25.0  # temperature gradient, C
D = 1e-4  # thermal diffusivity, m^2/s
L = 1.0  # length of rod, m

# input parameters
alpha = 1.01  # 类似库兰特数
dx = L*0.01  # 空间步长
dt = dx**2/D*0.5*alpha  # 时间步长
tmax = L**2/D*0.3  # 总的系统演化时间

# construct initial data
N = int(L/dx)
N2 = int(tmax/dt)
x = [0.0]*(N+1)
u0 = [0.0]*(N+1)
u1 = [0.0]*(N+1)
for j in range(N+1):
    x[j] = j*dx

# preform the evolution

plt.figure()
plt.plot(x, u0)
plt.ylim(-5, T0)
plt.xlabel('x (m)')
plt.ylabel('u')
plt.show()

# prepare animated plot
fig, ax = plt.subplots()
line, = ax.plot(x, u0, '-k', animated=False)
ax.grid()

plt.ylim(-5, 25)
plt.xlabel('x (m)')
plt.ylabel('u (t, x) (Celcius)')

# preform the evolution
t = 0.0
i = 0.0


def update(frame):
    global u0
    global u1
    global t
    global i
    if t < tmax:
        for j in range(1, N):
            u1[j] = u0[j]+dt*D*(u0[j+1]-2.0*u0[j]+u0[j-1])/dx**2

        # boundary conditions
        u1[0] = T0
        u1[N] = 0.0
        # swap old and new lists
        (u0, u1) = (u1, u0)

        t += dt
        i += 1
        plt.title('t = %6f' % t+'    i = %6f' % i)
        line.set_data(x, u0)
    return line,


pam_ani = animation.FuncAnimation(fig, update, frames=range(N2),
                                  interval=1, repeat=False, blit=True)
#pam_ani.save('heat_ftcs.gif', writer='pillow',fps=100)
plt.show()
