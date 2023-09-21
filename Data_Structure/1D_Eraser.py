for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    c=0
    j = 0
    while j<n:
        if s[j]=="B":
            c+=1
            j+=k
        else:
            j+=1
    print(c)