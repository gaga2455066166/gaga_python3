n = int(input())
a = 0
b = 1
while True:
    s = a
    a += b
    b = s
    if a > n:
        print(a)
        break