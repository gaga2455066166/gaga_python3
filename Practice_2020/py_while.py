# # # # # print("打印10遍\n" * 10)
# # # # #
# # # # # i = 0
# # # # #
# # # # # while i < 5:
# # # # #     print("i = %d" % i)
# # # # #     i = i + 1
# # # # #
# # # #
# # # # a = 0
# # # # s = 0
# # # # while a <= 100:
# # # #     s = s + a
# # # #     a += 1
# # # # print("s = %d" % s)
# # #
# # # a = 0
# # # s = 0
# # # while a <= 100:
# # #     if a % 2 == 0:
# # #         s = s + a
# # #     a = a + 1
# # # print("s = %d" % s)
# #
# # i = 0
# # while i <= 100:
# #     if i == 5:
# #         i = i + 1
# #         continue
# #         # break
# #     print(i)
# #     i = i + 1
# i = 0
# j = 0
# while i < 5:
#     j = 0
#     while j <= i:
#         print(" * ", end="")
#         j = j + 1
#     print()
#     i = i + 1
i = 1

while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d\t" % (j, i, i * j), end="")
        j = j + 1
    print()
    i = i + 1
