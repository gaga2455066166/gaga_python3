line=input()
c,blank,d,other=0,0,0,0
for e in line:
    if e.isdigit():
        d+=1
    elif e.isalpha():
        c+=1
    elif e.isspace():
        blank+=1
    else:
        other+=1
print("%d %d %d %d"%(c,blank,d,other))