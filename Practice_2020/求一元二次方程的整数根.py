import math      #import 是用来函数调用的，math就是包括sqrt(开方)等的函数模块
a=1
b=6
c=5
if b**2-4*a*c>0:
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("{:.0f} {:.0f} ".format(min(x1,x2),max(x1,x2)))
elif b**2-4*a*c==0:
    x=(-b)/(2*a)
    print("{:.0f} {:.0f} ".format(x))
else:
    print("{} {} ".format("无根","无根"))