a,b,c=input().split()
a,b,c=eval(a),eval(b),eval(c)
d=a*1.0* pow(1+c,b)-a
print("interest=%.2f"%d)