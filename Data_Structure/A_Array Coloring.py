for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if arr[i]%2 == 1:
            count += 1
    if count % 2 ==1:
        print("NO")
    else:
        print("YES")




