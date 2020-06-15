import math
x = float(input())
if math.fabs(x) < 1:
    result=math.sqrt(2-2*x)
    print('f({:.3f})={:.3f}'.format(x,result))
elif x >= 1:
    a=2.5+(x+math.log(100))
    result=(math.cos(x)+math.pow(x,2))/a
    print('f({:.3f})={:.3f}'.format(x, result))
else:
    result=math.exp(x)
    print('f({:.3f})={:.3f}'.format(x, result))