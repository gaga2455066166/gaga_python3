n = int(input())
s = 0
lists = []
for i in range(1, n):
    if n % i == 0:
        s += i
        lists.append(i)
if s == n:
    print('{}='.format(s), end='')
    for i in range(len(lists)-1):
        print('{}+'.format(lists[i]), end='')
print(lists[len(lists)-1])