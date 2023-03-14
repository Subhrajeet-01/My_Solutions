
for i in range(int(input())):
    n=int(input())
    s=str(input())
    l = []
    pivot=''
    bit=0
    for m in range(n):
        if s[m] != pivot:
            pivot=s[m]
            if s[m] in l:
                bit=1
            else:
                l.append(s[m])
    if bit == 1:
        print("NO")
    else:
        print("YES")
