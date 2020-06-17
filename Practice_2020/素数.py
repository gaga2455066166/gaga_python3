a = int(input())
temp=False
if a<=1:
    print(f'{a} is not prime')
else:
    for i in range(2,a):
        if a%i==0:
            temp=True
            print(f'{a} is not prime')
            break
    if temp==False:
        print(f'{a} is prime')
