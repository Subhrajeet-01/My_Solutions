n,h=map(int,input().split())
count=0
l=[]
for i in range(n):
    x = map(int, input().split())
    l+=x
    break
for j in range(len(l)):
    if(int(l[j])>h):
        if(int(l[j])%h!=0):
            y = int(l[j]) // h
            count += y+1
        else:
            y = int(l[j]) // h
            count += y
    else:
        count += 1

print(count)