n, k, l, c, d, p, nl, np = map(int,input().split())
x=(k*l)//nl
y=c*d
z=p//np
r=min(x,y,z)//n
print(r)

