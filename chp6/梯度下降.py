# 一个程序例子：
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 求fxy的函数值


def fxy(x, y):
    return (x - 10) ** 2 + (y - 10) ** 2


def gradient_descent():
    times = 50  # 迭代次数限制
    gamma = 0.05  # 固定的步长
    x = 20  # x的初始值
    y = 20  # y的初始值

    fig = Axes3D(plt.figure())      # 将图转化为3D
    xp = np.linspace(0, 20, 100)
    yp = np.linspace(0, 20, 100)
    xp, yp = np.meshgrid(xp, yp)    # 将数据转化为网格数据
    zp = fxy(xp, yp)
    fig.plot_surface(xp, yp, zp, rstride=1, cstride=1,
                     cmap=plt.get_cmap('rainbow'))

 # 梯度下降算法
    for i in range(times):
        xb = x          # 用于画图
        yb = y          # 用于画图
        fb = fxy(x, y)  # 用于画图

        x = x - gamma * 2 * (x - 10)  # 根据梯度和gamma取值来迭代求下一步的x值
        y = y - gamma * 2 * (y - 10)
        f = fxy(x, y)
        # 关于这里的输出语法，请自行百度"python的格式化输出"学习
        print("第%d次迭代：x=%f，y=%f，fxy=%.10f" % (i + 1, x, y, f))

        fig.plot([xb, x], [yb, y], [fb, f], 'k.', lw=2, ls='-')
    plt.show()


if __name__ == "__main__":
    gradient_descent()
