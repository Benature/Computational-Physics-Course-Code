from random import random
import numpy as np

ndim = 3  # dimension
N = 10000


def f(x, y, z):
    if sum(np.array([x, y, z])**2) > 1:
        return 0

    if sum(np.array([x-0.5, y])**2) <= 0.5**2:
        return 1
    return 0


tot = 0.0
for i in range(N):
    r = np.random.random((3,))*2-1  # FOCUS! from -1 to 1
    tot += f(*r)

I = 2**ndim * tot/N
print(I)
