for _ in range(int(input())):
    arr=['0']+list(input())
    z=10**9
    n = len(arr)
    for i in range(n-1,0,-1):
        if int(arr[i])>=5:
            arr[i-1] = str(int(arr[i-1])+1)
            z = i
    for i in range(n):
        if i>=z:
            arr[i] = '0'
    print(int(''.join(arr)))


"""
for _ in range(int(input())):
    n = int(input())
    l = list(str(n))
    ans = 0
    if l[0]>=5:
        ans = 10 * len(l)
    else:
        while l[0] >= 5:
            print()
"""




