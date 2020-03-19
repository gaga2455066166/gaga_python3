# s1=eval(input())
# s2=eval(input())
# list_dig=[]
# list_wor=[]
# dic={}
# for i in s1:
#     dic[i]=dic.get(i,0)+s1.get(i,0)
#     if type(i)==type(1):
#         list_dig.append(i)
#     elif type(i)==type('w'):
#         list_wor.append(i)
# for i in s2:
#     dic[i] = dic.get(i, 0) + s2.get(i, 0)
#     if type(i)==type(1):
#         list_dig.append(i)
#     elif type(i)==type('w'):
#         list_wor.append(i)
# list_dig.sort();list_wor.sort()
# list=list_dig+list_wor
# print("{",end="")
# cnt=0;length=len(dic)
# for i in list:
#     if i in dic:
#         cnt += 1
#         if type(i)==type(1):
#             print("{}:{}".format(i,dic[i]),end="")
#         else:
#             print('"{}":{}'.format(i,dic[i]),end="")
#         del dic[i]
#         if cnt!=length:
#             print(",",end="")
# print("}")
# a = {1: 23, 2: 34}
# b = {1: 1, 4: 34}
# c = a.copy()
# c.update(b)
# print(c)
# for num in range(1000, 10000):
# #     a = num // 1000
# #     b = (num % 1000) // 100
# #     c = (num % 100) // 10
# #     d = num % 10
# #     m = pow(a, 4) + pow(b, 4) + pow(c, 4) + pow(d, 4)
# #     if m == num:
# #         print(num)
