for i in range(int(input())):
    n=int(input())
    L=[]
    count=0
    s=input()
    l=list(s)
    for element in(l):
        if element not in L:
            L.append(element)
    count=len(L)*2
    if(len(L)<len(l)):
        x=len(l)-len(L)
        count+=x
    print(count)
