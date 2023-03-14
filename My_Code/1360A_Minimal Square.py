t=int(input())
l=[]
for i in range(t):
    x,y=map(int,input().split())
    mini=min(x,y)
    maxi=max(x,y)
    mini *= 2
    if((mini**2)>=(maxi**2)):
        l+=[(mini**2)]
    else:
        l+=[(maxi**2)]
for j in range(len(l)):
    print(l[j])