def factor(x):
    sum_x = 1
    for i in range(1, (x + 1)):
        sum_x = sum_x * i
    return sum_x


n = int(input())
sum_n = 0
for j in range(1,(n+1)):
    sum_n = sum_n + factor(j)
print(sum_n)