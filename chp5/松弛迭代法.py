# 做上面的(b)部分练习，看到结果不收敛。再尝试修改程序，做(c)部分，使用松弛法求解出x和y的值
# 参考答案

from math import exp, sqrt, log
import matplotlib.pyplot as plt
x1 = 1.5
y1 = 0.9
a = 1.0
b = 2.0
xs = [x1]
ys = [y1]
for k in range(50):
    x = sqrt(b/y1-a)**0.5
    y = (x1-a*y1)/x1**2.0
    x1 = x
    y1 = y
    xs.append(x1)
    ys.append(y1)
    # print(x1, y1) 查看x1和y1的结果

plt.figure()
plt.plot(xs, 'r.')
plt.plot(ys, 'b.')
plt.xlabel('N')
plt.ylabel('x, y')
plt.show()
