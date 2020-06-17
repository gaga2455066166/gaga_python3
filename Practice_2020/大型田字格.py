def jia0():
    print('+ - - - - +', end='')


def jia():
    print(' - - - - +', end='')


def shu0():
    print('|         |', end='')


def shu():
    print('         |', end='')


n = int(input())
x = 1 + 5 * n
for i in range(x):
    if i % 5 == 0:
        for j in range(n):
            if j == 0:
                jia0()
            else:
                jia()
    else:
        for j in range(n):
            if j == 0:
                shu0()
            else:
                shu()
    print()
