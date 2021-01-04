# 使用雅克比迭代法求上面的方程组的解
import numpy as np
A = np.array([[10,   3,  1],
              [2, -10,  3],
              [1,   3, 10]])
B = np.array([14, -5, 14])

eps = 1e-2  # 想要的迭代精度
N = len(B)
n_iter = 0
xs1 = np.zeros(N)  # 猜测解
xs2 = xs1 + 2*eps

while np.max(abs(xs2-xs1)) > eps:
    xs1 = xs2.copy()
    n_iter += 1
    for i in range(N):
        xs2[i] = B[i]
        for j in range(N):
            if (j != i):
                xs2[i] -= A[i, j]*xs1[j]
        xs2[i] = xs2[i]/A[i, i]

print('solution = ', xs2)
print('iteration number = ', n_iter)
print(np.dot(A, xs2)-B)
