import math
def prime(a):
    if a == 1:
        return 'No'
    for i in range(2, int(math.sqrt(a))+1):
        if a%i==0:
            return 'No'
    return 'Yes'

a = int(input())
for i in range(0, a):
    b=int(input())
    print(prime(b))