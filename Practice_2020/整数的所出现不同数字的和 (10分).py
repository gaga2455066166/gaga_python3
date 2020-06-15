# 本题目要求读入一个整数n，输出所出现不同数字的和。
# 例如：用户输入 123123123，其中所出现的不同数字为：1、2、3，这几个数字和为6。
# 用户输入 31415926，不同数字的和
str_num = input()
i = 0
dic_num = {}
sum_num = 0
while i < len(str_num):
    if not str_num[i] in dic_num.keys():
        dic_num[str_num[i]] = int(str_num[i])
    i += 1
for key in dic_num.keys():
    sum_num += dic_num[key]
print(sum_num)