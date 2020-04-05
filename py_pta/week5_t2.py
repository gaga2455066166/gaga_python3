x = eval(input())
y = []
for i in range(0, len(x)):
    if x[i] not in y:
        y.append(x[i])
for j in range(0, len(y) - 1):
    print('%d' % y[j], end=' ')
print(y[-1])
