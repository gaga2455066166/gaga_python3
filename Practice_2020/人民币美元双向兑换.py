def change(x):
    if x[0] == '$':
        s1 = int(x[1:])
        print('{}美元 = {:.2f}人民币'.format(s1, s1 * 6.709))
    else:
        s1 = int(x[1:])
        print('{}人民币 = {:.2f}美元'.format(s1, s1 / 6.709))


x = input()

change(x)
