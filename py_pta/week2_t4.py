str1, str2, str3 = input().split(' ')

money = float(str1)
year = int(str2)
rate = float(str3)
# interest=money×(1+rate)^year−money
interest = money * ((1 + rate) ** year) - money
print("interest=%.2f" % interest)
# print("interest={}".format(interest))
