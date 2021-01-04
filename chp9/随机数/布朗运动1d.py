# 参考答案
# random walk,随机行走
import matplotlib.pyplot as plt
import random as rd
# %matplotlib inline

nsteps = 100  # input('number of steps in walk -> ')
nwalks = 100  # input('number of random walks -> ') 粒子数
seed = 10  # input('random number seed -> ')
rd.seed(seed)
steps = range(nsteps)
xrms = [0.0] * nsteps  # mean squared distance

# loop over the number of walks being done
for i in range(nwalks):
    x = [0] * nsteps  # position at each step in walk
    # loop over steps in this walk
    for n in steps[1:]:
        if rd.random() < 0.5:
            x[n] = x[n-1] - 1
        else:
            x[n] = x[n-1] + 1
        xrms[n] += (x[n]**2 - xrms[n]) / (i+1)
    plt.plot(steps, x, 'o-')

for n in steps:
    xrms[n] = xrms[n]**0.5

plt.title('random walk')
plt.xlabel('step number')
plt.ylabel('x')
plt.grid()

plt.figure()
plt.title('root-mean-squared distance for %d walks' % nwalks)
plt.plot(steps, xrms, '.')
plt.plot(steps, [n**0.5 for n in steps], '-')
plt.xlabel('step number')
plt.ylabel('root-mean-squared distance')
plt.grid()

plt.show()
