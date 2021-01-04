# 参考答案，运行下就知道是哪个练习的答案了。
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
# 求解Burgers方程, 初始条件为一个阶梯状的激波，迎风格式
################SYSU#####
########################
##########initial#########
nx = 401
L = 10
dx = L / (nx - 1)
nu = 0.0  # .07
#dt = dx * nu
dt = dx*0.25
v_l = 0.8
v_r = 0.1

x = np.linspace(0, L, nx)
un = np.empty(nx)
t = 0

# initial condition
u = np.zeros(nx)
u[0:int(nx/2)] = v_l  # 2
u[int(nx/2):nx] = v_r  # 1

# plot initial condition
plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x, u, marker='o', lw=2, label='Initial Condition')
plt.xlim([0, L])
plt.xlabel("X")
plt.ylabel("u")
#plt.ylim([-1, 1])
plt.legend()


# plot characteristics
plt.figure(figsize=(8, 6), dpi=100)
i0 = 0
plt.plot(x, (x-x[i0])/u[i0])
i0 = 40
plt.plot(x, (x-x[i0])/u[i0])
i0 = 80
plt.plot(x, (x-x[i0])/u[i0])
i0 = 120
plt.plot(x, (x-x[i0])/u[i0])
i0 = 160
plt.plot(x, (x-x[i0])/u[i0])

# 间断面
i0 = 200
plt.plot(x, (x-x[i0])/(v_l+v_r)*2, 'ro')

i0 = 240
plt.plot(x, (x-x[i0])/u[i0])
i0 = 280
plt.plot(x, (x-x[i0])/u[i0])
i0 = 320
plt.plot(x, (x-x[i0])/u[i0])
i0 = 360
plt.plot(x, (x-x[i0])/u[i0])
plt.ylim(0, L)
plt.xlim(0, 10)
plt.xlabel("X")
plt.ylabel("t")
plt.show()

plt.figure(figsize=(11, 7), dpi=100)
# keep using shift+Enter to evolve this shock wave.
nt = 600  # int(np.pi/2/dt)  #50
print("nt =  ", nt)
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

    u[0] = v_l
    u[-1] = v_r
    if (n % 50) == 0:
        plt.plot(x, u, marker='o', lw=2, label='t = %5.2f' % (n*dt))

#plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.xlim([0, L])
plt.xlabel("X")
plt.ylabel("u")
#plt.ylim([-1, 1])
plt.legend()
plt.show()
