def prime(x):
    if x < 2:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False

    return True


str1, str2 = input().split()
m = int(str1)
n = int(str2)
prime_sum = 0
if m > n:
    temp = m
    m = n
    n = temp
for i in range(m, (n + 1)):
    if prime(i) == True:
        prime_sum = prime_sum + i

if prime_sum != 0:
    print(prime_sum)
else:
    print('not have prime!')
