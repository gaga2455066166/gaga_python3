m = float(input())
if m % 1 == 0:
    m = int(m)
n = int(input())
print("{} {} {} {} {}".format(m + n, m * n, m ** n, m % n, max(m, n)))
