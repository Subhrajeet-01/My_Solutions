for i in range(int(input())):
    w,h,n=map(int,input().split())
    s,k=1,1
    while(w%2==0):
        w/=2
        s*=2
    while(h%2==0):
        h/=2
        k*=2
    print("YES" if s*k >= n else "NO")