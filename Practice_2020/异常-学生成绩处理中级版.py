n = int(input())
num = n
sum_grade = 0
flag = True
err_grade = ""
err_list = []
while n:
    try:
        err_grade = input()
        grade = int(err_grade)
        sum_grade += grade
        n = n-1
    except:
        flag = False
        err_list.append(err_grade)
if flag:
    print("All OK")
else:
    for grade in err_list:
        print("Error for data %s! Reinput" % grade)
print("avg grade = %.2f" % (sum_grade/num))