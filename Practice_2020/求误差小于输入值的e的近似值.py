import math
e=float(input())
a=1
i=2
t=2
b=1/t
sum=1+1
while(a-b>=e):
    a=b
    sum=sum+a
    i=i+1
    t=t*i
    b=1/t
print('{:.6f}'.format(sum))