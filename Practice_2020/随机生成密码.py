import string
import random
x=int(input())
n=int(input())
m=int(input())
random.seed(x)
chars = string.ascii_letters+string.digits
new_chars=' '.join(chars)
ll=new_chars.split()
num=0
while num< n:
    num2 = 0
    while num2<m:
        num2+=1
        num3 = random.randint(0,61)
        print(ll[num3],end='')
    print()
    num+=1
