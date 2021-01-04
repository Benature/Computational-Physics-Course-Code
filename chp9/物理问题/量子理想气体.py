# quatum ideal gas and classical limit
from math import exp, pi
from random import random, randrange
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

T = 1000  # KB*T
N = 500  # number of particles
steps = 2000000  # how many times we update the status
# Create a 2D array to store the quantum numbers
n = np.ones([N, 3], int)  # quantum number
Es = np.ones(N, int)  # store the total energy for each particle
# Main loop
eplot = []  # 用来存储每一步计算出来的能量演化结果。
E = 3*N*pi*pi/2  # 初始能量
for k in range(steps):
    # Choose the particle and the move
    i = randrange(N)
    j = randrange(3)
    if random() < 0.5:
        dn = 1
        dE = (2*n[i, j]+1)*pi*pi/2
    else:
        dn = -1
        dE = (-2*n[i, j]+1)*pi*pi/2

    # Decide whether to accept the move, using Metropolis算法。
    if n[i, j] > 1 or dn == 1:
        if random() < exp(-dE/T):
            n[i, j] += dn
            E += dE
    eplot.append(E)

eplot = np.array(eplot)
eplot = eplot/N
# Make the graph
plt.figure()
plt.plot(eplot)
plt.ylabel("Energy")
plt.show()

for i in range(N):
    Es[i] = n[i, 0]**2+n[i, 1]**2+n[i, 2]**2
plt.figure()
n, bins, patches = plt.hist(Es, 30, density=0, facecolor='g')
# plt.plot(Es)
plt.show()
