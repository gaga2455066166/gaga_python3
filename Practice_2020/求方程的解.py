import math

a, b, c = map(int, input().split())  # 求ax2+bx+c=0方程的实根。a,b,c由键盘输入.

d = (b ** 2) - (4 * a * c)

if a == 0:  # 解方程要考虑系数a等于零的情况
    if b != 0:
        print('{:.2f}'.format(-(c / b)))
    elif b == 0:
        print('No')



elif a != 0:
    if d > 0:
        x1 = ((-b + math.sqrt(d)) / (2 * a))
        x2 = ((-b - math.sqrt(d)) / (2 * a))
        if x1 > x2:
            print('%.2f' % (x1), end=' ')
            print('%.2f' % (x2))
        elif x1 < x2:
            print('%.2f' % (x2), end=' ')
            print('%.2f' % (x1))
    elif d == 0:
        print('{:.2f}'.format((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)))
    elif d < 0:
        print('No')
