n=int(input())
d=[100,20,10,5,1]
count=0
for i in range(5):
    x=n//d[i]
    y=n%d[i]
    count+=x
    n=y
print(count)