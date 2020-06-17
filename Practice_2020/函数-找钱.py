n =  int(input())


def giveChange(param):
    m10=param//10
    m5=(param%10)//5
    m1=(param%10)%5
    print("{} = {}*10 + {}*5 + {}*1".format(param,m10,m5,m1))


for i in range(n):
    giveChange(int(input()))