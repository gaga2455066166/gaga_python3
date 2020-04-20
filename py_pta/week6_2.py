def prime(p):
    if p < 2:
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, p):
            if (p % i) == 0:
                return False
        return True


def PrimeSum(m, n):
    s = 0
    for i in range(m, n + 1):
        if prime(i):
            s += i
    return s
