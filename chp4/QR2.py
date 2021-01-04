from QR1 import gram_schmidt
import numpy as np

eps = 1e-6

A = np.array([[1, 4, 8, 4], [4, 2, 3, 7], [8, 3, 6, 9], [4, 7, 9, 2]], float)

A0 = np.copy(A)
N = len(A[0, :])
I = np.identity(N)
X = np.identity(N)
di = np.diag_indices(N, ndim=2)  # 标注了整个矩阵的对角元素的 index

for k in range(1000):
    Q, R = gram_schmidt(A)
    X = np.matmul(X, Q)
    A = np.matmul(R, Q)

    B = np.copy(A)
    B[di] = 0
    if np.amax(abs(B)) < eps:
        break

if k == 999:
    print("too many steps")
else:
    print('eigenvalues')
    print(A[di])
    print('eigenvectors')
    print(X)

print("test the first eigenvalue", np.matmul(A0, X[:, 0]) - A[0, 0]*X[:, 0])
