def judge(m):
    sum = 1
    for i in range(1, m + 1):
        sum *= i
    return sum


def cal(n, m):
    now_n = judge(n)
    now_m = judge(m)
    now_n_m = judge(n - m)
    return now_n / (now_m * now_n_m)


m, n = list(input().split())
flag = True
flag2 = True
try:
    m, n = int(m), int(n)
except:
    print("请输入数值")
    flag = False
if flag:
    if m > 0 and n > 0:
        print("result={:.2f}".format(cal(n, m)))
    else:
        print("不能负数")