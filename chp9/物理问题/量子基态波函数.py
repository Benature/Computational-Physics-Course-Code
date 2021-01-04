# 变分法求量子基态能量
import math
import random
import numpy as np
import matplotlib.pyplot as plt

# parameters for harmonic oscillator
hbar = 1.0
m = 1.0
k = 1.0
omega0 = (k/m)**0.5

# input number of grid points, steps, random seed
N = 15  # input('number of grid points -> ')
nstep = 300  # input('number of steps -> ')
seed = 12  # input('random number seed -> ')
random.seed(seed)

# setup grid and initial guess
xmin = -5.0
xmax = 5.0
dx = (xmax-xmin)/(N-1)
x = np.arange(xmin, xmax+0.1*dx, dx)
psi = np.ones(N)  # initial guess
psi[0] = psi[N-1] = 0.0  # endpoints fixed at zero

# compute energy, potential, normalization
V = np.zeros(N)
E = np.zeros(nstep+1)
ssq = 0
for i in range(1, N-1):
    V[i] = k*x[i]**2/2.0
    H = -hbar**2*(psi[i-1]-2.0*psi[i]+psi[i+1])/(2*m*dx**2)
    H += V[i]*psi[i]
    E[0] += psi[i]*H*dx
    ssq += psi[i]**2*dx
E[0] /= ssq
psi /= ssq**0.5  # 归一化

# 画图，画出精确解作对比
xfine = np.arange(xmin, xmax, 0.01)
psi0 = [(m*omega0/(math.pi*hbar))**0.25*math.exp(-0.5*m*omega0*xx**2/hbar)
        for xx in xfine]
plt.plot(xfine, psi0)
(line, ) = plt.plot(x, psi, 'o-')
plt.ylabel('$\psi$')
plt.xlabel('x')

# perform the evolution
n = 1
while n <= nstep:
    # choose a random point and a random amount to change psi
    tmp = np.copy(psi)  # temporary wavefunction trial
    j = random.choice(range(1, N-1))
    tmp[j] *= random.uniform(0.8, 1.2)

    # normalize and compute energy
    E[n] = 0.0
    ssq = 0.0
    for i in range(1, N-1):
        H = -hbar**2*(tmp[i-1]-2.0*tmp[i]+tmp[i+1])/(2*m*dx**2)
        H += V[i]*tmp[i]
        E[n] += tmp[i]*H*dx
        ssq += tmp[i]**2*dx
    E[n] /= ssq

    # test if the trial wavefunction reduces energy
    if E[n] < E[n-1]:
        # update current wavefunction
        psi = tmp/ssq**0.5  # 归一化
        # increment step count
        n += 1

# 更新最后计算出来的波函数
line.set_ydata(psi)
plt.title('%d moves' % n)
plt.draw()

# freeze animation and plot energy as a function of time
plt.figure()
plt.plot(range(nstep+1), E)
plt.ylabel('$E / \hbar\omega_0$')
plt.xlabel('step number')
plt.grid()
plt.show()
