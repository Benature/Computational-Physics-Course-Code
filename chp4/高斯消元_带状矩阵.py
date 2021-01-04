# 请做上面的练习
from numpy import zeros, empty
from pylab import plot, show

# Constants
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k - m*omega**2
print(alpha)

# Set up the initial values of the arrays
A = zeros([N, N], float)
for i in range(N-1):
    A[i, i] = alpha
    A[i, i+1] = -k
    A[i+1, i] = -k
A[0, 0] = alpha - k
A[N-1, N-1] = alpha

v = zeros(N, float)
v[0] = C

# Perform the Gaussian elimination
for i in range(N-1):
    # A Divide row i by its diagonal element
    v[i] /= A[i, i]
    A[i, i+1] /= A[i, i]  # 非主元（们）
    # A[i, i+1:i+1+1] /= A[i, i]  # 非主元（们）

    # Now subtract it from the next row down
    v[i+1] -= A[i+1, i] * v[i]
    A[i+1, i+1] -= A[i+1, i] * A[i, i+1]  # 非主元（们）
    # A[i+1, i+2] -= A[i+1, i] * A[i, i+1]  # 非主元（们）

# Divide the last element of v by the last diagonal element
v[N-1] /= A[N-1, N-1]

# Backsubstitution
x = empty(N, float)
x[N-1] = v[N-1]
for i in range(N-2, -1, -1):
    x[i] = v[i] - A[i, i+1] * x[i+1]

# plot
plot(x)
show()

print(x)
