m=input()
i=m[0]
if(i=='$'):
   print('￥',end='')
   x=int(m[1:])
   print('{:.2f}'.format(x*7))
elif(i=='￥'):
     print('$',end='')
     l=int(m[1:])
     print('{:.2f}'.format(l/7))
else:
     print('输入格式错误')
