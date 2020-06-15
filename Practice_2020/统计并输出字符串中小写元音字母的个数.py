import sys
str = input()
vowel=['a','e','i','o','u']
sum=0
for i in str:
    if i in vowel:
        sum+=1
print(sum)