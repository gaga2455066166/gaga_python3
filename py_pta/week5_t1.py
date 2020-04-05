# n = int(input())
# for i in range(n):
#     str_str = input()
#     str_str = str_str.replace(' ', '')
#     str_char = input()
#     str_str = str_str.replace(str_char, "")
#     print(str_str)
n = int(input())
for i in range(n):
    a = input()
    b = input()
    x = a.replace(b + ' ', '')
    x = x.replace(b, '')
    print(x.strip())
