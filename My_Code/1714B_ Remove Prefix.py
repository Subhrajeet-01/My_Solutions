for i in range(int(input())):
    n=int(input())
    l=input().split(" ")[::-1]
    s=set()
    for num in l:
        if num not in s:
            s.add(num)
        else:
            break
    print(n-len(s))
