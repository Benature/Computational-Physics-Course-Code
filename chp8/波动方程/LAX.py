# Lax算法，解波动方程
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math
# %matplotlib notebook

# fixed parameters
c = 300.0  # speed of propagation, m/s
L = 1.0  # length of wire, m
x0 = 0.5  # initial pulse location, m
s = 0.02  # initial pulse width, m

# input parameters
alpha = 0.50  # 0.5 # Courant库兰特数
dx = L*0.005
dt = dx/c*alpha  # Courant condition
tmax = L/c*1.2

# construct initial data
N = int(L/dx)
x = [0.0]*(N+1)
N2 = int(tmax/dt)

u0 = [0.0]*(N+1)
v0 = [0.0]*(N+1)
u1 = [0.0]*(N+1)
v1 = [0.0]*(N+1)

for j in range(N+1):
    x[j] = j*dx
    u0[j] = math.exp(-0.5*((x[j]-x0)/s)**2)

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
        # derivatives at interior points
        for j in range(1, N):
            #v1[j] = v0[j]+0.5*dt*c*(u0[j+1]-u0[j-1])/dx
            #u1[j] = u0[j]+0.5*dt*c*(v0[j+1]-v0[j-1])/dx
            v1[j] = 0.5*(v0[j-1]+v0[j+1])+0.5*dt*c*(u0[j+1]-u0[j-1])/dx
            u1[j] = 0.5*(u0[j-1]+u0[j+1])+0.5*dt*c*(v0[j+1]-v0[j-1])/dx
        # boundary conditions
        u1[0] = u1[N] = 0.0
        v1[0] = v1[1]+u1[1]
        v1[N] = v1[N-1]-u1[N-1]

        # swap old and new lists
        (u0, u1) = (u1, u0)
        (v0, v1) = (v1, v0)
        t += dt
        line.set_data(x, v0)
    return line,


# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
#                              repeat=False, init_func=init)
pam_ani = animation.FuncAnimation(fig, update, frames=range(N2),
                                  interval=1, repeat=False)
#pam_ani.save('wave_LAX_dissipation.gif', writer='pillow',fps=30)
plt.show()
# freeze final plot
