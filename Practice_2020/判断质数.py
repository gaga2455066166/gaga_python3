def isPrime(num):
    try:
        x = int(num)
    except ValueError:
        return False
    else:
        if x < 2:
            return False
        elif x == 2:
            return True
        else:
            for i in range(3, x):
                if x % i == 0:
                    return False
            return True


num = input()
if isPrime(num):
    print('yes')
else:
    print('no')
