for i in range(int(input())):
    n = int(input())
    l=list(map(int,input().split()))
    L=[]
    while len(l)!=0:
        maxi = max(l)
        index = l.index(maxi)
        L += l[index:]
        del l[index:]
    for j in range(len(L)):
        print(L[j],end=' ')
    print()

