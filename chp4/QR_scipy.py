# 亦可尝试scipy中的QR分解法
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

# From the Wikipedia Article on QR Decomposition
A = scipy.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
Q, R = scipy.linalg.qr(A)

print("A:")
print(A)

print("Q:")
print(Q)

print("R:")
print(R)
