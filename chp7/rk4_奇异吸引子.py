# 上一小章中的练习题，洛伦兹方程积分，吸引子，用RK4算法
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 4阶龙格库塔积分函数


def rk4(t, x, f, dt):
    dx1 = f(t, x)*dt
    dx2 = f(t+0.5*dt, x+0.5*dx1)*dt
    dx3 = f(t+0.5*dt, x+0.5*dx2)*dt
    dx4 = f(t+dt, x+dx3)*dt
    return x+dx1/6.0+dx2/3.0+dx3/3.0+dx4/6.0


# 注意在这个函数里，使用了p,r,b这些全局的变量。
def lorenz(t, X):
    x, y, z = X
    return np.array([p*(y - x), x * (r - z) - y, x * y - b * z])


p = 10.0
r = 28.0
b = 8.0/3.0
x0 = 0.0
y0 = 1.0
z0 = 0.0

dt = 0.01
tmax = 100.0
nsteps = int(tmax/dt)
x1 = [0.0]*nsteps
y1 = [0.0]*nsteps
z1 = [0.0]*nsteps

# integrate Lorenz equations of motion using rk4;

X = np.array([x0, y0, z0])
for i in range(nsteps):
    x1[i] = X[0]
    y1[i] = X[1]
    z1[i] = X[2]
    # update the vector X to the next time step
    X = rk4(i*dt, X, lorenz, dt)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x1, y1, z1)

# 计算初值稍微变化后的运动轨迹
x0 = 0.0
y0 = 1.01
z0 = 0.0
x2 = [0.0]*nsteps
y2 = [0.0]*nsteps
z2 = [0.0]*nsteps

X = np.array([x0, y0, z0])
for i in range(nsteps):
    x2[i] = X[0]
    y2[i] = X[1]
    z2[i] = X[2]
    # update the vector X to the next time step
    X = rk4(i*dt, X, lorenz, dt)
#ax.plot(x2, y2, z2)
plt.show()
plt.plot(x1, z1)
plt.plot(x2, z2, 'r')
plt.xlabel('x')
plt.ylabel('z')
plt.show()
