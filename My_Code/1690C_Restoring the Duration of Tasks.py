for j in range(int(input())):
    n=int(input())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    l=[]
    x=l2[0]-l1[0]
    l.append(x)
    for i in range(1,n):
        m=max(l2[i-1],l1[i])
        x=l2[i]-m
        l.append(x)
    for k in range(len(l)):
        print(l[k],end=' ')
    print()