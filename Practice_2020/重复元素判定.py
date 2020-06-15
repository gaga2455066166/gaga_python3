n = int(input())
false = true = 0
for i in range(n):
    list = input()
    a_list = []
    a_list = list.split()
    if len(a_list) == len(set(a_list)):
        false += 1
    else:
        true += 1
print("True=%d, False=%d"%(true, false))