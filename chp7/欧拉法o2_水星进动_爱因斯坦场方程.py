# 静质量非零物体的运动轨迹
import matplotlib.pyplot as plt
import numpy as np

M = 1.0
G = 1.0
# q2 = 2.6e-8# 中心物体的GM与绕转物体的轨道半径之比。对于 水星,肉眼几乎看不出短短几个轨道的变化
q2 = 0.026  # 我们把这个量放大1百万倍，来观察下一个假水星的进动。
e = 0.4
phi_max = 4.5*np.pi
dphi = 0.001  # 相位角的步长

# 根据步长和总的相位角计算总步数
nsteps = int(phi_max/dphi)
u = np.zeros(nsteps)  # 初始化每一步的u, 长度为nsteps
v = np.zeros(nsteps)  # 初始化每一步的v, 长度为nsteps
phi = np.zeros(nsteps)  # 初始化每一步的相位角phi的list ,长度为nsteps

# use Euler's method to integrate equation for radioactive decay
phi[0] = 0.0
u[0] = q2*(1+e)
v[0] = 0.0
for i in range(nsteps-1):
    phi[i+1] = phi[i]+dphi
    u[i+1] = u[i]+dphi*v[i]
    v[i+1] = v[i]+dphi*(q2+3*u[i]**2-u[i])

# 下面开始作图
plt.figure(figsize=(15, 15))
plt.polar(phi, 1.0/u, '.')
# plt.xlabel('phi')
# plt.ylabel('rho')
plt.title('Orbit')
plt.show()
