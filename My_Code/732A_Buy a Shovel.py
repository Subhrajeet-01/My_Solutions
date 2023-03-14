x,y=map(int,input().split())
r=x%10
count=0
z=x
m=2
if(r==0 or r==y):
    count=1
else:

    while(r!=0):
        r = z % 10
        count += 1
        z=x*m
        m+=1
        if(r==y):
            break

print(count)

