def r(x, y, z):
    return (y * y - 4 * x * z) ** 0.5


a, b, c = map(int, input().split())
if isinstance(r(a, b, c), complex):
    print('no real solution')
elif r(a, b, c) == 0:
    print('x={:.3f}'.format(-b / (2 * a)))
else:
    print('x1={:.3f}'.format((-b - r(a, b, c)) / (2 * a)))
    print('x2={:.3f}'.format((-b + r(a, b, c)) / (2 * a)))
