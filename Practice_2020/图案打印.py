n = eval(input())
for i in range(1, n + 1):
    flag_copy = False
    temp = 0
    for j in range(1, n + 1):
        if i == j:
            temp = j
            print('%4d' % j, end="")
            flag_copy = True
        elif flag_copy:
            print('%4d' % temp, end="")
        else:
            print('%4d' % j, end="")
    print()
