import math
x=int(input())
k=list(hex(x))
del k[0]
del k[0]
lenn=len(k)
for i in range(lenn):
    if k[i].isalpha():
        k[i]=k[i].upper()
k=''.join(k)
print('{}D is {}H'.format(x,k))