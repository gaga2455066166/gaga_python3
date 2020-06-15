s = input()
# 保留字符串中的所有的字母
t = ''.join([i for i in s if i.isalpha()])
result = ''.join([
    t[i] for i in range(len(t))
     if t[i].upper() not in t[:i].upper()
]) # 去除重复的字母
if len(result) > 9:
    print(result[:10])
else:
    print("not found")