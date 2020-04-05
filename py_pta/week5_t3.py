from functools import cmp_to_key


def cmp(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0


dic_word = {}
while True:
    str_word = input().lower()
    if str_word == '!!!!!':
        break
    elif len(str_word) == 0:
        continue
    else:
        str_word = str_word.replace('!', ' ')
        str_word = str_word.replace('.', ' ')
        str_word = str_word.replace(',', ' ')
        str_word = str_word.replace(':', ' ')
        str_word = str_word.replace('*', ' ')
        str_word = str_word.replace('?', ' ')
        # print(str_word.split(" "))
        list_word = str_word.split(" ")
        # print(list_word)
        for i in list_word:
            if not len(i.strip()):
                continue
            # print(len(i.strip()))
            if i in dic_word.keys():
                dic_word[i] += 1
            else:
                dic_word[i] = 1
# print(dic_word)
# print(sorted(dic_word.items(), key=lambda value1: value1[1]))
# print(sorted(dic_word.items(), key=lambda key0: key0[0]))
print(len(dic_word))
ls = sorted(dic_word.items(), key=cmp_to_key(cmp))
count = 0

for i in ls:
    if count < 10:
        print("%s=%s" % (i[0], i[1]))
    count += 1
