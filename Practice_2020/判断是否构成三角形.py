s = list(input().split())
x,y,z = int(s[0]),int(s[1]),int(s[2])

if z > x and z > y and x+y > z and z-y < x and z-x < y:
    print("yes")
elif x > z and x >y and z + y > x and x-y < z and x-z < y:
    print("yes")
elif y > z and y >y and x+z > y and y-z < x and y-x < z:
    print("yes")
else :
    print("no")