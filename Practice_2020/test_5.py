# 一个正整数如果它的所有因子之和恰好等于它本身，我们称它是“完整数”，
# 例如6的因子有1，2，3.恰好6=1+2+3。
# 则6是“完整数”。
# 输入两个整数m,n求出m--n之间的所有的完整数

def comp(x):
    total = 0
    for j in range(1, x):
        if x % j == 0:
            total = total + j
    if total == x:
        return True
    else:
        return False


str_m, str_n = input().split()
m = eval(str_m)
n = eval(str_n)
if m > n:
    temp = m
    m = n
    n = temp

for i in range(m, n + 1):
    if comp(i):
        print(i)
