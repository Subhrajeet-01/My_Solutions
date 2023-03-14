k=int(input())
L=int(input())
m=int(input())
n=int(input())
d=int(input())
l=[]
count=0
nocount=0
for i in range(1,d+1):
    l+=[i]

for j in range(len(l)):
    if(l[j]%k==0 or l[j]%L==0 or l[j]%m==0 or l[j]%n==0):
        count+=1
    else:
        nocount+=1
x=d-nocount
print(x)


