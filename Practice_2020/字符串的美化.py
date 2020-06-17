strs = input()
new_strs = ''
for i in strs:
    if not (i.isdigit() or i == '-'):
        new_strs += i
strs_list = new_strs.split()
for i in strs_list:
    if i[0] == '@' or i[0] == '#':
        strs_list.remove(i)
for i in range(len(strs_list)):
    if strs_list[i].endswith('...'):
        strs_list[i] = strs_list[i].rstrip('...')

for i in range(len(strs_list)-1):
    print(strs_list[i], end=' ')
print(strs_list[len(strs_list)-1])
