a = input()
n = 0
ans = 0
backup = a
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
    elif b[i+1] == ',' or b[i+1] == ']':
        if n%2==0:
            ans += int(nums[j]) * n * -1
        else:
            ans += int(nums[j]) * n
        j += 1
print(ans)
