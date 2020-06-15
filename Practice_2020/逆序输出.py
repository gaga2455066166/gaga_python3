b = input().split()
a=b[::-1]
str=""
str2=""
for i in a:
   str+=" "+i
   str2+=i
print(str2)
print(b)
print(str[1:])