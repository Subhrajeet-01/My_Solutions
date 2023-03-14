for i in range(int(input())):
    n=int(input())
    l = list(map(int,input().split()))
    ans=0
    for j in range(1,n-1):
        if(l[j-1]<l[j] and l[j]>l[j+1]):
            ans=1
            print("YES")
            print(j,j+1,j+2)
            break
    if(ans==0):
        print("NO")
