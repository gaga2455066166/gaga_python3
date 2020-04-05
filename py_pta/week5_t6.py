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