money = int(input())
bonus = 0
if 0 < money <= 100000:
    bonus = bonus + money * 0.1
if 100000 < money <= 200000:
    bonus = 100000 * 0.1 + (money - 100000) * 0.075
if 200000 < money <= 400000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + (money - 200000) * 0.05
if 400000 < money <= 600000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (money - 400000) * 0.03
if 600000 < money <= 1000000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (money - 600000) * 0.015
if 1000000 < money:
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (money - 1000000) * 0.01
print("{}".format(bonus))