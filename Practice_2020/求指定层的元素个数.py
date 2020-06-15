a = eval(input())
layer = int(input())
def fn(base, deep, layer):
    if deep == layer:
        return len([i for i in base if type(i) == int])
    else:
        return sum(fn(i, deep+1, layer) for i in base if type(i) == list)
print(fn(a, 1, layer))