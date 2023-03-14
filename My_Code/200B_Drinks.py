n=int(input())
l=[]
sum=0
for i in range(n):
    x=map(int,input().split())
    l+=x
    break
for j in range(len(l)):
    sum+=int(l[j])
x=sum/n
s=str(x)
if(len(s)>15):
    print(round(x,12))
else:
    print('{0:.12f}'.format(x))


