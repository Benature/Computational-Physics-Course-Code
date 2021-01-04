# 计算地球表面的二维投射问题
import math
import matplotlib.pyplot as plt

g = 9.8  # standard freefall (m/s^2)
v0 = 10.0  # initial velocity (m/s)
angles = [30.0, 35.0, 40.0, 45.0, 50.0, 55.0]  # launch angles (degrees)
dt = 0.01  # time step (s)
for theta in angles:
    x = [0.0]
    y = [0.0]
    vx = [v0*math.cos(theta*math.pi/180.0)]
    vy = [v0*math.sin(theta*math.pi/180.0)]

    # use Euler's method to integrate projectile equations of motion
    # 使用while循环，当发射的物体触地的时候，就停止计算
    while y[-1] >= 0.0:
        # apply finite difference approx to equations of motion
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        vx.append(vx[-1])
        vy.append(vy[-1]-g*dt)

    # plot the trajectory
    plt.plot(x, y, label=str(theta)+' degrees')

plt.title('trajectory of a projectile')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(bottom=0.0)  # 图的下限画图范围设置为0
plt.legend()
plt.show()
