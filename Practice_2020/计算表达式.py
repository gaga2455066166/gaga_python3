s=input()
exp=s.split()
if exp[1] in ['*','//','%']:
    exp=''.join(exp)
    print(exp,'=',eval(s),sep='')
else:
    print('Invalid operator')