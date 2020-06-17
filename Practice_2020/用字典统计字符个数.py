def Freq(line):
    dics = {}
    for i in line:
        if i not in dics.keys():
            dics[i] = 1
        else:
            dics[i] += 1
    lists = sorted(dics.items(), key=lambda item: item[0])
    print(len(lists))
    for i in lists:
        print('{} = {}'.format(i[0],i[1]))


line = input()
Freq(line)
