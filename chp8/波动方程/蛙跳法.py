#蛙跳法动画, 解波动方程
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math
# %matplotlib notebook

# fixed parameters
c = 300.0  # speed of propagation, m/s
L = 1.0  # length of wire, m
x0 = 0.3  # initial pulse location, m
s = 0.02  # initial pulse width, m

# input parameters
dx = L*0.003
dt = dx/c*0.1
tmax = L/c*1.2

# construct initial data
N = int(L/dx)
x = [0.0]*(N+1)
N2 = int(tmax/dt)
u0 = [0.0]*(N+1)
v0 = [0.0]*N
u1 = [0.0]*(N+1)
v1 = [0.0]*N
for j in range(N+1):
    x[j] = j*dx
    u0[j] = math.exp(-0.5*((x[j]-x0)/s)**2)

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
plt.ylabel('u')

# preform the evolution
global t
t = 0.0


def update(frame):
    global v0
    global u0
    global v1
    global u1
    global t
    if t < tmax:
        # update plot
        # derivatives at interior points
        for j in range(N):
            v1[j] = v0[j]+dt*c*(u0[j+1]-u0[j])/dx
        for j in range(1, N):
            u1[j] = u0[j]+dt*c*(v1[j]-v1[j-1])/dx

    # boundary conditions for u
        u1[0] = u1[N] = 0.0

    # swap old and new lists
        (u0, u1) = (u1, u0)
        (v0, v1) = (v1, v0)
        t += dt
        line.set_data(x, u0)
    return line,


# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
#                              repeat=False, init_func=init)
print()
pam_ani = animation.FuncAnimation(fig, update, frames=range(N2),
                                  interval=3, repeat=False, blit=False)
#pam_ani.save('wave_frogleap.gif', writer='pillow',fps=30)
plt.show()
