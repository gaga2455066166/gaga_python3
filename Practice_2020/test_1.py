i = 0
s = 0
t = int(input())
try:
    while i < t:
        n = int(input("".format()))
        if n > 100:
            print("illegal input")
            break
        s += n
        i = i + 1
        a = s / i
        print("{:.2f}".format(a))
except:
    print("illegal input")
