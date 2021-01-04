# 总程序示例
# 使用emcee来做模型拟合,被拟合的是一条直线。
import scipy.optimize as op
import corner
import matplotlib.pyplot as plt
import emcee
import numpy as np
# %matplotlib inline

# Choose the "true" parameters.
m_true = -0.9594
b_true = 4.294
f_true = 0.534  # 误差

# Generate some synthetic data from the model.
N = 50
x = np.sort(10*np.random.rand(N))
yerr = 0.1+0.5*np.random.rand(N)
y = m_true*x+b_true
y += np.abs(f_true*y) * np.random.randn(N)
y += yerr * np.random.randn(N)


def lnlike(theta, x, y, yerr):
    '''高斯误差模型'''
    m, b, lnf = theta
    model = m * x + b
    inv_sigma2 = 1.0/(yerr**2 + model**2*np.exp(2*lnf))
    return -0.5*(np.sum((y-model)**2*inv_sigma2 - np.log(inv_sigma2)))


def lnprior(theta):
    m, b, lnf = theta  # 参数 theta
    if -5.0 < m < 0.5 and 0.0 < b < 10.0 and -10.0 < lnf < 1.0:
        return 0.0
    return -np.inf


def lnprob(theta, x, y, yerr):
    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + lnlike(theta, x, y, yerr)


xfine = np.arange(0.0, 10, 0.1)
#yfit = [f(xx, popt[0], popt[1],popt[2]) for xx in xfine]
ytrue = [m_true*xx+b_true for xx in xfine]

plt.figure()
plt.errorbar(x, y, fmt='r.', yerr=yerr)
plt.plot(xfine, ytrue)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# 与我们前面的示例有些不同，使用scipy计算初始的最佳取值 FOCUS!
nll = lambda *args: -lnlike(*args)
result = op.minimize(nll, [m_true, b_true, np.log(f_true)], args=(x, y, yerr))
m_ml, b_ml, lnf_ml = result["x"]

ndim, nwalkers = 3, 100
# 马科夫链的起点放在了最佳拟合值附近
pos = [result["x"] + 1e-4*np.random.randn(ndim)
       for i in range(nwalkers)]  # 链的起点

# args 是数据
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))
sampler.run_mcmc(pos, 500)

# burn-in, 烧掉开头的链
samples = sampler.chain[:, 50:, :].reshape((-1, ndim))

fig = corner.corner(samples, labels=["$m$", "$b$", "$\ln\,f$"],
                    truths=[m_true, b_true, np.log(f_true)])
fig.savefig("triangle.png")


plt.figure(figsize=(8, 6))
xl = np.array([0, 10])
for m, b, lnf in samples[np.random.randint(len(samples), size=100)]:
    plt.plot(xl, m*xl+b, color="k", alpha=0.1)
plt.plot(xl, m_true*xl+b_true, color="r", lw=2, alpha=0.8)
plt.errorbar(x, y, yerr=yerr, fmt=".k")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


samples[:, 2] = np.exp(samples[:, 2])
m_mcmc, b_mcmc, f_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
                             zip(*np.percentile(samples, [16, 50, 84],  # 百分位数
                                                axis=0)))
print("m= ", m_mcmc)
print("b=", b_mcmc)
print("f= ", f_mcmc)

# 参数，左 sigma，右 sigma
