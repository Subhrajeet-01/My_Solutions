n=int(input())
a=list(map(int,input().split()))
ans=0
max=min=a[0]
for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
        ans+=1
    if a[i]<min:
        min=a[i]
        ans+=1
print(ans)








"""
n=int(input())
l=[]
count=0
c=0
for i in range(n):
    x=map(int,input().split())
    l+=x
    break
for i in range(len(l)-1):
    if(l[i]<=l[i+1]):
        count+=1
    elif(l[i+1]<=l[i]):
        c+=1
if(n==1):
    count=0
elif(c==len(l)-1):
    count=c
print(count)
"""