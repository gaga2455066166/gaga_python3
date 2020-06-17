s = input()
count = 0
cnt = 0
for i in s:
    if i <= '9' and i >= '0':
        count += 1
    elif i <= 'z' and i >= 'a':
        cnt += 1
print("共有%d个数字，%d个小写字符" % (count,cnt))