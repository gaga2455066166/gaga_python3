m,n=input().split()
m=int(m)
n=int(n)


def isPrime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        for i in range(2,num):
            if  num % i == 0:
                return False
            if i == num - 1:
                return True



def PrimeSum(m, n):
    sum=0
    for i in range(m,n+1):
        if isPrime(i):
            sum=sum+i
    return sum



print(PrimeSum(m,n))