# Ising模型 ， 示例程序
import random
import pylab
import numpy as np
import math
import matplotlib.pyplot as plt
%matplotlib inline

J = 1.0  # exchange energy
L = 30  # number of atoms per side of lattice
nsweep = 1000  # number sweeps to average
seed = 12  # random number seed
random.seed(seed)

N = L**2  # grid size
kT = np.arange(0.1, 2.8, 0.1)  # 温度分布
# kT = np.arange(0.1, 50.0, 10) #温度分布

e = np.zeros(len(kT))  # 单位能量
m = np.zeros(len(kT))  # 单位磁性

# initial data
s = np.ones((L, L))
E = 0.0  # 存储能量
M = 0.0  # 存储总磁性
for i in range(L):
    for j in range(L):
        E -= J*s[i, j]*(s[(i+1) % L, j]+s[i, (j+1) % L])
        M += s[i, j]

# initial state
image = plt.imshow(s, vmax=1, vmin=-1)
plt.show()

# slowly warm up
for t in range(len(kT)):
    for sweep in range(nsweep):
        # sweep over all particles in lattice
        for i in range(L):
            for j in range(L):
                # compute energy required to flip spin
                dE = s[(i+1) % L, j]+s[(i-1) % L, j] + \
                    s[i, (j+1) % L]+s[i, (j-1) % L]
                dE *= 2.0*J*s[i, j]

                # Metropolis algorithm to see if we should accept trial
                if dE <= 0.0 or random.random() <= math.exp(-dE/kT[t]):
                    # accept trial: reverse spin; return dE and dM
                    s[i, j] *= -1
                    M += 2.0*s[i, j]  # 总磁性的变化
                    E += dE  # 总能量变化
       # 更新总能量和总磁性
        e[t] += E
        m[t] += M
    # average nsweep sweeps
    e[t] /= nsweep
    m[t] /= nsweep
    e[t] /= N
    m[t] /= N
    if t % 1 == 0:
        plt.imshow(s, vmax=1, vmin=-1)
        plt.title('kT = %g' % kT[t])
        plt.text(L*1.03,  L/2, ' M = %g' % m[t], color='r')
        plt.show()

# produce plots
plt.figure(figsize=(10, 8))
plt.plot(kT, e, 'o')
plt.xlabel('temperature')
plt.ylabel('energy per atom')
plt.grid()
plt.figure(figsize=(10, 8))
plt.plot(kT, m, 'o')
plt.xlabel('temperature')
plt.ylabel('magnetization per atom')
plt.grid()
plt.show()
