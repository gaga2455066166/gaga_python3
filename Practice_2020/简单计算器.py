n = int(input())
for i in range(n):
    try:
        x = eval(input(''))
    except NameError:
        print('NameError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except SyntaxError:
        print('SyntaxError')
    else:
        print('{:.2f}'.format(x))
