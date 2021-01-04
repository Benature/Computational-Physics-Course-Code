import numpy as np
import matplotlib.pyplot as plt


def leap(t, x1, x2, f, dt):
    dx12 = dt * f(t+0.5*dt, x2)
    dx22 = dt * f(t+dt, x1+dx12)
    return x1 + dx12, x2 + dx22


def dXdt(t, X):
    x = X[0]
    vx = X[1]
    ax = -g / l * x
    return np.array([vx, ax])


g = 9.8
l = 1.
theta0 = 0.1
dt = 0.001
tmax = 20

nsteps = int(tmax/dt)
omega = [0.0] * nsteps
theta = [0.0] * nsteps
t = [0.0] * nsteps
energy = [0.0] * nsteps

theta[0] = theta0
omega[0] = 0.0
t[0] = 0.0

# X1 and X2 represent x(n*dt) and x(n*dt+0.5dt)
X1 = np.array([theta0, omega[0]])
X2 = X1+0.5*dt*dXdt(0, X1)

for i in range(nsteps-1):
    X1, X2 = leap(t[i], X1, X2, dXdt, dt)
    t[i+1] = t[i]+dt
    theta[i+1] = X1[0]
    omega[i+1] = X1[1]

omega = np.array(omega)
theta = np.array(theta)
energy = 0.5 * l**2 * omega**2 + 0.5 * g * l * theta**2
energy = energy / np.min(energy)

plt.plot(t, theta)
plt.xlabel('time(s)')
plt.ylabel('theta(rad)')
plt.title('simple pendulum (Leapfrog)')
plt.show()
plt.plot(t, energy)
plt.xlabel('time(s)')
plt.ylabel('energy')
plt.title('simple pendulum(Energy)')
plt.show()
