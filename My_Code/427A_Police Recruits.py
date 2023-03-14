n=int(input())
l=list(map(int,input().split()))
police,crime=0,0
for i in range(n):
    if(l[i]==-1):
        if(police>0):
            police-=1
        else:
            crime+=1
    else:
        police+=l[i]
print(crime)
