n = int(input())
t = n
l = [0] * (n + 1)
a = list(map(int, input().split()))
for i in a:
    if i != t:
        l[i] = 1
        print()
    else:
        print(i, end=" ")
        for x in range(t - 1, -1, -1):
            if l[x]:
                print(x, end=" ")
                l[x] = 0
            else:
                break
        print()
        t = x


