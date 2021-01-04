import numpy as np


def gram_schmidt(A):
    Q = np.zeros_like(A)
    cnt = 0
    for a in A.T:
        u = np.copy(a)
        for i in range(0, cnt):
            u -= np.dot(np.dot(Q[:, i].T, a), Q[:, i])  # 减去待求向量在已求向量上的投影
        e = u / np.linalg.norm(u)  # noum
        Q[:, cnt] = e
        cnt += 1
    # 对于正交矩阵，Q^(-1) = Q.T
    R = np.dot(Q.T, A)
    return Q, R


np.set_printoptions(precision=4, suppress=True)
A = np.array([[1, 2], [2, 1]], float)
Q, R = gram_schmidt(A)

print(Q)
print(R)
print(np.matmul(Q, R))
print(np.matmul(Q[:, 0], Q[:, 0]))