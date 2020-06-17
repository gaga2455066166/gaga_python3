str = input()
x = int(input())
y = int(input())
l = str.__len__()
if x<1 or x>l or y<x or y>l:
    print('没子串！')
else:
    print(str[x-1:y])