t=int(input())
for i in range(t):
    s=input()
    x=len(s)
    if(x%2==1):
        print("NO")
    else:
        s1=s[:int(x/2)]
        s2=s[int(x/2):]
        if(s1==s2):
            print("YES")
        else:
            print("NO")