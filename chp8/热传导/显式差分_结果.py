# heat conduction research， FTCS scheme
import matplotlib.pyplot as plt
import math
# %matplotlib notebook

# fixed parameters
T0 = 25.0  # temperature gradient, C
D = 1e-4  # thermal diffusivity, m^2/s
L = 1.0  # length of rod, m

# input parameters
dx = L*0.01  # 空间步长
dt = dx**2/D*0.5  # 时间步长
tmax = L**2/D*0.25  # 总的系统演化时间

# construct initial data
N = int(L/dx)
x = [0.0]*(N+1)
u0 = [0.0]*(N+1)
u1 = [0.0]*(N+1)
for j in range(N+1):
    x[j] = j*dx

# prepare animated plot
i = 0
# preform the evolution
t = 0.0
while t < tmax:
    # derivatives at interior points
    for j in range(1, N):
        u1[j] = u0[j]+dt*D*(u0[j+1]-2.0*u0[j]+u0[j-1])/dx**2

    # boundary conditions
    u1[0] = T0
    u1[N] = 0.0

    # swap old and new lists
    (u0, u1) = (u1, u0)
    t += dt
    i += 1

plt.figure()
plt.plot(x, u1, '-k')
plt.ylim(0, T0)
plt.xlabel('x (m)')
plt.ylabel('Temperature (Celcius)')
plt.title('t = %6f' % t+'    i = %6f' % i)
plt.show()
# freeze final plot
