w,x,y,z=map(int,input().split())
l=[w,x,y,z]
W=l.count(w)
X=l.count(x)
Y=l.count(y)
Z=l.count(z)
L=[W,X,Y,Z]
L.sort()
if(L[0]==4):
    print(3)
elif(L[0]==2):
    print(2)
elif(L[0]==1 and L[1]==3):
    print(2)
elif(L[0]==1 and L[2]==2):
    print(1)
else:
    print(0)


