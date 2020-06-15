s = input()
if s[0] == '$':
    money = float(s[1:])
    print("{}{:.2f}".format('R',6*money))
else:
    money = float(s[1:])
    print("{}{:.2f}".format('$',money/6))