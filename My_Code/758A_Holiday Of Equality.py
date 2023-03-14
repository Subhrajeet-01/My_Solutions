n= int(input())
count=0
for i in range(n):
    l=list(map(int,input().split()))
    break

x=max(l)
for j in range(len(l)):
    if(x>l[j]):
        r=x-l[j]
        count+=r

print(count)
