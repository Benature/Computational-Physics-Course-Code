import numpy as np
# 请做上面的练习，可以参考下面的程序。
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]
              ], float)
B = np.array([-4, 3, 9, 7], float)
N = len(B)  # 返回列向量B的长度

# 按列选主元,进行高斯消元
for m in range(N):
    # 👇 多了这部分
    # 首先找到(m,m)元下面的元中绝对值最大的元,假设在k列,然后
    # 把k行和m行交换,进行消元
    idx = np.argmax(abs(A[m: N, m]))
    if idx != 0:
        tmp1 = np.copy(A[m, :])
        tmp2 = np.copy(B[m])
        A[m, :] = np.copy(A[idx+m, :])
        A[idx+m, :] = np.copy(tmp1)
        B[m] = np.copy(B[idx+m])
        B[idx+m] = np.copy(tmp2)
        # print(idx, tmpl, tmp, A, B)# used to debug 把第m行元素都除以对角元,包含A和B
    # 👆 多了这部分

    div = A[m, m]
    A[m, :] /= div
    B[m] /= div

    # 用m行的元把(m,m)对角元下面的列元退一消去,包含矩阵A和向量B
    for i in range(m+1, N):
        mult = A[i, m]
        A[i, :] -= mult*A[m, :]
        B[i] -= mult*B[m]

# print(A)
# print(B)
x = np.empty(N)  # N*N 空矩阵
for m in range(N-1, -1, -1):
    x[m] = B[m]
    for i in range(m+1, N):
        x[m] -= A[m, i] * x[i]
print(x)
