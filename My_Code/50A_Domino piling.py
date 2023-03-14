x,y=map(int,input().split())
m=x*y
if(m%2==1):
    r=(m-1)/2
    print(int(r))
else:
    print(int(m/2))