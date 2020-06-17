n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

min = [] #每列的最小值
for i in range(n):
    m = a[0][i]
    for j in range(n):
        if a[j][i] < m:
            m = a[j][i]
    min.append(m)

t = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == max(a[i]) and a[i][j] == min[j]:
            t += 1
print(t)