n,k=map(int,input().split())
count=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]+k > 5:
        continue
    else:
        count+=1
print(count//3)