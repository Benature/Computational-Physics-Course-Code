# 练习：请修改前面的程序，来使用 v(t) = k*sin(2pi/Period*t+phi0)这个模型来拟合data_fitting_planet1.txt中的观测数据。
# 参考答案。

# 使用emcee来做模型拟合，拟合系外行星的周期参数
# 初始参数设置离最终模型最佳参数很远的时候
#np.random.randn(N), 返回N个高斯分布随机数
# np.random.rand(N)， 返回N个[0,1)的随机数

from IPython.display import display, Math
from numpy import sin, pi
import corner
import matplotlib.pyplot as plt
import emcee
import numpy as np
# %matplotlib inline


def lnprior(theta):
    m, b, phi = theta
    if 0.0 < m < 21.0 and 0.0 < b < 15.0 and 0.0 < phi < 2*pi:
        return 0.0
    return -np.inf


def lnlike(theta, x, y, yerr):
    m, b, phi = theta
    model = m * sin(b*x+phi)
    inv_sigma = 1.0/(yerr**2)
    return -0.5*(np.sum((y-model)**2*inv_sigma))


def lnprob(theta, x, y, yerr):
    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + lnlike(theta, x, y, yerr)


# Choose the "true" parameters.
m_true = 10.91
b_true = 4.294
phi_true = 0.5
labels = ["K", "Period", "phi"]

# Generate some synthetic data from the model.
N = 100
x = np.sort(10*np.random.rand(N))
yerr = 0.2+0.0*np.random.rand(N)
y = m_true*sin(b_true*x+phi_true)
y += yerr * np.random.randn(N)


# load data
datum = np.loadtxt('../../data/10/data_fitting_planet1.txt')
print(datum.shape)
x = datum[:, 0]
y = datum[:, 1]
yerr = datum[:, 2]


plt.figure()
plt.errorbar(x, y, fmt='r.', yerr=yerr)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

ndim, nwalkers = 3, 100
# 马科夫链的初始起点放在一些随机参数点上
# 只要在prior方程限定范围，还是能找到最佳拟合值
pos = np.zeros((nwalkers, 3))
for i in range(nwalkers):
    pos[i, 0] = 20*np.random.rand(1)
    pos[i, 1] = 10.0*np.random.rand(1)
    pos[i, 2] = 2*pi*np.random.rand(1)

# 马科夫链的起点放在了最佳拟合值附近
pos = [[10.9, 4.4, 0.51] + 1e-2*np.random.randn(ndim) for i in range(nwalkers)]
#pos = [result["x"] + 3*np.random.randn(ndim) for i in range(nwalkers)]
#pos = [[11,4.4, 0.55] + 0.1*np.random.randn(ndim) for i in range(nwalkers)]

sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))

# 每个链都跑N_mcmc步
N_mcmc = 5000
sampler.run_mcmc(pos, N_mcmc)
# burn-in, 烧掉开头的一些链
N_burn = 1000
samples = sampler.chain[:, N_burn:, :].reshape((-1, ndim))

fig = corner.corner(samples, labels=["$m$", "$b$", "$phi$"],
                    truths=[m_true, b_true, phi_true])
fig.savefig("triangle.png")

plt.figure(figsize=(8, 6))
x2 = np.array([0, 10])
x2 = x
for m, b, phi in samples[np.random.randint(len(samples), size=100)]:
    plt.plot(x2, m*sin(b*x2+phi), color="k", alpha=0.1)
plt.plot(x2, m_true*sin(b_true*x2+phi_true), color="r", lw=2, alpha=0.8)
plt.errorbar(x, y, yerr=yerr, fmt=".k")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# plot the evolution of the first parameter to check the result
plt.figure()
plt.plot(samples[:, 0])
plt.show()


# 两种不同的计算模型参数分布的方法
# 方法一
for i in range(ndim):
    mcmc = np.percentile(samples[:, i], [16, 50, 84])
    q = np.diff(mcmc)
    txt = "\mathrm{{{3}}} = {0:.3f}_{{-{1:.3f}}}^{{{2:.3f}}}"
    txt = txt.format(mcmc[1], q[0], q[1], labels[i])
    display(Math(txt))


# 方法二
m_mcmc, b_mcmc, phi_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
                               zip(*np.percentile(samples, [16, 50, 84],
                                                  axis=0)))

print("Semi-amplitude = ", m_mcmc)
print("period = ", b_mcmc)
print("phi=", phi_mcmc)

print("Semi-amplitude (in m/s) = ", m_mcmc[0])
print("period (in day) = ", 2*pi/b_mcmc[0])
print("phi=", phi_mcmc)

# 使用简单的公式计算行星的质量
print("planet mass in Jupiter mass =  ",
      m_mcmc[0]/28.4*(2*pi/b_mcmc[0]/365.24)**(1.0/3.0))
