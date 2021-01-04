# 快递员问题
from math import sqrt, exp
from numpy import empty
from random import random, randrange, seed
import matplotlib.pyplot as plt

N = 25  # 多少个小镇
R = 0.02
Tmax = 10.0  # 最大的退火温度
Tmin = 1e-3  # 最小的退火温度
tau = 1e4  # 温度的半衰期

# Function to calculate the magnitude of a vector


def mag(x):
    return sqrt(x[0]**2+x[1]**2)

# Function to calculate the total length of the tour


def distance():
    s = 0.0
    for i in range(N):
        s += mag(r[i+1]-r[i])
    return s


# Choose N city locations and calculate the initial distance
r = empty([N+1, 2], float)
seed(1)  # 选择同样的城市组合位置
for i in range(N):
    r[i, 0] = random()
    r[i, 1] = random()
r[N] = r[0]  # 终点即是始点
D = distance()

seed()  # 随机种子，用系统时间做种子
plt.figure()
plt.plot(r[:, 0], r[:, 1], 'ro-')
plt.title('Temp=%g Dist=%g' % (T, D))
plt.show()

plt.figure()
# Main loop
t = 0
T = Tmax  # 初始温度
while T > Tmin:
    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)  # 用半衰期为tau的退火温度

    # Update the plot every 100 moves
    if t % 5000 == 0:
        plt.plot(r[:, 0], r[:, 1], 'ro-')
        plt.title('Temp=%g Dist=%g' % (T, D))
        plt.show()

    # Choose two cities to swap and make sure they are distinct
    i, j = randrange(1, N), randrange(1, N)
    while i == j:
        i, j = randrange(1, N), randrange(1, N)

    # Swap them and calculate the change in distance
    oldD = D
    r[i, 0], r[j, 0] = r[j, 0], r[i, 0]
    r[i, 1], r[j, 1] = r[j, 1], r[i, 1]
    D = distance()
    deltaD = D - oldD

    # If the move is rejected, swap them back again
    if random() > exp(-deltaD/T):
        r[i, 0], r[j, 0] = r[j, 0], r[i, 0]
        r[i, 1], r[j, 1] = r[j, 1], r[i, 1]
        D = oldD

plt.figure()
plt.plot(r[:, 0], r[:, 1], 'ro-')
plt.title('Temp=%g Dist=%g' % (T, D))
plt.show()
