# 静质量为零物体的运动轨迹
# 这个就留给同学们自己计算了，对引力透镜效应感兴趣，对黑洞把光线弯曲感兴趣，或者对100年前爱丁顿测量日食，
# 恒星位置偏移量感兴趣的同学可以自行计算。比上面的要简单些，初始条件可以搞成phi=0, u约等于0(从很远的地方射过来的光子)

# 静质量非零物体的运动轨迹
import matplotlib.pyplot as plt
import numpy as np

M = 1.0
G = 1.0
phi_max = 1.00*np.pi
dphi = 0.00001  # 相位角的步长

# 根据步长和总的相位角计算总步数
nsteps = int(phi_max/dphi)
u = np.zeros(nsteps)  # 初始化每一步的u, 长度为nsteps
v = np.zeros(nsteps)  # 初始化每一步的v, 长度为nsteps
phi = np.zeros(nsteps)  # 初始化每一步的相位角phi的list ,长度为nsteps


# 初始条件，强烈的光线弯曲
phi[0] = -0.8*np.pi
u[0] = 4e-2  # 1e-8
v[0] = 0.1  # 0.001

# 初始条件，弱的光线弯曲, u~q*cos(phi)
#phi[0] = -0.48*np.pi
#u[0] = 2e-6
#v[0] = 0.001


for i in range(nsteps-1):
    phi[i+1] = phi[i]+dphi
    u[i+1] = u[i]+dphi*v[i]
    v[i+1] = v[i]+dphi*(3*u[i]**2-u[i])

# 下面开始作图
plt.figure(figsize=(8, 6))
plt.plot(phi, u)
plt.xlabel('phi')
plt.ylabel('u')
plt.title('Orbit')
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(1.0/u*np.cos(phi), 1.0/u*np.sin(phi))
# plt.ylim(-1e5,1e5)
# plt.xlim(-1e4,1e4)
plt.plot(0.0, 0.0, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Orbit')
plt.show()
