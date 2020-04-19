n = eval(input())
j = 0
list_student = [[] for i in range(n)]
max_score = 0
while j < n:
    str_student = input().split()
    list_student[j].append(str_student[0])
    list_student[j].append(str_student[1])
    sum_score = int(int((str_student[2])) + int((str_student[3])) + int((str_student[4])))
    list_student[j].append(sum_score)
    if sum_score > max_score:
        max_score = sum_score
    j += 1
for student in list_student:
    if student[2] == max_score:
        print(student[1] + ' ' + student[0], end=' ')
        print(student[2])

