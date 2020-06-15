def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


s = int(input())
sums = 0
c = ''
for i in range(s):
    a = input()
    if is_number(a.strip()):
        sums += int(a)
    else:
        c = a
        break
if c == '':
    print("All OK")
    print("avg grade = {:.2f}".format(sums / s))
else:
    print("Error for data \"{}\"! Break".format(c))
print("Process Completed")
