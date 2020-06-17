import random
def jc(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
n = int(input())
t = list()
t1 = set()
for i in range(1,n+1):
    t.append(str(i))
while True:
    if len(t1) >= jc(n):
        break
    random.shuffle(t)
    t1.add("".join(t))
s = sorted(t1)
for i in s:
    print(i)