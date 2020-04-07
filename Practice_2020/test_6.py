str_str = input()
count_max = 0

for i in set(str_str):
    if str_str.count(i) > count_max:
        count_max = str_str.count(i)
dic_number_of_letters = {}
for j in set(str_str):
    if str_str.count(j) == count_max:
        dic_number_of_letters[j] = count_max
dic_number_of_letters = sorted(dic_number_of_letters.items(), key=lambda letters: letters[0])

for letter in dic_number_of_letters:
    print("%s %s" % (letter[0], letter[1]))
