s1=input()
t1=input()
s=list(s1)
t=list(t1)
count=0
if(len(s)!=len(t)):
    print('NO')
else:
    for i in range(len(t)):
        if(t[i]==s[(len(s)-1)-i]):
            count+=1

    if(count==len(s)):
        print('YES')
    else:
        print('NO')