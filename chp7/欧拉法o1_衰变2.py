'''practice 7.1'''
import numpy as np
from matplotlib import pyplot as plt
# 输入初始的参数，包括N0，tau，步长dt，和所需的演化计算时间tmax
N0 = 1000
N0_2 = 1000
tau = 1.5
tau2 = 1.5
dt = 0.1
tmax = 10

# 根据步长和总的演化时间计算总步数
nsteps = int(tmax/dt)
#初始化每一步所剩的原子核数目list, 长度为nsteps
N = [0.0]*nsteps  # N_A
N2 = [0.0]*nsteps  # N_B
t = [0.0]*nsteps  # 初始化每一步的时间list ,长度为nsteps

# use Euler's method to integrate equation for radioactive decay
t[0] = 0.0
N[0] = N0
for i in range(nsteps-1):
    t[i+1] = t[i]+dt  # 时间
    N[i+1] = N[i] + (-N[i]/tau*dt)  # N_A
    N2[i+1] = N[i] - (N2[i]/tau2 + N[i]/tau)*dt  # + or - ???

# 下面开始作图
plt.plot(t, N, '.-b')
plt.xlabel('time')
plt.ylabel('N')
plt.title('radioactive decay')
plt.grid()
plt.show()
