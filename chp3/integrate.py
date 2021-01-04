from gaussxw import gaussxw


def simpsons(f, a, b, N):
    '''Simpsons integral
    f: function to be integrated
    a: begin  
    b: end
    N: grid number (should be int)'''
    h = (b-a)/N  # grid size
    S = h * 1/3 * (f(a) + f(b))  # begin and end

    for i in range(1, N, 2):  # odd
        S += h * 4/3*f(a+i*h)

    for i in range(2, N, 2):  # even
        S += h * 2/3*f(a+i*h)
    return S


def trapezoid(f, a, b, N):
    '''trapzoid integral
    f: function to be integrated
    a: begin  
    b: end
    N: grid number (should be int)'''
    h = (b-a)/N  # grid size
    S = 1/2 * (f(a) + f(b)) * h  # begin and end
    for i in range(1, N):  # body part integral
        S += h * f(a+i*h)  # add
    return S


def gauss(f, a=0, b=1, N=25):
    x, w = gaussxw(N)  # 采样点与权重
    xp = 0.5 * (b-a) * x + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w

    S = 0.
    for k in range(N):
        S += wp[k] * f(xp[k])
    return S
