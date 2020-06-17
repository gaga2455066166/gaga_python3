def Prime(x):
    if x == 2:
        return True
    elif x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def PrimeSum(x, y):
    s = 0
    for j in range(x, y + 1):
        if Prime(j) == True:
            s += j
    return s
