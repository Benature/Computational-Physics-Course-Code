# 处理模糊图像
from math import exp
from numpy.fft import rfft2, irfft2
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

# 5,10,15,20,25.0,30,35， 高斯型PSF的方差值， 可以尝试不同的值
sigma = 25  # FOCUS!

# Read the data array
x = np.loadtxt("../../data/11/blur.txt", float)
rows = x.shape[0]
cols = x.shape[1]

# Make a density plot，展示模糊图像
plt.figure(figsize=(8, 8))
plt.imshow(x)
plt.show()

# Compute the point spread function
f = np.empty([rows, cols], float)
for j in range(cols):
    jp = j
    if jp > cols/2:
        jp -= cols
    for i in range(rows):
        ip = i
        if ip > rows/2:
            ip -= rows
        f[i, j] = exp(-(ip*ip+jp*jp)/(2*sigma*sigma))

# Fourier transform the picture and the point spread function
xfft = rfft2(x)
ffft = rfft2(f)

# Divide one by the other
yfft = np.empty([rows, cols//2+1], complex)
for j in range(cols//2+1):
    for i in range(rows):
        if ffft[i, j] <= 1.0e-6:
            yfft[i, j] = xfft[i, j]
        else:
            yfft[i, j] = xfft[i, j]/ffft[i, j]

# Invert the transform， 傅里叶逆变换
y = irfft2(yfft)

# Make a density plot，查看复原图像
plt.figure(figsize=(8, 8))
plt.imshow(y)
plt.show()
