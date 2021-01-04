from numpy.linalg import eigh, eigvalsh
from numpy import array
import scipy.linalg   # SciPy Linear Algebra Library
import numpy as np

L = 5 * 1e-10  # Angstrom

M = 9.1094e-31     # 电子质量
hbar = 1.0546e-34  # 约化普朗克常数
e = 1.6022e-19     # 电荷

a = 10 * e


def intss(m, n):
    if n == m:
        return L**2/4
    elif abs(n-m) % 2 == 0:  # 同奇同偶
        return 0
    else:
        return - (2*L/np.pi)**2 * m * n / (m**2-n**2)**2


def V(x):
    return a * x / L


def Hmn(m, n):
    m = m+1
    n = n+1
    if m == n:
        H_K = L/2 * (hbar**2/(2*M)) * (np.pi*n/L)**2
    else:
        H_K = 0
    H_V = intss(m, n) * a/L

    return (H_K + H_V) * 2/L


N = 10

H = np.empty((N, N))
for i in range(N):
    for j in range(N):
        H[i, j] = Hmn(i, j)

x, V = eigh(H)
# x = eigvalsh(H)
print((x/e)[:10])
