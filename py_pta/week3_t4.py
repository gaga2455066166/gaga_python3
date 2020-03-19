def is_num(x):
    if x == 0:
        return False
    temp = x
    x_is = 0
    while temp != 0:
        a = temp % 10
        temp = temp // 10
        x_is = x_is + a ** 5
    if x == x_is:
        return True
    else:
        return False


str_n = input()
n = int(str_n)
for i in range(10 ** n):
    if is_num(i):
        print(i)
