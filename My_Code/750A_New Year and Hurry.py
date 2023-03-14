n,k=map(int,input().split())
t=240-k
p=0
for i in range(1,n+1):
    p+=i*5
if(t>p):
    print(n)
else:
    while(t<p):
        p-=n*5
        n-=1
    print(n)
