import math


def readPoint():
    s=input().split(',')
    for i in range(3):
        if s[i]=='':
            s[i]=0
        else:
            s[i]=int(s[i])
    b=(s[0],s[1],s[2])
    return b


def distance(p):
    d=math.sqrt(p[0]*p[0]+p[1]*p[1]+p[2]*p[2])
    return d


def ClassifyPoints(points, r):
    a=[]
    b=[]
    for i in points:
        if distance(i)<r:
            a.append(i)
        else:
            b.append(i)
    c=(a,b)
    return c


def printPointsTuple(pointsTuple, r):
    avg=0
    for i in pointsTuple[0]:
        avg=distance(i)+avg
    avg=avg/len(pointsTuple[0])
    print("distance < {}, avgDistance = {:.3f}, points = {}".format(r,avg,pointsTuple[0]))
    avg=0
    for i in pointsTuple[1]:
        avg=distance(i)+avg
    avg=avg/len(pointsTuple[1])
    print("distance >= {}, avgDistance = {:.3f}, points = {}".format(r,avg,pointsTuple[1]))



n = int(input())
r = int(input())
points = []
for i in range(n):
    p = readPoint()
    points.append(p)
    print('Point = {}, type = {}, distance = {:.3f}'.format(p,type(p),distance(p)))


pointsTuple = ClassifyPoints(points, r)
print("pointsTuple = {}".format(pointsTuple))




printPointsTuple(pointsTuple,r)
