n,t=map(int,input().split())
l=list(input())
for i in range(t):
    i=0
    while i < n-1:
        if l[i]=="B" and l[i+1]=="G":
            l[i],l[i+1]="G","B"
            i+=2
        else:
            i+=1
for i in range(len(l)):
    print(l[i],end='')


"""

length,time=map(int,input().split())
x=list(input())
#print(s)
y=[]
for i in range(time):
    for j in range(length):
        if(x[i]=='B' and x[i+1]=='G'):
            x[i+1],x[i]=x[i],x[i+1]

            #print(str(x))
final=''.join(x)
print(final)                      """
