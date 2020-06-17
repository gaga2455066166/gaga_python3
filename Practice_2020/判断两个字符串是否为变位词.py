def is_deformation(str1, str2):
    if str1 is None or str2 is None or len(str1) != len(str2):
        return False
    i, map = 0, [0]
    while i <= 256:
        map.append(0)
        i += 1
    for i in range(0, len(str1)):
        map[ord(str1[i])] += 1
    for i in range(0, len(str2)):
        if map[ord(str2[i])] == 0:
            return False
    return True
str1 = input()
str2 = input()
if is_deformation(str1,str2):
    print('yes')
else:
    print('no')