a,b=map(int,input().split())
a=abs(a)
b=abs(b)
sum=0
while True:
    if a==0 and b==0:
        break
    sum=sum+((a%10)*(b%10))
    a=a//10
    b=b//10
print(sum)