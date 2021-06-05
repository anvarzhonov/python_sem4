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
        elif x[2] == "mql5":
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
            elif x[1] == 1965:
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
    originalTable = [[f"{done(i[0])}",
                      f"{date(i[1])}",
                      f"{rounder(i[3])}",
                      f"{mail(i[4])}"] for i in x]

    table = []

    for i in originalTable:
        if i not in table:
            table.append(i)

    def transpose(tab):
        return [list(row) for row in zip(*tab)]

    z = transpose(table)

    return z


def rounder(x):
    num = round(float(x), 2)
    num *= 100
    return str(('%f' % num).rstrip('0').rstrip('.'))+"%"


def date(x):
    a = x[6]+x[7]+x[2]+x[3]+x[4]+x[2]+x[0]+x[1]
    return a


def done(x):
    if x == 'Не выполнено':
        return 'Нет'
    else:
        return 'Да'


def mail(x):
    rez = ""
    list(x)
    for i in range(len(x)):

        if x[i] == "@":
            rez = x[i+1:]
    return rez


print(f23([
    ['Не выполнено', '00-04-26', None, '0.681', 'bifskij35@mail.ru'],
    ['Выполнено', '21-04-04', None, '0.892', 'bifskij35@yahho.ru'],
    ['Не выполнено', '00-04-26', None, '0.681', 'bifskij35@mail.ru'],
    ['Выполнено', '01-02-21', None, '0.345', 'bifskij35@mai4п.com'],
]))
