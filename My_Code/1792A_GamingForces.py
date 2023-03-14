for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    L=[]
    l1=[]
    for ele in l:
        x=l.count(ele)
        l1.append(x)
        if ele not in L:
            L.append(ele)
    if(len(l)!=len(L)):
        maxi1=max(l1)
        y=l1.count(1)
        r=maxi1+()
        print(r)
    else:
        print(n)

