# 输入格式:
# 在一行中输入列表或元组
#
# 输出格式:
# 在一行中输出数字的和
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# [11,2,[3,7],(68,-1),"123",9]
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 99
str_str = input()
sum_str = 0
str_str = str_str.replace('[', '')
str_str = str_str.replace(']', '')
str_str = str_str.replace('(', '')
str_str = str_str.replace(')', '')
int_str = eval(str_str)
for i in int_str:
    if isinstance(i, int):
        sum_str += i
print(sum_str)