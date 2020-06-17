# 返回值是菲波那切数列的第n项数字
def fib(i):
    x1 = 1
    x2 = 1
    x = 2
    j = 0
    if (i > 2):
        while (j < (i - 2)):
            x1 = x2
            x2 = x
            x = x1 + x2
            j += 1
        return x
    elif (i <= 2):
        return 1


# 用列表的形式返回范围[m,n]中斐波那契数列
def PrintFN(m, n):
    list = []
    for i in range(1, 50):
        if (fib(i) >= m and fib(i) <= n):
            list.append(fib(i))
    return list


m, n, i = input().split()
n = int(n)
m = int(m)
i = int(i)
b = fib(i)
print("fib({0}) = {1}".format(i, b))
fiblist = PrintFN(m, n)
print(len(fiblist))
