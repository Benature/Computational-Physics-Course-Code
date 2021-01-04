# 请在此程序单元中，修改上面的欧拉法，使用欧拉-克罗莫方法啊计算单摆问题

# 练习参考答案.
#Euler-Cromer, 稳定的单摆积分
import matplotlib.pyplot as plt
# %matplotlib inline

g = 9.8  # standard freefall (m/s^2)
l = 0.1
theta0 = 0.5
dt = 0.001
tmax = 30

nsteps = int(tmax/dt)
omega = [0.0]*nsteps
theta = [0.0]*nsteps
t = [0.0]*nsteps

# use Euler's method to integrate pendulum equations of motion
theta[0] = theta0
for i in range(nsteps-1):
    omega[i+1] = omega[i]-g/l*theta[i]*dt
    theta[i+1] = theta[i]+omega[i+1]*dt
    t[i+1] = t[i]+dt
plt.plot(t, theta)
plt.xlabel('time (s)')
plt.ylabel('theta (rad)')
plt.title('simple pendulum (Euler method)')
plt.show()
