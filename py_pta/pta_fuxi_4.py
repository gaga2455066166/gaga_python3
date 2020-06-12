# 输出全排列，p88，例题6-32
# ['a', 'D', 'b', 'f', 'd']
c = eval(input())
print(sorted(c))
d = [s.lower() for s in c if isinstance(s, str) == True]
print(sorted(d))
