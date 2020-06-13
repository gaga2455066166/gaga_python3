# 输出全排列，p88，例题6-32
# # ['a', 'D', 'b', 'f', 'd']
# c = eval(input())
# print(sorted(c))
# d = [s.lower() for s in c if isinstance(s, str) == True]
# print(sorted(d))


####################################
# 输入样例：
# 3
# 输出样例：
# 123
# 132
# 213
# 231
# 312
# 321
from itertools import permutations

n = int(input())
a = [str(i) for i in range(1, n + 1)]
# print(a)
s = ""
s = s.join(a)
# print(s)
for i in permutations(s, n):
    # print(i)
    print("".join(i))
