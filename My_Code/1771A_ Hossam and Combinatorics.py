for i in range(int(input())):
    n =int(input())
    l=list(map(int,input().split()))
    a=l.count(max(l))
    b=l.count(min(l))
    if(max(l)==min(l)):
        print(a*(b-1))
    else:
        print(a*b*2)