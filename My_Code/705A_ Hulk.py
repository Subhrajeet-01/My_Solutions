n=int(input())
s1=' it'
s2=' I hate'
s3=' I love'
s4=' that'
s=''
if(n==1):
    s=' I hate'
else:
  for i in range(1,n+1):
        if(i%2==1):
            s=s+s2
            if(i!=n):
                s+=s4
        else:
            s=s+s3
            if (i != n):
                s += s4


s=s+s1
l=list(s)
l.pop(0)
for j in range(len(l)):
    print(l[j],end='')