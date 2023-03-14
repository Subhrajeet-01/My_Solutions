t=int(input())
mishka,chris=0 ,0
for i in range(t):
    m,c=map(int,input().split())
    if(m>c):
        mishka+=1
    elif(c>m):
        chris+=1
    else:
        mishka+=1
        chris+=1
if(mishka>chris):
    print("Mishka")
elif(mishka<chris):
    print("Chris")
else:
    print("Friendship is magic!^^")