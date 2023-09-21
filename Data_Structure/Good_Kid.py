for _ in range(int(input())):
    length = int(input())
    arr = list(map(int,input().split()))
    mini = min(arr)
    arr.append(mini+1)
    arr.remove(mini)
    res = 1
    for i in range(length):
        res *= arr[i]
    print(res)
