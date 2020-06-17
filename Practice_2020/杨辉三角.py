def printYanghui(n):
    numbers = []
    for line in range(n + 1):
        numbers += [[]]
        for i in range(n + 1):
            numbers[line] += [0]
    numbers[1][1] = 1
    for line in range(2, n + 1):
        for i in range(1, n + 1):
            numbers[line][i] = numbers[line - 1][i] + numbers[line - 1][i - 1]
    for line in range(1, n + 1):
        for space in range(n - line):
            print(" ", end='')
        for i in range(1, line + 1 ):
            print(numbers[line][i], end=" ")
        print()

n = int(input())
printYanghui(n)
