a = float(input())
list = []
sum = a
list.append(a)
count = 1
if a >= 0:
    while 1:
        a = float(input())
        if a < 0:
            break
        list.append(a)
        sum = a + sum
        count = count + 1
    print("平均分={:.2f},不及格人数=".format(sum / count), end="")
    n = 0
    for i in list:
        if i < (sum / count):
            n = n + 1
    print("%d" % n)
else :
    print("没有学生")