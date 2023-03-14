for i in range (int(input())):
    n=int(input())
    l=[]
    for j in range(1,n+1):
        s=2**j
        l.append(s)
    a=sum(l[:(n//2-1)])
    b=sum(l[n//2-1: n-1])
    r=abs((a+2**n)-b)
    print(r)