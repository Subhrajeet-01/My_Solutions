for i in range(int(input())):
    n=int(input())
    print(2)
    x,y=n,n-1
    for j in range(1,n):
        print(x,y)
        x,y=(x+y+1)//2,y-1

