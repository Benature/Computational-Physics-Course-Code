# 参考答案
# 使用emcee来做直线模型拟合练习，使用错误的误差模型。
import corner
import matplotlib.pyplot as plt
import emcee
import numpy as np
# %matplotlib inline

# we know the "true" parameters.
m_true = -0.9594
b_true = 4.294
f_true = 0.534

# Generate some synthetic data from the model.
datum = np.loadtxt('../../data/10/data_fitting_class21.txt')
x = datum[:, 0]
y = datum[:, 1]
yerr = datum[:, 2]
N = len(x)


def lnlike(theta, x, y, yerr):
    m, b, f = theta
    model = m * x + b
    inv_sigma2 = 1.0/((yerr/f)**2)
    return -0.5*(np.sum((y-model)**2*inv_sigma2 - np.log(inv_sigma2)))


def lnprior(theta):
    m, b, f = theta
    if -5.0 < m < 5 and -10 < b < 10.0 and 0 < f < 1.0:
        return 0.0
    return -np.inf


def lnprob(theta, x, y, yerr):
    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + lnlike(theta, x, y, yerr)


plt.figure()
plt.errorbar(x, y, fmt='r.', yerr=yerr)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


ndim, nwalkers = 3, 100
pos = np.zeros((nwalkers, 3))
# 马科夫链的起点放在了比较随机的点上，做大范围参数搜寻
for i in range(nwalkers):
    pos[i, 0] = 10*np.random.rand(1)-5.0
    pos[i, 1] = 20.0*np.random.rand(1)-10.0
    pos[i, 2] = np.random.rand(1)

# 马科夫链的起点放在了最佳拟合值附近，在小范围内搜索最佳拟合值
pos = [[-0.8, 3.2, 0.12] + 1e-1*np.random.randn(ndim) for i in range(nwalkers)]

sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))

sampler.run_mcmc(pos, 2000)
# burn-in, 烧掉开头的链
samples = sampler.chain[:, 500:, :].reshape((-1, ndim))

fig = corner.corner(samples, labels=["$m$", "$b$", "$f$"],
                    truths=[0, 0, 0.5])

fig.savefig("triangle.png")

plt.figure(figsize=(8, 6))
xl = np.array([0, 10])
for m, b, f in samples[np.random.randint(len(samples), size=100)]:
    plt.plot(xl, m*xl+b, color="k", alpha=0.1)
plt.errorbar(x, y, yerr=yerr, fmt=".k")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

m_mcmc, b_mcmc, f_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
                             zip(*np.percentile(samples, [16, 50, 84],
                                                axis=0)))
print("m= ", m_mcmc)
print("b=", b_mcmc)
print("f= ", f_mcmc)
