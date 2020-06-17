def sort(str):
    count = len(str)
    for i in range(0, count):
        for j in range(i, count):
            if str[i] > str[j]:
                t = str[i]
                str[i] = str[j]
                str[j] = t
                sort(str)
    return str
if __name__ == '__main__':
    a = list(map(int,input().split()))
    s = sort(a)
    for i in s:
        print(i,end=' ')






