import math
x=eval(input())
if math.fabs(x)>=300:
 y=-1
else:
 a=math.log10((math.fabs(x)+2.6))
 y=(x**3)/a
print("f({:.3f})={:.3f}".format(x,y))