for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    maxi=max(l)
    mini=min(l)
    x=l.count(maxi)
    y=l.count(mini)
    if(x>y):
        print(l.index(mini)+1)
    else:
        print(l.index(maxi)+1)