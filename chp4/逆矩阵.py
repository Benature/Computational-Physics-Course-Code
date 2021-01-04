# 可以尝试用numpy 或者scipy中带的函数解线性方程组
import numpy as np
from numpy.linalg import inv, solve

A = np.array([[2, 1, 1], [3, 4, -1], [1, -4, 5]], float)
B = np.transpose(np.array([[-4, 3, 9]], float))

A_inv = inv(A)

print(A_inv)

X = solve(A, B)
print(X)  # 方程的解 ,可以看到解有问题。
print(np.dot(A_inv, B))  # 逆矩阵乘以常数向量求解
print(np.dot(A, A_inv))  # 如何判断矩阵是奇异矩阵
