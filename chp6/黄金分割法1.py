# 黄金分割算法函数
def golden(f, a, b, c, eps=1e-6):
    """ Uses a golden section search for the minimum of a function. """
    goldenratio = 0.5+0.5*5.0**0.5
    tolerance = eps**0.5
    fb = f(b)
    while abs(a-c) > tolerance:
        # make sure that b is closer to c
        if abs(b-a) < abs(c-b):
            (a, c) = (c, a)
        x = a+(b-a)/goldenratio
        fx = f(x)
        if fx < fb:
            (a, b, c) = (a, x, b)
            fb = fx
        else:
            (a, b, c) = (x, b, c)
    if fx < fb:
        return (x, fx)
    else:
        return (b, fb)

# Richard Buckingham Potential


def f(r):
    return (sigma/r)**6 - exp(-r/sigma)


y = golden(f, 0.1, 5, 2.0, eps=1e-6)
# 用 golden函数来求解f(r)函数的最小值
print("最小值的位置r 和 f(r) = ", y)
