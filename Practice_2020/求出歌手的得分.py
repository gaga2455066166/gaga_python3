n = int(input())
num = [int(n) for n in input().split()]
num.sort()#sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
for i in range(0,4):
    num1 = num.pop(-1)
    num.reverse()
nsum = 0
for j in range(len(num)):
    nsum += num[j]
avg = nsum / len(num)
print("aver={:.2f}".format(avg))