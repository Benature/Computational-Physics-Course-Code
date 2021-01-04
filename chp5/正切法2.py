import numpy as np
G = 6.674e-11
M = 5.974e24
m = 7.348e22
R = 3.844e8
omega = 2.662e-6


def f(L):
    return G*M/L**2 - G*m/(R-L)**2 - omega**2*L


L1 = 0.5*R
L1_list = [L1]
n = 60
rate = 0.001

for i in range(n):
    dfdL = (f(L1)-f(L1-rate*R))/(rate*R)
    L1 = L1-f(L1)/dfdL
    L1_list.append(L1)

print(L1_list[-1])
