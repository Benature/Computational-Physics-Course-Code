import numpy
from matplotlib import pyplot as plt
import time
import sys

# %matplotlib inline

nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2 / (nx-1)
nt = 25  # nt is the number of timesteps we want to calculate
dt = .025  # dt is the amount of time each timestep covers (delta t)
c = 1  # assume wavespeed of c = 1

u = numpy.ones(nx)  # numpy function ones()
# setting u = 2 between 0.5 and 1 as per our I.C.s
u[int(.5 / dx):int(1 / dx + 1)] = 2
print(u)
# 画图
plt.plot(numpy.linspace(0, 2, nx), u)

un = numpy.ones(nx)  # initialize a temporary array

for n in range(nt):  # loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()  # copy the existing values of u into un
    for i in range(1, nx):  # you can try commenting this line and...
        # for i in range(nx): ## ... uncommenting this line and see what happens!
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

plt.plot(numpy.linspace(0, 2, nx), u)


def linearconv(nx, nt):
    dx = 2 / (nx - 1)
    # nx 是空间格点数目，nt is the number of timesteps we want to calculate
    c = 1
    sigma = .5

    dt = sigma * dx

    u = numpy.ones(nx)
    u[int(.5/dx):int(1 / dx + 1)] = 2

    un = numpy.ones(nx)

    for n in range(nt):  # iterate through time
        un = u.copy()  # copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

    plt.plot(numpy.linspace(0, 2, nx), u)


# Bo, 比较不同的空间格点数目计算的细节比较,可以看出，个点越多，hat函数的细节处越清晰。
linearconv(801, 400)
linearconv(51, 25)

plt.show()
