str_num = input().split(" ")
dic_word = {}
i = 1
while i < len(str_num):
    if str_num[i] in dic_word.keys():
        dic_word[str_num[i]] += 1
    else:
        dic_word[str_num[i]] = 1
    i += 1

max_num = max(dic_word, key=dic_word.get)
print(max_num, end=" ")
print(dic_word[max_num])
