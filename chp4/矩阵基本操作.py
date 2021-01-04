import numpy as np

# 行向量
v = np.array([[1, 2, 3]])
print(v)
# 列向量
v = np.transpose(np.array([[1, 2, 3]]))
print(v)
# 矩阵的乘法，用 np.dot(), 比如 w = np.dot(A,v)

# 单位矩阵
I = np.identity(5)
print(I)
I.diagonal()  # 取对角元素

print(np.zeros([3, 3]))  # 0矩阵
print(np.empty([3, 3]))  # 空矩阵
