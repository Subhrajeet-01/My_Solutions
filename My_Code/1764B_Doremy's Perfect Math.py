t= int(input())
l=[]
x=1
y=2
count=[]
for i in range(t):
    n=int(input())
    s = list(map(int, input().split()))
    s.sort()
    #print(s)
    for j in range(len(s)):
        if(s[x]-s[x-1]!=s[j]):
            r=s[x]-s[x-1]
            s.append(r)
            s.sort()
            x+=1
        elif(s[y]-s[y-2]!=s[j]):
            u=s[y]-s[y-2]
            s.append(u)
            s.sort()
            y+=1
        else:
            s.sort()
    L=len(s)
    count.append(L)

print(count)
