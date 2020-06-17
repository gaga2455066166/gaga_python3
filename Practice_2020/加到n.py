n = int(input())
s = 0
last = 0
for i in range(n):
    s += i
    if s > n:
        last = i
        break
if last == 0:
    print('0=0')
elif last == 1:
    print('1==1')
elif last == 2:
    print('3=1+2')
elif last == 3:
    print('6=1+2+3')
else:
    print('{}=1+2+...+{}'.format(s, last))
