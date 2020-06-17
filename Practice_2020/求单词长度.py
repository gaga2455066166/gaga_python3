n = int(input())
ls = []
for i in range(n):
    s = input()
    ls.append(s)
ls.sort(key=lambda x:len(x),reverse=False)
for e in ls:
    print("({}, '{}')".format(len(e),e))