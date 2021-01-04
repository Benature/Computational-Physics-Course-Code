# 二维扩散过程的模拟程序
import math
import random
import numpy as np
import matplotlib.pyplot as plt

L = 100  # length of side of box
M = 20  # length of side of square of particles
B = 10  # number of coarse-grainig bins per side
nsteps = 300  # input('number of steps in walk -> ')
steps = range(nsteps)
seed = 10  # input('random number seed -> ')
random.seed(seed)

# initial positions of particles form a M*M block in the middle of the box
xside = range((L-M)//2, (L+M)//2)
yside = range((L-M)//2, (L+M)//2)
x = [i for i in xside for j in yside]  # x-locations of the particles
y = [j for i in xside for j in yside]  # y-locations of the particles
N = len(xside)*len(yside)  # number of particles


# simulate the random walks
for n in steps:
    # update plot
    if n % 20 == 0:
        plt.figure(figsize=(6, 6))
        (points, ) = plt.plot(x, y, 'ro')
        plt.xlim(0, L)
        plt.ylim(0, L)
        plt.xticks(range(0, L+1, L//B))
        plt.yticks(range(0, L+1, L//B))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('step %d' % n)
        plt.grid()
        plt.show()
    # update positions of particles and update counts in bins
    # 移动每一个粒子
    for i in range(N):
        (dx, dy) = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        x[i] += dx
        y[i] += dy
        # make sure that the particles stay in the box
        if x[i] < 0 or x[i] >= 100:
            x[i] -= dx
        if y[i] < 0 or y[i] >= 100:
            y[i] -= dy
