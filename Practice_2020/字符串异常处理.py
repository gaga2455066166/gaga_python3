try:
    s = input()
    x = input()
    print("{}".format(s[int(x)]))
except ValueError:
    print("下标要整数")
except IndexError:
    print("下标越界")