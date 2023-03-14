for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    for j in range(k):
        A = min(a)
        B = max(b)
        if (B>A):
            a.append(B)
            a.remove(A)
            b.remove(B)
    print(sum(a))