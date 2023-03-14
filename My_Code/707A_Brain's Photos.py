x,y=map(int,input().split())
a=True
for i in range(x):
    s=input().split()
    for j in range(y):
        if(s[j]=='C' or s[j]=='M' or s[j]=='Y'):
            a=False
            break

if a:
    print("#Black&White")
else:
    print("#Color")

