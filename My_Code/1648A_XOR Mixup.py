for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=True
    for j in range(len(l)):
        if(l[j]%2==1):
            print(l[j])
            a=False
            break
    if (a==True):
        print(l[0])
