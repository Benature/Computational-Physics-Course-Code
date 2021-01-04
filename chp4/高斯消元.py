import numpy as np
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]
              ], float)
B = np.array([-4, 3, 9, 7], float)

N = len(B)

for m in range(N):
    div = A[m, m]  # 对角元
    B[m] /= div
    A[m, :] /= div

    for i in range(m+1, N):
        mult = A[i, m]
        B[i] -= mult * B[m]
        A[i, :] -= mult * A[m, :]

x = np.empty(N)  # N*N 空矩阵
for m in range(N-1, -1, -1):
    x[m] = B[m]
    for i in range(m+1, N):
        x[m] -= A[m, i] * x[i]

print(x)
print(A)
