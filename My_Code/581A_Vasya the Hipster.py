x,y=map(int,input().split())
if(x>y):
    remain=y
    p = (x-y) // 2
else:
    remain=x
    p = (y - x) // 2

print(remain,p)