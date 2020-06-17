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

n = int(input())
for i in range(n):
    p = readPoint()
    print('Point = {}, type = {}, distance = {:.3f}'.format(p,type(p),distance(p)))