# # 双重循环
# # 读入一个m行n列的数据，矩阵中所有的偶数相加或者基数相加或者3的倍数相加
# # 或者求分数序列前n项和
# 3 5
# 3 4 5 6 7
# 4 5 6 7 8
# 6 7 8 9 2
m, n = map(int, input().split())  # 先输入一个数字代表需要输入几行，比如Q=4，那么就需要再输入4行数据
y = []
for i in range(m):
    x = list(map(int, input().rstrip().split()))
    if len(x) != n:
        print('输入错误')
        break
    y.append(x)

# 偶数相加：
sum_even = 0
for i1 in y:
    for j1 in i1:
        if j1 % 2 == 0:
            sum_even +=j1
print(sum_even)

# 基数相加：
sum_number = 0
for i2 in y:
    for j2 in i2:
        sum_number += j2
print(sum_number)

# 3的倍数求和：
sum_3 = 0
for i3 in y:
    for j3 in i3:
        if j3 %3 == 0:
            sum_3 += j3
print(sum_number)
