import random

computer = random.randint(-1, 1)
human = int(input("玩家请出拳\n-1\t=>\t剪刀\n 0\t=>\t石头\n 1\t=>\t布\n:"))
if computer == -1:
    print("电脑出拳：剪刀")
elif computer == 0:
    print("电脑出拳：石头")
else:
    print("电脑出拳：布")

if human == -1:
    print("你的出拳：剪刀")
elif human == 0:
    print("你的出拳：石头")
else:
    print("你的出拳：布")

if ((human == -1 and computer == 1)
        or (human == 0 and computer == -1)
        or (human == 1 and computer == 0)):
    print("玩家胜利了")
elif human == computer:
    print("平局")
else:
    print("电脑赢了哦")
