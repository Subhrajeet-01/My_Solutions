n=int(input())
l=[]
Sereja , Dima, i = 0, 0, 0
t=map(int,input().split())
l+=t
y=len(l)
a=True
while(y!=0):
    if(l[0]>=l[y-1]):
        x=l[0]
        l.pop(0)
    else:
        x=l[y-1]
        l.pop(y-1)
    if(a==True):
        Sereja+=x
        a=False
    else:
        Dima+=x
        a=True
    y-=1
print(Sereja,Dima)







