import numpy as np
# 使用高斯-赛德尔方法求解上面的线性方程组，可以发现比雅克比方法收敛到快。
A = np.array([[10,   3,  1],
              [2, -10,  3],
              [1,   3, 10]])
B = np.array([14, -5, 14])

eps = 1e-4  # 想要的迭代精度
N = len(B)
n_iter = 0
xs1 = np.zeros(N)
xs2 = xs1 + 2*eps

while np.max(abs(xs2-xs1)) > eps:
    xs1 = xs2.copy()
    n_iter += 1
    for i in range(N):
        tmp = B[i]
        for j in range(N):
            if (j != i):
                tmp = tmp-A[i, j]*xs2[j]
        xs2[i] = tmp/A[i, i]

print('solution = ', xs2)
print('iteration number = ', n_iter)
print(np.dot(A, xs2)-B)
