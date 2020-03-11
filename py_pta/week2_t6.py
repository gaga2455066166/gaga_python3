a = int(input())
b = int(input())
c = int(input())
s = (a + b + c) * 1.0 / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("area=%.2f;perimeter=%.2f" % (area,a+b+c))

