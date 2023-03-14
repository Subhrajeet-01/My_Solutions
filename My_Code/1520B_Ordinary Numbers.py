for i in range(int(input())):
    n=int(input())
    count=0
    j=1
    while j<=n:
        for k in range(1,10):
            if(k*j<=n):
                count+=1
            else:
                break
        j = j*10 + 1
    print(count)

















"""
    //if(n<=10):
        count=n
    elif(n<=100):
        n=n//11
        count=9+n
    elif(n<=1000):
        n=n//111
        count=18+n
    else:
        n=n//1111
        count=27+n
    print(count)

"""