def giveChange(num):
    x = int(num / 10)
    m = num % 10
    y = int(m / 5)
    m = m % 5
    z = int(m / 1)
    print("{} = {}*10 + {}*5 + {}*1".format(num, x, y, z))
