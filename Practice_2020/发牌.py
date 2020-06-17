import random


def create():
    ls = []
    for i0 in range(4):
        for j in range(13):
            a = suit[i0] + d[j]
            ls.append(a)
    return ls


def shufflecard(pokers):
    random.shuffle(pokers)
    return pokers


def deal(pokers, n1):
    r = list()
    pos = n1 - 1
    for i1 in range(5):
        r.append(pokers[pos])
        pos += 4
    print("第{}个玩家拿到的牌是：{},{},{},{},{}".format(n1, r[0], r[1], r[2], r[3], r[4]))


suit = ['♥', '♠', '♦', '♣']
d = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
n = int(input())
random.seed(n)
poker = create()
poker = shufflecard(poker)
for i in range(52):
    print('%-4s' % poker[i], end='  ')
    if i % 13 == 12:
        print()
for i in range(1, 5):
    deal(poker, i)
