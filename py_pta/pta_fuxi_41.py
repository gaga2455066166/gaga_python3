# 去除重复数字
# a = list(map(int, input().strip().split()))
# b = list(set(a))
# print(b)
x = eval(input())
numbers = []
while x > 0:
    c = x % 10
    x = x // 10
    numbers.append(c)
numbers = list(set(numbers))
print(numbers)
