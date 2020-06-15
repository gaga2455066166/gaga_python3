c = eval(input())
a = 1  # 分母
b = 2  # 分子
s = 0
for i in range(0, c):
    s = s + b / a
    temp_b = b
    b = a + b
    a = temp_b
print('%.2f' % s)
print('{:.2f}'.format(s))