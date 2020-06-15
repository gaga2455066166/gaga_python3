def myprint(a,b):
    for i in range(0,a-b):
        print("{:<3d}".format(b),end='')
        b=b+a-i
    print(b)

a=eval(input())
for i in range(1,a):
    myprint(a,i)
print(a)