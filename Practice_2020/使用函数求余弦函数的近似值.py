def funcos(eps, x):
    temp = 0
    cos = 0
    i = 0
    j = 1
    while True:
        temp = x ** i / jiec(i)
        if abs(temp) > eps:
            cos = cos + temp*j
            j *=-1
            i += 2
        else:
            break
    return cos


def jiec(a):
    s = 1
    if a <= 0:
        return s
    else:
        for i in range(1, a + 1):
            s = s * i
    return s

eps = float(input())
x = float(input())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))
