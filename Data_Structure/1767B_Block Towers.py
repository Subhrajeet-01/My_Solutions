for j in range(int(input())):
    n = int(input())
    l=list(map(int,input().split()))
    l1=sorted(l[1::])
    x=l[0]
    for i in l1:
        if i > x:
            if(x+i)%2 != 0:
                y = (x+i)//2
                x = y+1
            else:
                y = (x+i)//2
                x = y
    print(x)