n= int(input())
count=0
for i in range(n):
    l=list(map(int,input().split()))
    maxi=max(l)
    mini=min(l)
    imax,imin=0,0
    for i in range(n):
        if l[i]==maxi :
            imax=i+1
            break
    for i in range(n):
        if l[i]==mini:
            imin=i+1
    if imax>imin:
        count= imax+n-imin-2
    else:
        count= imax+n-imin-1
    print(count)
    break

"""
    break
if(l.index(x)<l.index(y)):
    count=l.index(x)+((len(l)-1)-l.index(y))
else:

    if(l.count(x)>1):
        for k in range(l.count(x)):
            count-=1
    count = l.index(x) + ((len(l) - 1) - l.index(y))
print(count)
"""






"""
if(l[len(l)-1]==x):
        l[len(l)-1],l[len(l)-2]=l[len(l)-2],l[len(l)-1]
        count+=1
for j in range(len(l)):
    if(l[0]!=x):
        l[j],l[j+1]=l[j+1],l[j]
        count+=1
print(count)
    
    """