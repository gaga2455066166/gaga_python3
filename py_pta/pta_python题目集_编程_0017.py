str_a, str_b, str_c = input().split()
a = eval(str_a)
b = eval(str_b)
c = eval(str_c)
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('yes')
        else:
            print('no')
    else:
        print('no')
else:
    print('no')
