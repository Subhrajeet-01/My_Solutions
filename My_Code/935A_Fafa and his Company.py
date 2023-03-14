n=int(input())
i=1
count=0
while(i<=n/2):
    if((n-i)%i==0):
        count+=1
    i+=1
print(count)