import cmath
import math

str_a, str_b, str_c = input().split(',')
a = float(str_a)
b = float(str_b)
c = float(str_c)

delta = b * b - 4 * a * c
if delta == 0:
    x1 = -b / (2 * a)
    print('x1=x2=%.1f' % x1)
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('x1=%.2f' % x1)
    print('x2=%.2f' % x2)
else:
    c1 = (-b + cmath.sqrt(delta)) / (2 * a)
    c2 = (-b - cmath.sqrt(delta)) / (2 * a)
    # “{0.real:.3f}{0.imag:+.3f}j”.format(4.2344+5.3445j)
    print('C1={0.real:.3f}{0.imag:+.3f}j'.format(c1))
    print('C2={0.real:.3f}{0.imag:+.3f}j'.format(c2))
