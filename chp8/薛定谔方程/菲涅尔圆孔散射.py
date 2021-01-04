# 二维含时间薛定谔问题解法，散射
import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# solves the tridiagonal system of equations A.x = b


def tridiag(alp, bet, gam, b):
    n = len(bet)
    x = np.zeros(b.shape, dtype=complex)
    y = np.zeros(b.shape, dtype=complex)
    y[0] = gam[0]/bet[0]
    x[0] = b[0]/bet[0]
    for i in range(1, n):
        den = bet[i]-alp[i]*y[i-1]
        y[i] = gam[i]/den
        x[i] = (b[i]-alp[i]*x[i-1])/den
    for i in reversed(range(n-1)):
        x[i] -= x[i+1]*y[i]
    return x


hbar = 1.0  # reduced Planck's constant
m = 1.0  # mass
k0 = 1.0  # initial wavenumber

# grid and time intervals
dy = dx = 0.5/k0
dt = 0.5*m/(hbar*k0**2)
ymin = xmin = -30.0/k0
ymax = xmax = 30.0/k0

# initial data
x = np.arange(xmin, xmax, dx)
y = np.arange(ymin, ymax, dy)
N = len(x)
u = np.zeros((N, N), dtype=complex)
v = np.zeros((N, N), dtype=complex)
p = np.zeros((N, N))
x0 = -15.0/k0
y0 = 0.0/k0
sigma = 5.0/k0
for j in range(N):
    for k in range(N):
        rr = (x[j]-x0)**2+(y[k]-y0)**2
        u[j, k] = cmath.exp(-rr/(4.0*sigma**2)+1j*k0*x[j])
        p[j, k] = u[j, k].real**2+u[j, k].imag**2

# potential 势阱
a = 2.0/k0
E0 = (hbar*k0)**2/(2.0*m)
V = np.zeros((N, N))
for j in range(N):
    for k in range(49, 52):
        if 58 < j < 62:
            continue
        V[k, j] = E0
    # for k in range(N):
    #     rr = x[j]**2+y[k]**2
    #     if rr < a**2:
    #         V[j, k] = E0


# setup coefficients of the tridiagonal matrix
alpha = gamma = -1j*hbar*dt/(4.0*m*dx**2)
alp = alpha*np.ones(N, dtype=complex)
gam = gamma*np.ones(N, dtype=complex)
bet = np.zeros((N, N), dtype=complex)
for j in range(N):
    for k in range(N):
        bet[j, k] = 1.0-2.0*alpha+1j*(V[j, k]/(2.0*hbar))*dt

# preform the evolution; blithely ignore boundary conditions
t = 0.0
tmax = 30.0*m/(hbar*k0**2)
it = 0
while t-tmax < 0.5*dt:
    # update plot
    for j in range(N):
        for k in range(N):
            p[j, k] = u[j, k].real**2+u[j, k].imag**2
    if it % 10 == 0:  # 每隔50时间步画一幅图
        plt.figure()
        plt.xlabel('x')
        plt.ylabel('y')
        image = plt.imshow(p.T, origin='upper', extent=(xmin, xmax, ymin, ymax),
                           cmap=plt.cm.hot)
        plt.contour(V.T, origin='upper', extent=(
            xmin, xmax, ymin, ymax), colors='c')

        image.set_data(p.T)
        plt.title('t = %5f' % t)
        plt.show()

    # first step of operator splitting
    for j in range(1, N-1):
        for k in range(1, N-1):
            v[j, k] = -alpha*u[j, k-1]+(2.0-bet[j, k])*u[j, k]-gamma*u[j, k+1]
    for k in range(1, N-1):
        u[:, k] = tridiag(alp, bet[:, k], gam, v[:, k])

    # second step of operator splitting
    for k in range(1, N-1):
        for j in range(1, N-1):
            v[j, k] = -alp[j]*u[j-1, k] + \
                (2.0-bet[j, k])*u[j, k]-gam[j]*u[j+1, k]
    for j in range(1, N-1):
        u[j, :] = tridiag(alp, bet[j, :], gam, v[j, :])
    t += dt
    it = it+1

# plt.show()


# freeze final plot
plt.figure()
plt.xlabel('x')
plt.ylabel('y')
image = plt.imshow(p.T, origin='upper', extent=(xmin, xmax, ymin, ymax),
                   cmap=plt.cm.hot)
plt.contour(V.T, origin='upper', extent=(xmin, xmax, ymin, ymax), colors='c')

image.set_data(p.T)
plt.title('final plot, t = %5f' % t)
plt.show()
