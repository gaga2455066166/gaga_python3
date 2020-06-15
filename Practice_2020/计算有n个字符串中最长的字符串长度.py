n=int(input())
max = 0
maxstr = ""
for i in range(0, n):
    s =str(input().lstrip())
    if (max < len(s)):
        max = len(s)
        maxstr = s
print("length=%d"%len(maxstr))