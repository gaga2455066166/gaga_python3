# 去除重复数字
# a = list(map(int, input().strip().split()))
# b = list(set(a))
# print(b)
x = input()
letter_list = list(x)
print(letter_list)
print(sorted(letter_list))
x = x.lower()
letter_list = list(x)
print(sorted(letter_list))