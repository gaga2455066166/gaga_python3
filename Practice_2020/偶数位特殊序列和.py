def fun(a,b):
   s=0
   x=0
   for i in range(0,b):
      x=x*10+a
      if(i==b-1):
        l=x
      s+=x
   return l;
m,n=input().split()
x=int(m)
y=int(n)
s=0
for i in range(2,y+1,2):
    s+=fun(x,i)
print(s)