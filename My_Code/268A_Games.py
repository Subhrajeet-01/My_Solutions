N= int(input())
n=N*(N-1)
l=[]
count=0
i=0
while(i<N):
    x,y=map(int,input().split())
    l+=[[x,y]]
    i+=1
for j in range(len(l)):
    for k in range(len(l)):
        if(l[j][1]==l[k][0]):
            count+=1
print(count)

