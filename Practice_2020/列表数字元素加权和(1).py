a = eval(input())
def fn(base, power):
    if type(base) == int:
        return base * power
    else:
        return sum(fn(i, power+1) for i in base)
print(fn(a, 0))