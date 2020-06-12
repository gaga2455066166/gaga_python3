# 计算序列 2/1+3/2+5/3+8/5+... 的前N项之和
# 注意该序列从第2项起，每一项的分子是前一项分子与分母的和，分母是前一项的分子。
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
