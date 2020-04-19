a = input()
x = eval(input())
n = 0
ans = 0
backup = a
dic_num = {}
a = a.replace('[', '')
a = a.replace(']', '')
nums = a.split(',')
b = backup
j = 0
for i in range(len(b)):
    if b[i] == '[':
        n += 1
    elif b[i] == ']':
        n -= 1
    elif b[i] == ',':
        continue
    elif b[i + 1] == ',' or b[i + 1] == ']':
        if n not in dic_num.keys():
            dic_num[n] = 1
        else:
            dic_num[n] += 1
        j += 1
print(dic_num[x])
