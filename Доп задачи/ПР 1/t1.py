

def naive_mul(x, y, res=0):
    for _ in range(y):
        res += x
    return res


def test():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("Done!")

test()
