# 隐式算法
# implicit scheme, no animation
import matplotlib.pyplot as plt
import math
# %matplotlib notebook

# fixed parameters
T0 = 25.0  # temperature gradient, C
D = 1e-4  # thermal diffusivity, m^2/s
L = 1.0  # length of rod, m

# input parameters
dx = L*0.01  # 空间步长
dt = dx**2/D*1.00  # 时间步长
tmax = L**2/D*1.0  # 总的系统演化时间

# coefficients of the tridiagonal matrix
alpha = gamma = -D*dt/dx**2
beta = 1.0+2.0*D*dt/dx**2

# construct initial data
N = int(L/dx)
x = [0.0]*(N+1)
v = [0.0]*(N+1)
u = [0.0]*(N+1)
for j in range(N+1):
    x[j] = j*dx
u[0] = T0

plt.figure()
plt.plot(x, u)

# preform the evolution
t = 0.0
while t < tmax:
    # swap u and v
    (u, v) = (v, u)

    # boundary conditions
    u[0] = T0
    u[N] = 0.0

    # set the j=1 and j=N-1 points of v to the correct values
    v[1] -= alpha*u[0]
    v[N-1] -= gamma*u[N]

    # forward sweep
    u[1] = v[1]/beta
    v[1] = gamma/beta
    for j in range(2, N):
        den = beta-alpha*v[j-1]
        u[j] = (v[j]-alpha*u[j-1])/den
        v[j] = gamma/den
    # backward sweep
    for j in reversed(range(1, N-1)):
        u[j] -= u[j+1]*v[j]
    t += dt
    if t == 10.0:
        plt.plot(x, u)
    if t == 30.0:
        plt.plot(x, u)
    if t == 100.0:
        plt.plot(x, u)
    if t == 300.0:
        plt.plot(x, u)
    if t == 1000.0:
        plt.plot(x, u)
    if t == 3000.0:
        plt.plot(x, u)

#plt.plot(x, u)
l_list = ["t=0s", "t=10s", "t=30s", "t=100s", "t=300s", "t=1000s", "t=3000s"]
plt.legend(l_list)
plt.ylabel("u(x, t) (Celcius Degree)")
plt.xlabel("x (m)")
plt.show()
