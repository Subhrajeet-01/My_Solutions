n=int(input())
s=list(input())
r=['0','0','0','0','0','0','0','0','0','0']
for i in range(len(s)):
    if(s[i]=='L'):
        x=r.index('0')
        r[x]='1'
    elif(s[i]=='R'):
        r.reverse()
        x=r.index('0')
        r[x]='1'
        r.reverse()
    else:
        x=int(s[i])
        r[x]='0'
for k in range(len(r)):
    print(r[k],end='')