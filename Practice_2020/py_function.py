def f1():
    i = 1

    while i <= 9:
        j = 1
        while j <= i:
            print("%d * %d = %d\t" % (j, i, i * j), end="")
            j = j + 1
        print()
        i = i + 1


if __name__ == '__main__':
    print("九九乘法表")
    f1()


def say_hello():
    print("你好啊")
    print("我很好哦")
