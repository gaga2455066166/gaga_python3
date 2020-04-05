import random


def random4(x):
    all_char = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

    index = len(all_char)-1
    code = ''
    for _ in range(x):
        num = random.randint(0, index)
        code += all_char[num]
    return code


str_k, str_n = input().split()
k = eval(str_k)
n = eval(str_n)
for i in range(k):
    print(random4(n))
