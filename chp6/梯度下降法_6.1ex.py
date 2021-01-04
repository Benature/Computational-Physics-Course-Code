# 练习参考答案
from math import exp, sqrt
import numpy as np
import matplotlib.pyplot as plt
# Constants
sigma = 1.0             # Value of sigma in nm

g1 = (sqrt(5)-1)/2
g2 = 1 - g1
accuracy = 1e-6         # Required accuracy in nm

# Function to calculate the Buckingham potential


def f(r):
    return (sigma/r)**6 - exp(-r/sigma)


def f_d(r):
    return -6 * sigma**6/r**7 - exp(-r/sigma) * (-1/sigma)


times = 100
gamma = 0.05
x2 = 1
for i in range(times):
    x2 -= gamma * f_d(x2)


# Print the result
print("The minimum falls at", x2, "nm")

# make a plot
N = 1000
rs = np.linspace(1.0, 8, N)
ys = []
for r in rs:
    ys.append(f(r))
plt.plot(rs, ys, '.')
plt.plot(x2, f(x2), 'ro')
plt.xlabel("r")
plt.ylabel("V")
plt.show()
