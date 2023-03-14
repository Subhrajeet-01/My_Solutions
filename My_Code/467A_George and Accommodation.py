n=int(input())
l=[]
count=0
for i in range(n):
    x,y=map(int,input().split())
    l+=[x,y]
for j in range(0,len(l),2):
    if(l[j]!=l[j+1]):
        if(l[j+1]-l[j]>=2):
            count+=1
print(count)