for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    sum = 0
    L = []
    while(l.index(0)==0):
        l.pop(0)
    for j in range(len(l)):
        if(l[j]==0):
            L.append(j)
    for k in range(len(L)-1):
        if(L[k+1] - L[k]==1):
            sum = l[L[k+1]-2] + l[L[k]-2]
        else:
            sum = max(l[:L[k]]) + max(l[L[k]:])
    print(sum)


