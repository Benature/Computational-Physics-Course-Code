# Computational Physics Course 计算物理课程代码

Course in 2020-2021, cover most exercise code.

---

## Chp3 数值微积分

- 数值误差
	- [[Chp03_数值微积分#舍入误差（Rounding Error）]]：浮点截断
	- [[Chp03_数值微积分#截断误差（Truncation Error）]]：泰勒展开截断

### 数值微分
[[Chp03_数值微积分#3 4 数值微分 Numerical Differentiation]]
差分法

### 数值积分

- [[Chp03_数值微积分#3 5 1 梯形法]]
- [[Chp03_数值微积分#3 5 2 辛普森积分法 Simpson’s Rule]]
- [[Chp03_数值微积分#高斯积分法]]
	- [[Chp03_数值微积分#无穷积分]]
- [[Chp03_数值微积分#3 5 6 Scipy的积分]]

## Chp4 线性方程

- 求解
	- [[Chp04_线性方程#4 3 逆矩阵解法]]
	- [[Chp04_线性方程#4 4 高斯消元法]]
	- [[Chp04_线性方程#4 5 LU分解法（三角分解法）]]
	- [[Chp04_线性方程#4 6 雅克比 Jacobi 迭代法求解]]
- 本征值
	- [[Chp04_线性方程#4 7 QR求解特征值和特征向量]]

## Chp5 非线性方程

- [[Chp05_非线性方程#5 1 二分法]]
- [[Chp05_非线性方程#5 2 松弛 迭代法]]
- [[Chp05_非线性方程#5 3 牛顿迭代法 Newton-Raphson Method]]
- [[Chp05_非线性方程#5 4 正切法]]

## Chp6 极值求解和优化问题
- 裸代码
	- [[Chp06_极值与优化#6 1 黄金分割法 Golden Ratio Golden Section method]]
	- [[Chp06_极值与优化#6 5 梯度下降法 Gradient Descent Steepest Descent]]
- [[scipy.optmize]]
	- [[Chp06_极值与优化#6 2 一维问题中的Brent方法]]
		`result = optimize.minimize_scalar(f)`
	- [[Chp06_极值与优化#6 3 牛顿法]]
		`optimize.minimize(f, [2,-1], method="Newton-CG", jac=jacobian, hess=hessian)`
		- [[Chp06_极值与优化#6 4 准牛顿法]]
			`optimize.minimize(f, [2, -1], method="BFGS", jac=jacobian)`
			`optimize.minimize(f, [2, 2], method="L-BFGS-B", jac=jacobian)`
	- [[Chp06_极值与优化#6 6 Downhill Simplex Method 下山单纯形法，下降单纯形法）]]
		 `optimize.minimize(f, [2, -1], method="Nelder-Mead") `
	- [[Chp06_极值与优化#6 7 全局优化]] 
		`optimize.brute(f, ((-1, 2), (-1, 2))) `
	- [[Chp06_极值与优化#6 9 线性规划和优化问题]]

## Chp7 ODE
- 初值问题
	- [[Chp07-1_ODE#欧拉法]]：线性误差积累严重
	- [[Chp07-1_ODE#7 3 龙格-库塔法]]
		- [[Chp07-1_ODE#RK2]]
		- [[Chp07-1_ODE#RK4]]
		- [[Chp07-1_ODE#RK45]]：变步长
	- [[Chp07-2_ODE#7 5 1 蛙跳法 leapfrog method]]
- 边界值问题
	- [[Chp07-2_ODE#7 6 1 射击法 Shooting method 打靶法]]

## Chp8 PDE
- 偏微分方程分类
	- $b^2-4ac>0$, 双曲线 
	- $b^2-4ac=0$, 抛物线 
	- $b^2-4aC<0$, 椭圆


- [[Chp08-1_PDE#8 2 波动方程]]
	- [[Chp08-1_PDE#欧拉 显式差分 FTCS]]
		不稳定
	- [[Chp08-1_PDE#Lax 格式]]
		有耗散
	- [[Chp08-1_PDE#蛙跳法]]  ([[蛙跳法]])
		能量守恒，无耗散
- [[Chp08-1_PDE#8 2 热传导方程]]
	- [[Chp08-1_PDE#隐式格式]]
		使用未来的数据，需要总体算完 u 矩阵
- [[Chp08-2_PDE#8 3 拉普拉斯方程和泊松方程求解]]
	- [[Chp08-2_PDE#松弛迭代法]]
	- [[Chp08-2_PDE#超级松弛迭代法]]
- [[Chp08-2_PDE#8 4 含时间的薛定谔方程求解]]

[[Chp08-1_PDE#^courant]]

## Chp9 随机 & 蒙特卡洛
重点在 [[Chp09-1_随机萌卡#9 2 1 定积分中的应用]]：
	和以前我们学过的梯形法和辛普森法求定积分相比,蒙特卡罗法的 程序比较简单,计算的误差和维数和边界的复杂程度无关,所以它 具有以下特点

-   优势:高维度,不规则的积分区域
-   劣势:
    - 精度不容易提高,精度仅仅正比于 $N^{0.5}$
    - 误差正比于 $\sigma \propto 1 / \sqrt{N} * I$
    - 要得到10%的精度,需要撒N=100个点。如果使用辛普森积分法, 计算中使用N=100个步长点,则精度可以到1E-8
- 方法
	- [[Chp09-1_随机萌卡#一维定积分掷点法]]
	- [[Chp09-1_随机萌卡#一维定积分平均值法]]
	- [[Chp09-1_随机萌卡#一维定积分重要抽样法]]

## Chp10* MCMC
应该不考，略

## Chp11 傅里叶周期信号
- [[Chp11_FT#离散傅里叶变换]]
- [[Chp11_FT#卷积运算和图像处理]]：可略
- [[Chp11_FT#10 3 非均匀采样和Lomb-Scargle周期功率谱]]
	- [[Chp11_FT#Lomb-Scargle]]
	- [[Chp11_FT#Boot-Strapping]]

## Chp12 流体

- [[Chp12_流体#12 1 顶盖驱动问题求解]]
- [[Chp12_流体#12 2 激波问题求解]]