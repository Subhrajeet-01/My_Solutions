for j in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    r=l[-1]+l[-2]-l[0]-l[1]
    print(r)
