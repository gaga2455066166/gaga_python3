s1 = list(input().split(","))
m,n = int(s1[0]),int(s1[1])
s=m*n
if m<n:
    m,n=n,m
i=m%n
m,n=n,i
while i!=0:
    i=m%n
    m,n=n,i
t=s/m
print("GCD:{:.0f}, LCM:{:.0f}".format(m,t))
