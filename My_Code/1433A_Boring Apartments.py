t=int(input())
a,b=0,1
z=True
R=[]
for i in range(t):
    x=int(input())
    s=str(x)
    l=list(s)
    x = int(l[0])-1
    y = len(l)
    while(y>0):
        a+=b
        y-=1
        b+=1
    r = (x*10)+a
    a=0
    b=1
    R.append(r)
for j in range(len(R)):
    print(R[j])
