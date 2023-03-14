t=int(input())
l=[]
for i in range(t):
    x=int(input())
    if(x==1 or x==2):
        l+=[0]
    else:
        y = x // 2
        if(x%2==0):
            z=y-1
            l+=[z]
        else:
            l+=[y]
for j in range(len(l)):
    print(l[j])

