def f1():
    i = 1

    while i <= 9:
        j = 1
        while j <= i:
            print("%d * %d = %d\t" % (j, i, i * j), end="")
            j = j + 1
        print()
        i = i + 1


