N=int(input())
n=N+1
dist=0
while(dist==0):
    s = str(n)
    l = list(s)

    a = l.count(l[0])
    b = l.count(l[1])
    c = l.count(l[2])
    d = l.count(l[3])

    if(a==b==c==d==1):
        dist=1
    else:
        n+=1
if(dist==1):
    print(n)

