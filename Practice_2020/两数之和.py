lst = list(map(int(input().split(" "))))
flag=0
for i in range(0,len(lst)):
    for j in range(i,len(lst)):
        if(lst[i]+lst[j]==n):
            print('{:d} {:d}'.format(i,j))
            flag=1
if(flag==0):
    print("no answer")