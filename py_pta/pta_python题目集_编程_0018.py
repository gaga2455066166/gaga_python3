import cmath
import math

x = float(input())
# print(math.log10(100))
if -1 < x < 1:
    print('f({:.3f})={:.3f}'.format(x, (2 - 2 * x) ** 0.5))
elif x >= 1:
    print('f({:.3f})={:.3f}'.format(x, ((math.cos(x) + math.pow(x, 2)) / (2.50 + abs(x + math.log(100,math.e))))))
else:
    print('f({:.3f})={:.3f}'.format(x, math.exp(x)))

