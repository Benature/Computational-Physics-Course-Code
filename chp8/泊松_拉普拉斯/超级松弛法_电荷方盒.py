import mpl_toolkits.mplot3d
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np

eps = 1e-5  # fractional error allowed
L = 1.0  # half-length of each side
N = 51  # N number of grid points on a side
dz = dy = dx = 2.0*L/(N-1.0)
x = -L + np.array(range(N))*dx
y = -L + np.array(range(N))*dy
z = -L + np.array(range(N))*dz

u = np.zeros((N, N, N))
rho = np.zeros((N, N, N))

# source
q = 1.0
rho[(N-1)//2, (N-1)//2, (N-1)//2] = q/(dx*dy*dz)
s = u[:, :, (N-1)//2]

# compute over-relaxation parameter
omega = 2.0 / (1.0 + np.sin(np.pi*dx/L))
white = [(i, j, k) for i in range(1, N-1) for j in range(1, N-1)
         for k in range(1, N-1) if (i+j+k) % 2 == 0]
black = [(i, j, k) for i in range(1, N-1) for j in range(1, N-1)
         for k in range(1, N-1) if (i+j+k) % 2 == 1]

n = 0  # number of iterations
err = 1.0  # average error per site

while err > eps:   # 迭代计算过程：
    # next iteration in refinement
    n = n + 1
    err = 0.0
    for (i, j, k) in white+black:  # loop over white pixels then black pixels
        du = (u[i-1, j, k] + u[i+1, j, k] + u[i, j-1, k] +
              u[i, j+1, k] + u[i, j, k-1] + u[i, j, k+1] +
              dx**2 * rho[i, j, k])/6.0 - u[i, j, k]
        u[i, j, k] += omega * du
        err += abs(du)
    err /= N**3

s = u[:, :, (N-1)//2]

# surface plot of final solution
x, y = np.meshgrid(x, y)
s = s.clip(eps, 1.0)
image = plt.imshow(s.T, origin='lower', extent=(-L, L, -L, L), vmax=1.0)
plt.colorbar(image)
plt.show()

levels = [10**(l/2.0) for l in range(-5, 0)]
fig = plt.figure(figsize=(10, 8))
axis = fig.gca(projection='3d', azim=-60, elev=20)
surf = axis.plot_surface(x, y, s.T, rstride=1, cstride=1, linewidth=0.25,
                         cmap=plt.cm.jet, norm=matplotlib.colors.LogNorm())

axis.contour(x, y, s.T, levels, zdir='z', offset=-1.0,
             norm=matplotlib.colors.LogNorm())
axis.contourf(x, y, s.T, 1, zdir='x', offset=-L)
axis.contourf(x, y, s.T, 1, zdir='y', offset=L)
axis.set_zlim(-1.0, 1.0)
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('u')
plt.show()
