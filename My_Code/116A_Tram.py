n=int(input())
total,maxi=0,0
for _ in range(n):
    out,inp=map(int,input().split())
    total+=inp-out
    if(maxi<total):
        maxi = total
print(maxi)

"""
print(l)
for j in range(0,len(l)-1,2):
    t=l[j+1]-l[j+2]
   # t=int(l[j][1]-l[j+1][0])

    print(t)
w
print(l)

    """