import math
invphi = (math.sqrt(5) - 1) / 2  # 1/phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1/phi^2


def gssrec(f, a, b, tol=1e-5, h=None, c=None, d=None, fc=None, fd=None):
    (a, b) = (min(a, b), max(a, b))
    if h == None:
        h = b-a
    if h <= tol:
        return (a, b)  # 跳出
    if c == None:
        c = a + invphi2*h
    if d == None:
        d = a + invphi*h
    if fc == None:
        fc = f(c)
    if fd == None:
        fd = f(d)
    if fc < fd:
        return gssrec(f, a, d, tol, h*invphi, c=None, fc=None, d=c, fd=fc)
    else:
        return gssrec(f, c, b, tol, h*invphi, c=d, fc=fd, d=None, fd=None)
