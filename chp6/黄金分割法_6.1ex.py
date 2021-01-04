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


# Initial values of the variables
x1 = sigma/10
x3 = sigma*10
x2 = g1*x1 + g2*x3

f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

# Main loop of the search process
while x3-x1 > accuracy:
    if x2 > 0.5*(x1+x3):
        xp = g1*x1 + g2*x3
        fp = f(xp)
        if fp > f2:
            x1, f1 = xp, fp
        else:
            x3, f3 = x2, f2
            x2, f2 = xp, fp
    else:
        xp = g2*x1 + g1*x3
        fp = f(xp)
        if fp > f2:
            x3, f3 = xp, fp
        else:
            x1, f1 = x2, f2
            x2, f2 = xp, fp

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
