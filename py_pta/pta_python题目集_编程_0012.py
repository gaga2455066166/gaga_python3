str_str = input()
str_char = input()
str_int = eval(str_char)
total = 0
for a in str_str:
    if a == str_char:
        total = total+str_int

print(total)