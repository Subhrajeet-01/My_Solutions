for i in range(int(input())):
    L=[]
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    for j in range(len(l)-1):
        value=l[j+1]-l[j]
        L.append(value)
    print(min(L))

