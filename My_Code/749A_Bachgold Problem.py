n=int(input())
count=0
if(n%2==1):
    n=n-3
    d=n//2
    print(d+1)
    for i in range(d):
        print(2, end=' ')
    print(3, end=' ')
else:
    d=n//2
    print(d)
    for i in range(d):
        print(2, end=' ')

