c = eval(input())
if c <= 50:
    s = c * 0.53
else:
    s = 50 * 0.53 + (c - 50) * 0.58

if c >= 0:
    print('cost='+'{:.2f}'.format(s))
else:
    print('Invalid Value！')