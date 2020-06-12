# 阶梯电价、分支结构
c = eval(input())
if c <= 50:
    s = c * 0.53
else:
    s = 50 * 0.53 + (c - 50) * 0.58

print('%.2f' % s)
print('{:.2f}'.format(s))
