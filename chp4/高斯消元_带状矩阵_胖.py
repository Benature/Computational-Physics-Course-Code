# 请做上面的练习
from numpy import zeros, empty
import numpy as np
from pylab import plot, show
from numpy.linalg import inv, solve

# Constants
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k - m*omega**2
print(alpha)

w = 2  # width of ribbon

# Set up the initial values of the arrays
A = zeros([N, N], float)
for i in range(N-1):
    A[i, i] = alpha
    A[i, i+1:i+w+1] = -k
    A[i+1:i+w+1, i] = -k
A[0, 0] = alpha - k
A[N-1, N-1] = alpha

v = zeros(N, float)
v[0] = C

A0 = np.copy(A)
v0 = np.copy(v)

# Perform the Gaussian elimination
for i in range(N-2):
    # A Divide row i by its diagonal element
    v[i] /= A[i, i]
    A[i, i+1] /= A[i, i]  # 非主元（们）
    A[i, i+2] /= A[i, i]  # 非主元（们）

    # A[i, i+1:i+w+1] /= A[i, i]  # 非主元（们）
    # A[i, :] /= A[i, i]

    # Now subtract it from the next row down
    # for j in range(w):
    #     if i+1+j >= N:
    #         break
    #     v[i+1+j] -= A[i+1, i] * v[i]
    #     A[i+1+j, i+1:i+w+1] -= A[i+1, i] * A[i, i+1]  # 非主元（们）
    # for J in range(i+1, N):
    #     mult = A[J, i]
    #     v[J] -= mult * v[i]
    #     A[J, :] -= mult * A[i, :]
    v[i+1] -= A[i+1, i] * v[i]
    A[i+1, i+1] -= A[i+1, i] * A[i, i+1]  # 非主元（们）
    A[i+1, i+2] -= A[i+1, i] * A[i, i+1]  # 非主元（们）

v[N-2] /= A[N-2, N-2]
v[N-1] -= A[N-1, N-2] * v[N-2]
A[N-1, N-1] -= A[N-1, N-2] * A[N-2, N-1]
# Divide the last element of v by the last diagonal element
v[N-1] /= A[N-1, N-1]

# Backsubstitution
x = empty(N, float)
x[N-1] = v[N-1]
for i in range(N-2, -1, -1):
    x[i] = v[i] - A[i, i+1] * x[i+1]

# plot
plot(x)
# show()

print(x)

X = solve(A0, v0)
print(X)
plot(X)
