t=int(input())
l=[]
for i in range(t):
    x,y=map(int,input().split())
    if(x>y):
        z = x-y
        d = z//10
        if z%10==0:
            l+=[d]
        else:
            l+=[d+1]
    elif(x<y):
        z = y-x
        d = z//10
        if z%10==0:
            l+=[d]
        else:
            l+=[d+1]
    else:
        l+=[0]
for j in range(len(l)):
    print(l[j])