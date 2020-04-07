if __name__ == '__main__':
    students = []
    subjects = set()
    message = input()
    while message != 'END':
        li = message.split(',')
        if len(li) == 2:
            dic = {'num': li[0], 'name': li[1]}
            students.append(dic)
        else:
            for i in students:
                if i['num'] == li[0]:
                    i[li[1]] = li[2]
                    subjects.add(li[1])
        message = input()
    print('学号,姓名,', end='')
    for i in subjects:
        print(i, end=',')
    print('平均分')
    for i in students:
        s = 0
        c = 0
        print('{},{}'.format(i['num'], i['name']), end=',')
        for j in subjects:
            print('' if i.get(j) is None else i.get(j), end=',')
            if i.get(j) is not None:
                c += 1
                s += int(i.get(j))
        print(s / c if c != 0 else 0)
