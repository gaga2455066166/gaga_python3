m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)


def fib(i):
    fi=[1,1]
    for j in range(100):
        fi.append(fi[-1]+fi[-2])
    return fi[i]


b=fib(i)
print("fib({0}) = {1}".format(i,b))


def PrintFN(m, n):
    count=0
    fi = [1, 1]
    i=0
    for j in range(100):
        if (fi[-1] + fi[-2])<m:
            i=j+3
        elif (fi[-1] + fi[-2])>n:
            break
        fi.append(fi[-1] + fi[-2])
    fi=fi[i:]
    return fi




fiblist=PrintFN(m,n)
print(len(fiblist))