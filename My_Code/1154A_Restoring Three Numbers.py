x1,x2,x3,x4=list(map(int,input().split()))
l=[x1,x2,x3,x4]
l.sort()
l1=l[3]-l[2]
l2=l[3]-l[1]
l3=l[3]-l[0]
print(l1,l2,l3)
