# 蛙跳法的算法实现:
# 蛙跳法解波动方程，无动画
import pylab
import math
import matplotlib.pyplot as plt
%matplotlib notebook

# fixed parameters
c = 300.0  # speed of propagation, m/s
L = 1.0  # length of wire, m
x0 = 0.3  # initial pulse location, m
s = 0.02  # initial pulse width, m

# input parameters
dx = L*0.001
dt = dx/c*0.5
tmax = L/c*1.2

# construct initial data
N = int(L/dx)
x = [0.0]*(N+1)
u0 = [0.0]*(N+1)
v0 = [0.0]*N
u1 = [0.0]*(N+1)
v1 = [0.0]*N
for j in range(N+1):
    x[j] = j*dx
    u0[j] = math.exp(-0.5*((x[j]-x0)/s)**2)

# preform the evolution
t = 0.0
while t < tmax:
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

# freeze final plot
plt.figure()
plt.plot(x, u0, '-k')
plt.grid()
plt.ylim(-1.2, 1.2)
plt.xlabel('x (m)')
plt.ylabel('u')
plt.show()
