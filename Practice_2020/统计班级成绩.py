m = input()
students = {}
name = ''
score = ''
sum_score = 0
flag_score = False
for i in m:
    if i.isalpha():
        if flag_score:
            students[name] = float(score)
            sum_score += float(score)
            flag_score = False
            name = ''
            score = ''
        name = name + i
    else:
        score = score + i
        flag_score = True
students[name] = float(score)
sum_score += float(score)
max_score = max(zip(students.values(), students.keys()))
min_score = min(zip(students.values(), students.keys()))
print('{:.1f}'.format(sum_score / len(students)))
print('{} {:.1f}'.format(max_score[1], max_score[0]))
print('{} {:.1f}'.format(min_score[1], min_score[0]))
# print('{} {:.1f}'.format())
# print(len(students))
# print(students)
