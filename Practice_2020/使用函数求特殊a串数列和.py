def fn0(a, n):
    str_a = str(a)
    str_as = str_a * n
    return int(str_as)


def fn(a, n):
    s = 0
    for i in range(1, n + 1):
        s = s + fn0(a, i)
    return s
