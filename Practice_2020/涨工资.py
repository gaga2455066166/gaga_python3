s = input()
ls = []
ls = s.split()
cnt = 0
for i in ls:
    i = float(i)
    if i <= 5000 and cnt == 1:
        if i - int(i) > 0:
            print(" {:.2f}".format(i * 1.5), end="")
        else :
            print(" {:.1f}".format(i*1.5),end="")
    elif i > 5000 and cnt == 1:
        print(" {:d}".format(int(i)),end="")
    if cnt == 0:
        if i <= 5000:
            if i - int(i) > 0:
                print("{:.2f}".format(i * 1.5), end="")
                cnt = 1
            else:
                print("{:.1f}".format(i * 1.5), end="")
                cnt = 1
        else:
            print("{:d}".format(int(i)), end="")
            cnt = 1