
import math
x=eval(input())
if math.fabs(x)==3:
    y=10
elif x<3:
    y=1.2
else:
    y = 2*x+1;
print("f({:.2f})={:.2f}".format(x,y))