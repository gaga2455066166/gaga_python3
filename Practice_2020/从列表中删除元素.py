n = int(input())
for i in range(n):
    a=input()
    b=input()
    x=a.replace(b+' ','')
    x=x.replace(b,'')
    print(x.strip())