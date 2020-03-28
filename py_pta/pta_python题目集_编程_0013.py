str_str = input().split()
# print(str_str)
str_ints = list(map(int, list(str_str)))
str_ints.sort()
i = len(str_ints)-1
# print(i)
while i != 0:
    print("%d->" % str_ints[i], end='')
    i = i - 1
print(str_ints[0])
