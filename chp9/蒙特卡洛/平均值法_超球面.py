# 练习：请在这个程序单元中，练习求一个三维球体体积的积分
# 参考答案见下面.
# 求一个N_d维超球面的体积
from random import random
import numpy as np

N_d = 7  # 球面的维数
N = 10000  # 取样点的总数目

r = np.zeros(N_d)
tot = 0.0


def f(r):
    if sum(r**2) <= 1:
        return 1
    else:
        return 0


for i in range(N):
    for j in range(N_d):
        r[j] = random()
    tot += f(r)

I1 = 2.0**N_d*tot/N/np.pi**(N_d//2)
I2 = 2.0**N_d*tot/N  # 积分结果

print(I1, I2)
