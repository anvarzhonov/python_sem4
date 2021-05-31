
def f21(x):
    if x[3] == 2001:
        if x[2] == 'logos':
            if x[0] == 1999:
                return 0
            elif x[0] == 1970:
                return 1
            elif x[0] == 2007:
                return 2
        elif x[2] == 'haml':
            return 3
        elif x[2] == 'mql5':
            if x[1] == 1988:
                return 4
            elif x[1] == 1965:
                return 5
    elif x[3] == 2010:
        if x[2] == 'logos':
            return 6
        elif x[2] == 'haml':
            if x[1] == 1988:
                return 7
            elif x[1] == 1968:
                return 8
        elif x[2] == 'mql5':
            if x[1] == 1988:
                return 9
            elif x[1] == 1965:
                return 10


def f22(x):
    e = x & 0xFE000000
    d = x & 0x1800000
    c = x & 0x780000
    b = x & 0x7FC00
    a = x & 0x3FF

    b <<= 13
    e >>= 9
    c >>= 7
    d >>= 13

    x = a + b + c + d + e
    return x



def f23(x):



def done(x):
    if x == 'Не выполнено':
        return 'Нет'
    else:
        return 'Да'

