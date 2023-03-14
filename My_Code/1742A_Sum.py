for i in range(int(input())):
    l=list(map(int,input().split()))
    maxi=max(l)
    x=l.index(maxi)
    l.pop(x)
    add=sum(l)
    if(add==maxi):
        print("YES")
    else:
        print("NO")