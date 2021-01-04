# 不做动画，只做数值计算
import matplotlib.pyplot as plt
import math
# %matplotlib notebook

# fixed parameters
c = 300.0  # speed of propagation, m/s
L = 1.0  # length of wire, m
x0 = 0.5  # initial pulse location, m
s = 0.02  # initial pulse width, m

# input parameters

dx = L*0.001
dt = dx/c*1.1  # 这里可以改变库兰特数.
tmax = L/c*0.8

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


# preform the evolution
global t
t = 0.0
while t < tmax:
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

plt.figure()
plt.plot(x, u0)
plt.ylim(-1.2, 1.2)
plt.xlabel('x (m)')
plt.ylabel('u')
plt.show()
