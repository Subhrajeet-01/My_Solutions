x,y=map(int,input().split())
a=True
d=x+1
count=0
while a:
    if((d)%2==1):
        for i in range(1,(d+1)):
           if(d%i==0):
               count+=1
        if (count == 2):
            a = False
        else:
            d+=1
            count=0
    else:
        d+=1
if(d==y):
    print("YES")
else:
    print("NO")







