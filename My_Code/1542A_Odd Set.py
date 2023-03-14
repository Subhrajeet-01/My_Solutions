for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    for j in l:
        count+=j%2
    if(count==n):
        print("YES")
    else:
        print("NO")