for i in range(int(input())):
    n=int(input())
    l = list(map(int,input().split()))
    x=l[-1]
    count=0
    for j in range(len(l)-1,-1,-1):
        if l[j]>x:
            count+=1
        else:
            x = min(l[j],x)
    print(count)
