for i in range (int(input())):
    n,m=map(int,input().split())
    l = list(map(int,input().split()))
    L=set()
    time,index=0,n-1
    t = [-1]*n
    for i in l:
        time+=1
        if i not in L and index>=0:
            t[index]=time
            index-=1
            L.add(i)
    for j in t:
        print(j,end=' ')
    print()