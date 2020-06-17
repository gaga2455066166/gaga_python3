m, n = input().split()
m, n = int(m), int(n)
set3 = set()
set5 = set()
set7 = set()
res_set = set()
for i in range(m, n + 1):
    if (i % 3 == 0):
        set3.add(i)
    if (i % 5 == 0):
        set5.add(i)
    if (i % 7 == 0):
        set7.add(i)
res_set = set3 & set5 & set7
print(len(res_set))