for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=sorted(l)
    if(n==1):
        print(-1)
    else:
        for j in range(len(l) - 1):
            if l[j] == l1[j]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
        if l1[-1] == l[-1]:
            l1[-1], l1[-2] = l1[-2], l1[-1]
        for k in l1:
            print(k, end=' ')
        print()
