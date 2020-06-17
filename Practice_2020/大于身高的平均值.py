lst = list(map(int,input().split()))
sum=0
for i in range(0,len(lst)):
    sum=sum+lst[i]
aver=sum/len(lst)
for i in range(0,len(lst)):
    if(lst[i]>aver):
        print('{:d} '.format(lst[i]),end="")