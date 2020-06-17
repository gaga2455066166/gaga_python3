def demo1(x):
    if x > 1:
        y = 2 * x + 1
    elif x > -2:
        y = 3
    else:
        y = -2 * x - 1
    print("y={:.2f}".format(y))


try:
    x = eval(input())
    demo1(x)
except Exception as result:
    print("Input Error!")