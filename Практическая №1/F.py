import math


def f11(x, y):
    d1 = ((math.e**y + math.e**x + 41) / (55*y - x**4))
    d2 = (x**3+18*y**8)
    d3 = (x**6/18+math.tan(x)+9)

    return d1-d2-d3


def f12(x):
    if x < 151:
        return math.exp**math.exp**x+math.fabs(x)+30
    if 151 <= x < 195:
        return math.tan(math.cos(x)+math.tan(x))+math.fabs(x)+76
    if 195 <= x < 285:
        return x**6+math.tan(x)
    if x >= 285:
        return 19*x**4+math.fabs(x)


def f13(n, m):
    s1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s1 += (j-i**5/94)

    s2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s2 += (math.log(i)+i**5)

    return s1 + 14*s2


def f14(n):
    if n == 0:
        return 6
    if n == 1:
        return 6
    else:
        return 1/98*f14(n-1)**2 + 1/33*f14(n-1)



