# 根据层数的不同选择不同的前进路线
def luxian(i):
    if i % 2 != 0:
        a = [[0, -1], [1, 0], [0, 1]]  # 左，下，右
    else:
        a = [[0, 1], [-1, 0], [0, -1]]  # 右，上，左
    return a


def zhixin(x):
    global num, begx, begy
    num += 1
    begx += FX[x][0]
    begy += FX[x][1]
    a[begx][begy] = num


n = int(input())  # 不管n是偶数还是奇数都能够实现
num = 1  # 进行螺旋的值
a = [[0] * n for i in range(n)]  # 产生n阶 数组

begy = int(n / 2)

if n % 2 == 0:  # 判断开始进行的位置，n不同
    begx = begy - 1
else:
    begx = begy

a[begx][begy] = num

for i in range(1, n):  # 产生螺旋
    FX = luxian(i)
    zhixin(0)
    for j in range(i):
        zhixin(1)
    for j in range(i):
        zhixin(2)

for i in range(n):  # 输出
    for j in range(n):
        if j != n - 1:
            print(str(a[i][j]).ljust(4), end="")
        else:
            print(a[i][j], end="")

    print()
