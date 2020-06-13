# 阶梯电价、分支结构
c = eval(input())
if c < 0:
    s = -1
elif c <= 50:
    s = c * 0.53
else:
    s = 50 * 0.53 + (c - 50) * 0.58
if s < 0:
    print('Invalid Value！')
else:
    print('%.2f' % s)
    print('{:.2f}'.format(s))
