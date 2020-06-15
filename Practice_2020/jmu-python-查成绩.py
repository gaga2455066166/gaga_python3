s = {}
while(True):
    try:
        m,n = input().split(":")
    except:
        break
    s[m] = n
m = input("请输入要查询的课程：\n")
try:
    print("{}".format(s[m]))
except:
    print("没有该门课程")