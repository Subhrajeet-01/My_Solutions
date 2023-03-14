n = int(input())
a = [int(i)for i in input().split()]
b = [int(i)for i in input().split()]
a.pop(0)
b.pop(0)
ans = True

for currentlevel in range(1,n+1):
    if(a.count(currentlevel)==0 and b.count(currentlevel)==0):
        ans = False
if ans:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")




"""

n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l=[]
r=[]
if(x==[0] or x==[0, 0] or y==[0] or y==[0, 0]):
    for i in range(n+1):
        l+=[i]
else:
    for i in range(1,n+1):
        l+=[i]

for element in x:
    if element not in r:
        r.append(element)
for elemen in y:
    if elemen not in r:
        r.append(elemen)
r.sort()
if(l==r):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
"""