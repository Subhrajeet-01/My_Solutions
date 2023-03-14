s=input()
r=''
i=0
while(i<(len(s))):
    if s[i]=='-':
        if s[i]+s[i+1]=='--':
            r+='2'
            i+=2
        else:
            r+='1'
            i+=2
    else:
        r+='0'
        i+=1

print(r)