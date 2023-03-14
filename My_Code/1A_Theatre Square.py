n,m,a=map(int,input().split())
w=n//a
if(n%a!=0):
    w+=1
l=m//a
if m%a!=0:
    l+=1
print(l*w)