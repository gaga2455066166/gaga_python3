s = input()
m, n=input().split()
s=s[::-1]
for i in range(0,len(s)):
    if(n==s[i]):
        print("{:d} {:s}".format(len(s)-i-1,n))
for i in range(0, len(s)):
    if (m == s[i]):
        print("{:d} {:s}".format(len(s) - i - 1, m))