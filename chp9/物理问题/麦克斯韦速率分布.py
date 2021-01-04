# 理想气体的速度麦克斯韦分布
import statistics
import math
from random import random, randrange
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline


def vout(v1, v2, alpha, gamma):
    v1out = math.sqrt(0.5*v1**2+0.5*v2**2 +
                      0.5*(v1**2-v2**2)*math.cos(gamma)+v1*v2*math.sin(alpha)*math.sin(gamma))
    v2out = math.sqrt(0.5*v1**2+0.5*v2**2 -
                      0.5*(v1**2-v2**2)*math.cos(gamma)-v1*v2*math.sin(alpha)*math.sin(gamma))
    return v1out, v2out


N = 1000  # 100000 # 总分子数
nstep = 5000  # 50000000
v = np.linspace(0, 1000, N)
print("total energy initial:  ", sum(v**2))
for i in range(nstep):
    k1 = randrange(N)  # int(random()*N)
    k2 = randrange(N)  # int(random()*N)
    vin1 = v[k1]
    vin2 = v[k2]
    alpha = 2*math.pi*random()
    gamma = 2*math.pi*random()
    v1out, v2out = vout(vin1, vin2, alpha, gamma)
    v[k1] = v1out
    v[k2] = v2out


plt.figure(figsize=(10, 5))
# 数据的直方图
n, bins, patches = plt.hist(v, 40, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Speed')
plt.ylabel('Probability')


# 添加标题
plt.title('Maxwell Speed distribution')
plt.axis([0, 1300, 0, 0.002])
plt.grid(True)
plt.show()


print("total energy final: ", sum(v**2))  # conservation of energy
print((sum(v**2)/N)**0.5)
print(statistics.mean(v))
print((sum(v**2)/N)**0.5/statistics.mean(v)*(3*3.14/8.0)**0.5)
