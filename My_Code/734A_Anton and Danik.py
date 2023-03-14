n=int(input())
s=input()
l=list(s)
a,d=0,0
for i in range(n):
    if(l[i]=='A'):
        a+=1
    else:
        d+=1
if(a>d):
    print('Anton')
elif(a<d):
    print('Danik')
else:
    print('Friendship')