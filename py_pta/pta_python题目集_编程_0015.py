str_str = input()
after = len(str_str) - 1
i = 0
flag = True
# print(after)
# print((len(str_str) // 2))
while i < (len(str_str) // 2):
    if str_str[i] != str_str[after]:
        flag = False
    i = i + 1
    after = after - 1

if flag:
    print("yes")
else:
    print("no")
