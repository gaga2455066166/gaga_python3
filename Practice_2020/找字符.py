s = input()
a = str(input())
b = True;
count = 0
for e in s:
    count = count + 1
    if e == a:
        print("index=%d" % count)
        b = False
        break
if b == True:
    print("can't find letter {}".format(a))