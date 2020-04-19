from itertools import permutations
n = int(input())
a = [str(i) for i in range(1,n+1)]
s = ""
s = s.join(a)
for i in permutations(s,n):
    print("".join(i))
