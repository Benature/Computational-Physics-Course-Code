import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# fixed parameters
T0 = 0.0     # initial temperature, C
D = 1.0      # thermal diffusivity, m^2/s
L = 100.0    # width of the bottom of the stainless container, m
sigma = 1.0  # in m

# input parameters
dx = L*0.001            # 空间步长
dt = dx**2 / D * 10.00  # 时间步长
tmax = L**2 / D * 1.0   # 总的系演化时向

# coefficient of the tridiagonal matrix
alpha = gamma = -D * dt / dx**2
beta = 1.0 + 2.0 * D * dt / dx**2

# construct initial data
N = int(L/dx)
N2 = int(tmax/dt)
x = [0.0] * (N+1)
v = [0.0] * (N+1)
u = [T0] * (N+1)

for j in range(N+1):
    x[j] = j*dx - 0.5*L
    u[j] = 1.0/np.sqrt(2.0*np.pi * sigma**2) * np.exp(-0.5 * (x[j]/sigma)**2)

# preform the evolution
plt.figure()
plt.plot(x, u)
plt.xlabel('x (cm)')
plt.ylabel('u (x, T) (Celcius Degree)')
plt.show()

# prepare animated plot
fig, ax = plt.subplots()
line, = ax.plot(x, u, '-k', animated=False)
ax.grid()

plt.xlabel('x (cm)')
plt.ylabel('u (x, T) (Celcius Degree)')

# preform the evolution
t = 0.0
i = 0.0


def update(frame):
    global v, u, t, i
    if t < tmax:
        # swap u and v
        u, v = v, u
        # boundary conditions
        u[0] = T0
        u[N] = T0

        # set the j=1 and j=N-1 points of v
        v[1] -= v[1]/beta
        v[N-1] -= gamma * u[N]

        # forward sweep
        u[1] = v[1]/beta
        v[1] = gamma/beta

        for j in range(2, N):
            den = beta - alpha * v[j-1]
            u[j] = (v[j] - alpha * u[j-1]) / den
            v[j] = gamma / den

        # backward sweep
        for j in reversed(range(1, N-1)):
            u[j] -= u[j+1] * v[j]

        t += dt
        i += 1
        plt.title('t = %6f' % t + '  i=%6f' % i)
        line.set_data(x, u)
    return line,


pam_ani = animation.FuncAnimation(fig, update, frames=range(500),
                                  interval=50, repeat=False, blit=True)
# pam_ani.save('gauss_implicit_quick.gif', writer='pillow', fps=30)
plt.show()
