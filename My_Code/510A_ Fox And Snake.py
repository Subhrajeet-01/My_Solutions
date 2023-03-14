n,m=map(int,input().split())
r=1
for i in range(n):
    if i%2==0:
        print("#"*m)
    elif r==1:
        print("."*(m-1),end='')
        print("#")
        r=0
    else:
        print("#",end='')
        print("."*(m-1))
        r=1







"""
x,y=map(int,input().split())
s=''
for i in range(x):
    for j in range(y):
        if(i%2==1 and j==1):
                while(y-1<j):
                    s+='.'
                    j+=4
    print()
"""