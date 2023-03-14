for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    res = "YES"
    big_even = 0
    big_odd = 0
    for elem in l:
        if elem % 2 == 0:
            if elem > big_even:
                big_even = elem
            elif elem < big_even:
                res = "NO"
                break
        elif elem % 2 == 1:
            if elem > big_odd:
                big_odd = elem
            elif elem < big_odd:
                res = "NO"
                break
    print(res)




"""
    if(len(s)!=1):
        for j in range(n - 1):
            if (l[j] > l[j + 1]):
                if ((l[j] + l[j + 1]) % 2 != 0):
                    l[j], l[j + 1] = l[j + 1], l[j]
                    if (l == L):
                        print("Yes")
                else:
                    print("No")
                    break
    else:
        print("Yes")
"""