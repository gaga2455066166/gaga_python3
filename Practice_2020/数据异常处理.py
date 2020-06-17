def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


s = int(input())
if s==0:
    print('除0错误，n不能等0')
else:
    sums = 0
    c = ''
    flag = True
    for i in range(s):
        if not flag:
            break
        a = input()
        a.strip()
        if is_number(a):
            sums += float(a)
        else:
            flag = False
            c = a
    if flag:
        print("正确")
        print("avg={:.2f}".format(sums / s))
    else:
        print("数值错误")
print("程序结束")
