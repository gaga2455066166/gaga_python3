str_str = input()
sum_str = 0
str_str = str_str.replace('[', '')
str_str = str_str.replace(']', '')
str_str = str_str.replace('(', '')
str_str = str_str.replace(')', '')
int_str = eval(str_str)
for i in int_str:
    if isinstance(i, int):
        sum_str += i
print(sum_str)
