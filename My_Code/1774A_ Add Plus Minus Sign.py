test=int(input())
for i in range(test):
    n =int (input())
    s=input()
    x=int(s[0])
    str=' '
    for i in range(1,n):
        if s[i]=='1':
            if x==0:
                x+=1
                str+=('+')
            elif x==1:
                x-=1
                str+=('-')
        else:
            str+=("+")
    print(str)

















