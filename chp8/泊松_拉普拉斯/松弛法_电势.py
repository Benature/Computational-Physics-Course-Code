# 松弛法计算电势，
import mpl_toolkits.mplot3d
import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

eps = 1e-5  # fractional error allowed
L = 1.0  # length of each side
N = 10  # number of grid points on a side
dy = dx = L/(N-1.0)
x = np.array(range(N))*dx
y = np.array(range(N))*dy
(x, y) = np.meshgrid(x, y)
u0 = np.zeros((N, N))
u1 = np.zeros((N, N))

# boundary conditions
for j in range(N):
    u1[j, N-1] = u0[j, N-1] = 1.0

n = 0  # number of iterations
err = 1.0  # average error per site
while err > eps:
    # next iteration in refinement
    n = n+1
    err = 0.0
    for j in range(1, N-1):
        for k in range(1, N-1):
            u1[j, k] = (u0[j-1, k]+u0[j+1, k]+u0[j, k-1]+u0[j, k+1])/4.0
            err += abs(u1[j, k]-u0[j, k])
    err /= N**2
    (u0, u1) = (u1, u0)  # swap old and new arrays for next iteration

# surface plot of final solution
fig = plt.figure(figsize=(8, 8))
axis = fig.gca(projection='3d', azim=-60, elev=20)  # 画三维视图
surf = axis.plot_surface(x, y, u0.T, rstride=1, cstride=1)  # u0.T代表转置
axis.contour(x, y, u0.T, 10, zdir='z', offset=-1.0)
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('u')
axis.set_zlim(-1.0, 1.0)
plt.title('t steps = %6f' % n)
plt.show()
