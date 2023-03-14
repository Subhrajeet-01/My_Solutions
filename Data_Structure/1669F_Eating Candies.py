def main():
    for _ in range(int(input())):
        n = int(input())
        w = list(map(int,input().split()))
        a = 0
        b = n-1
        ans,pre,pos = 0,w[0],w[n-1]
        while a < b:
            if pre == pos:
                ans = (a+1) + (n-b)
            if pre <= pos:
                a += 1
                pre += w[a]
            else:
                b -= 1
                pos += w[b]
        print(ans)
main()


