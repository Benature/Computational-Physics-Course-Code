import numpy as np
import matplotlib.pyplot as plt

# initialize
delta_t = 0.02
delta_x = 0.02
c = 1  # 波速
tao = c * delta_t / delta_x

x_max = 50
t_max = 79
u = np.zeros((x_max+1, t_max+1))

# 初始条件
for i in range(0, x_max+1):
    u[i][0] = np.sin(i * delta_x * np.pi)
    u[i][1] = np.sin(i * delta_x * np.pi)

# 边界条件
u[0, :] = 0
u[x_max, :] = 0

for t in range(1, t_max):
    for x in range(1, x_max):
        u[x][t+1] = 2*(1 - tao**2) * u[x][t] - u[x][t-1] + \
            tao**2 * (u[x-1][t]+u[x+1][t])

x = np.arange(0, 1.02, 0.02)
for t in range(0, 80, 2):
    plt.plot(x, u[:, t], 'r')

plt.xlabel('x/cm')
plt.ylabel('y/cm')
plt.show()
