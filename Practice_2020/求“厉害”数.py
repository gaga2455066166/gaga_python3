if __name__ == '__main__':
    n = int(input())
    power = [i ** 5 for i in range(10)]
    for i in range(1, 10 ** n):
        j = i
        s = 0
        while j != 0:
            s += power[j % 10]
            j //= 10
        if s == i:
            print(i)