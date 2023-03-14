x1,x2,x3=map(int,input().split())
l=[x1,x2,x3]
l.sort()
d1=l[2]-l[1]
d2=l[1]-l[0]
print(d1+d2)

