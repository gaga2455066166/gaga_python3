str  = input()
c1 = str[0]
c2 = str[1]
c3 = str[2]
str2 = str[3:]
l = str2.__len__()
print(c1,end='')
for i in range(l):
    print(c2,end='')
print(c1)

print(c3,end='')
print(str2,end='')
print(c3)

print(c1,end='')
for i in range(l):
    print(c2,end='')
print(c1)