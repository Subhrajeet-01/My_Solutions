t=int(input())
l=[]
for i in range(t):
    x,y=map(int,input().split())
    if(x>=y):
        if(x%y!=0):
            r=x%y
            move=y-r
            l+=[move]
        else:
            l+=[0]
    else:
        move=y-x
        l+=[move]
for j in range(len(l)):
    print(l[j])