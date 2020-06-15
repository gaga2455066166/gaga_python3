a = eval(input())
def fn(base):
    if type(base) == int:
        return base
    else:
        return sum(fn(i) for i in base if type(i) != str)
print(fn(a))