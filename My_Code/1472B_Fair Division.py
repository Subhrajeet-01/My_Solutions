t=int(input())
l=[]
add=0
for i in range(t):
    n=int(input())
    x=map(int,input().split())
    l+=x
    x1=l.count(1)
    x2=l.count(2)
    add=sum(l)
    if(x1==0 and x2%2!=0):
        print("NO")
    elif(x2==0 and x1%2!=0):
        print("NO")
    else:
        if(add%2==0):
            print("YES")
        else:
            print("NO")
    l=[]
    add=0




