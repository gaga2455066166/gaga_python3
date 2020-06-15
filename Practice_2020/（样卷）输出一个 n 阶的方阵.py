a=input().split()
num=int(a[0])

for i in range(num):
    print(a[1],end=' ')
print('')

for i in range(1,num-1):
    print(a[1],end=' ')
    for i in range(1,num-1):
        print(str(int(a[1])-1),end=' ')
    print(a[1],end=' ')
    print('')

for i in range(num):
    print(a[1],end=' ')
print('')