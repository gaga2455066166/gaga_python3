from functools import cmp_to_key

def cmpkey2(x,y):
    if x[1]>y[1]:
        return 1
    elif x[1]<y[1]:
        return -1
    elif x[0]>y[0]:
        return -1
    elif x[0]<y[0]:
        return 1
    return 0

word2 = ""
text = ""
while True:
    s = input()
    if s == '!!!!!':
        break
    text += ' '
    text += s
    for ch in '!.,:*?':
        word2 = word2.replace(ch, ' ')
    word2 += s + '\n'
text = text.lower()
for ch in '!.,:*?':
    text = text.replace(ch,' ')
cnt = {}
for word in text.split():
    cnt[word] = cnt.get(word,0)+1 #去重
items = list(cnt.items()) #返回值是一个个元组
items.sort(key=cmp_to_key(cmpkey2),reverse=True)
print(len(items))
for i in range(10):
    if i>=len(items):
        break
    key,val = items[i]
    print("{}={}".format(key,val))