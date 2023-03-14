l,b=map(int,input().split())
count=0
if(l!=b):
    while(l<=b):
       l*=3
       b*=2
       count+=1
else:
    count=1

print(count)
