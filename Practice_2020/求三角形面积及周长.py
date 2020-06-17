import math

a = int(input())
b = int(input())
c = int(input())
s = (a + b + c) / 2
x = s * (s - a) * (s - b) * (s - c)
area = math.sqrt(x)
perimeter = a + b + c
print('area={:.2f};perimeter={:.2f}'.format(area, perimeter))