import random


def generatePoints(n):
    ls = []
    for i in range(n):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        b = (x, y)
        ls.append(b)
    return ls


def createPointDict(pList):
    d = {}
    for i in pList:
        if i in d.keys():
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d


def doQuery(pDict, p):
    if p in pDict.keys():
        print("{} = {}".format(p, pDict[p]))
    else:
        print("Not Found")


n = int(input())
random.seed(int(input()))
pList = generatePoints(n)
pDict = createPointDict(pList)
for i in range(3):#查询3次
    x, y = [int(e) for e in input().split(',')]
    doQuery(pDict, (x, y))