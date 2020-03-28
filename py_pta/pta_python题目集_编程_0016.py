a = float(input())
if a < 3:
    print("f({:.2f})={:.2f}".format(a, 1.20))
elif a == 3:
    print("f({:.2f})={:.2f}".format(a, 10))
else:
    print("f({:.2f})={:.2f}".format(a, 2 * a + 1))
