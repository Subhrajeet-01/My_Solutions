L=[]
x = int(input())
for i in range(x):
    input()
    input()
    n, k = map(int,input().split())
    l = list(map(int,input().split()))
    for j in range(k):
        a, b = map(int,input().split())
        if(a in l and b in l[l.index(a)::]):
            L+=["YES"]
        else:
            L+=["NO"]
    if(i==x-1):
        for m in range(len(L)):
            print(L[m], sep=' ')



