n=int(input())
list1=list(map(eval,input().split()))
list2=list(map(eval,input().split()))
list3_b=[]
list3_g=[]
for i in range(n):
    if list2[i]==1:
        list3_g.append(list1[i])
    else:
        list3_b.append(list1[i])
list3_b.sort()
list3_g.sort()
for i in list3_g:
    print(i,end=" ")
for i in range(len(list3_b)-1):
    print(list3_b[i], end=" ")
print(list3_b[-1])