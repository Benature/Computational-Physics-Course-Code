# 这里是个示例，演示如何使用rk4算法双态量子系统中量子态的演化。
import math
import matplotlib.pyplot as plt
import numpy as np
import cmath

# 4阶龙格库塔积分函数


def rk4(t, x, f, dt):
    dx1 = f(t, x)*dt
    dx2 = f(t+0.5*dt, x+0.5*dx1)*dt
    dx3 = f(t+0.5*dt, x+0.5*dx2)*dt
    dx4 = f(t+dt, x+dx3)*dt
    return x+dx1/6.0+dx2/3.0+dx3/3.0+dx4/6.0


# 速率函数
def Ham(t, X):
    c1 = X[0]
    c2 = X[1]
    # print(c1,c2)
    im1 = complex(E1*c1+A*c2)/complex(0, 1)
    im2 = complex(E2*c2+A*c1)/complex(0, 1)
    return np.array([im1, im2])


# 系统的一些特殊态参数
# 1) E1=E2
E1 = 3.0  # in unit of \hbar
E2 = 3.0  # in unit of \hbar
A = 1.0  # in unit of \hbar

# 2) E1-E2>>V
# E1 = 9.0  # in unit of \hbar
# E2 = 3.0  # in unit of \hbar
# V  = 1.0  # in unit of \hbar

dt = 0.01
tmax = 10.0
nsteps = int(tmax/dt)
c1 = [complex(0, 0)]*nsteps
c2 = [complex(0, 0)]*nsteps

# integrate Lorenz equations of motion using rk4;

X = np.array([complex(1, 0), complex(0, 0)])
for i in range(nsteps):
    c1[i] = X[0]
    c2[i] = X[1]
    # update the vector X to the next time step
    X = rk4(i*dt, X, Ham, dt)

fig = plt.figure()

plt.plot(np.abs(c1)**2.0)  # c1和c2的模的平方，代表了物体分别处于两个态的概率.
plt.plot(np.abs(c2)**2.0)
plt.xlabel('N')
plt.ylabel('C_1 & C_2')
plt.show()
# 画出来的结果可以看到，c1和c2的模的平方的和等于1，代表了你总能在某一个态上找到它。
# 观察一些特殊的例子（解析解差不多存在的情况），
# 当E1=E2的时候，物体会在两个态之间来回震荡。
# 当E1-E2 >> A的时候，V代表的微扰动很难把物体从一个态弄到另一个态.
