s1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s = input()
k = int(input())
for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        for j in range(26):
            if s1[j] == s[i]:
                print("{}".format(s1[(j + k) % 26]), end="")
    elif 'A' <= s[i] <= 'Z':
        for j in range(26):
            if s2[j] == s[i]:
                print("{}".format(s2[(j + k) % 26]), end="")
    else:
        print("{}".format(s[i]),end="")