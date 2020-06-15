lst = list(map(int,input().split(",")))
d = {}
flag=0
for x in range(1,11):
    d[x]=0
for x in range(0,len(lst)):
    if not lst[x] in d:
        d[lst[x]] = 1
    else:
        d[lst[x]] = d[lst[x]] + 1
for i in range(6,11):
    if(d[i]==0):
        if(flag==0):
            print(i,end="")
            flag=1
        else:
            print(' {:d}'.format(i),end="")