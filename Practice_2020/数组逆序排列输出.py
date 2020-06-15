a=input().split()
l=len(a)
a=[int(x) for x in a]
a.sort()
a.reverse();
for i in a:
    l-=1
    print(i,end="")
    if l>0:
        print('->',end="")