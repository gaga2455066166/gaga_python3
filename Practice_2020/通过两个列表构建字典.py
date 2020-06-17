list_1 = input().split()
list_2 = input().split()
result = {}
for i in range(len(list_1)):
    result[list_1[i]] = list_2[i]
list_1 = sorted(list_1)
new_result = {}
for i in range(len(list_1)):
    new_result[list_1[i]] = result.get(list_1[i])
res = []
lin = []
for k, v in new_result.items():
    lin.clear()
    lin.append(k)
    lin.append(v)
    res.append(tuple(lin))
print(res)