# 供同学们参考的练习, 使用rk4算法，做开普勒轨道积分,计算哈雷彗星轨道
# 使用太阳系的天文单位做计算
import math
import matplotlib.pyplot as plt
import numpy as np
# heliocentric gravitational constant
GM = (2.0*math.pi)**2

# 4阶龙格库塔积分函数


def rk4(t, x, f, dt):
    '''RK4'''
    dx1 = f(t, x)*dt
    dx2 = f(t+0.5*dt, x+0.5*dx1)*dt
    dx3 = f(t+0.5*dt, x+0.5*dx2)*dt
    dx4 = f(t+dt, x+dx3)*dt
    return x+dx1/6.0+dx2/3.0+dx3/3.0+dx4/6.0

# 轨道参量变化速率函数


def dXdt(t, X):
    x = X[0]
    vx = X[1]
    y = X[2]
    vy = X[3]
    r = math.sqrt(x**2+y**2)
    ax = -GM*x/r**3
    ay = -GM*y/r**3
    return np.array([vx, ax, vy, ay])


# 距离的单位都用天文单位AU(地球和太阳的平均距离)
# 速度用 天文单位/年

# 行星轨道数据
e = 0.96714  # 椭圆偏心率
per = 75.32  # 周期
a = 17.834  # 椭圆长轴

# 初始位置
x0 = a*(1.0-e)
y0 = 0.0

# 初始速度
vx0 = 0.0
vy0 = 2.0*math.pi*a/per*math.sqrt((1.0+e)/(1.0-e))


dt = 0.01  # 时间步长
tmax = 160.0  # 总时长
nsteps = int(tmax/dt)
x = [0.0]*nsteps
y = [0.0]*nsteps

# integrate Newton's equations of motion using rk4;
# X is a vector that contains the positions and
# velocities being integrated
X = np.array([x0, vx0, y0, vy0])
for i in range(nsteps):
    x[i] = X[0]
    y[i] = X[2]
    # update the vector X to the next time step
    X = rk4(i*dt, X, dXdt, dt)
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'o-')
plt.xlabel('x (au)')
plt.ylabel('y (au)')
minmax = 1.1*max(abs(min(x+y)), abs(max(x+y)))
plt.axis([-minmax, minmax, -minmax, minmax], aspect='equal')
plt.grid()
plt.show()
