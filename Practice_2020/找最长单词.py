s = input()
s1 = ''
for i in range(len(s) - 1):
    s1 += s[i]
lt = s1.split()
ln = list()
for i in lt:
    ln.append(len(i))

m = 0
for i in range(len(ln)):
    if ln[i] > ln[m]:
        m = i
print(lt[m])