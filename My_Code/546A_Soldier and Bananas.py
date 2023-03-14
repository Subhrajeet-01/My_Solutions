k,n,w=map(int,input().split())
total=0

for i in range(1,w+1):
    total+=k*i
if(n>total):
    remain=0
else:
    remain=total-n
print(remain)