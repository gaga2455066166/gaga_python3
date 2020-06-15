def fun(x):
    if x == 2:
        return 1
    elif x < 2:
        return 0
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1


m, n = map(int, input().split())
s = 0
count = 0
for j in range(m, n + 1):
    if fun(j) == 1:
        # print(j)
        count += 1
        s += j

print(count, s)