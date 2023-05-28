for _ in range(int(input())):
    n ,q = map(int,input().split())
    a = list(map(int,input().split()))
    add=0
    for i in range(q):
        l,r,k = map(int,input().split())
        add=((r-l+1)*k)+sum(a[:(l-1)])+sum(a[r:])
        if(add%2!=0):
            print("YES")
        else:
            print("NO")