for i in range(int(input())):
    v,x,y,z=map(int,input().split())
    max1=max(v,x)
    max2=max(y,z)
    min1=min(v,x)
    min2=min(y,z)
    mini1=min(max2,max1)
    mini2=max(min1,min2)
    if(mini1>mini2):
        print("YES")
    else:
        print("NO")