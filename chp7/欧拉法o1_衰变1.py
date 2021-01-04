import numpy as np
from matplotlib import pyplot as plt

# 输入初始的参数，包括N0，tau，步长dt，和所需的演化计算时间tmax
nuclei0 = 1000
tau = 1.5
dt = 0.1
tmax = 10

# 根据步长和总的演化时间计算总步数
nsteps = int(tmax/dt)
nuclei = [0.0]*nsteps  # 初始化每一步所剩的原子核数目list, 长度为nsteps
t = [0.0]*nsteps  # 初始化每一步的时间list ,长度为nsteps

# use Euler's method to integrate equation for radioactive decay
t[0] = 0.0
nuclei[0] = nuclei0
for i in range(nsteps-1):
    t[i+1] = t[i]+dt
    nuclei[i+1] = nuclei[i]-nuclei[i]/tau*dt

# 下面开始作图
plt.plot(t, nuclei, '.-b')
plt.xlabel('time')
plt.ylabel('nuclei')
plt.title('radioactive decay')
plt.grid()
plt.show()
