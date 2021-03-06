


def fast_pow(x, y, res=1):
    while y > 0:
        if y == 1:
            return res * x
        if y % 2 != 0:
            res *= x
        x *= x
        y //= 2
    return res


def test():
    for x in range(101):
        for y in range(101):
            assert fast_pow(x, y) == x ** y
    print("Done!")
