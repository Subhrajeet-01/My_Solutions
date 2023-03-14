n = int(input())
l=list(map(int,input().split()))
l.sort()
count=1
for i in l:
    if i>=count:
        count+=1
print(count-1)