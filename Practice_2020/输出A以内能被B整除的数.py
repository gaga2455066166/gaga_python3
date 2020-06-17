b,a = map(int,input().split())
x = 0
i = 0
list =[]
if a>b:
    print('None.')
else:
    for i in range(a, b+1,a):
        x+=1
        list.append(i)
    l = list.__len__()
    if x==0:
        print('None.')
    else:
        for i in range(l-1):
            print(list[i],end=' ')
        print(list[l-1])