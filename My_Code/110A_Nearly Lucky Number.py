bignum=100
bignum=input()
count=0
for i in bignum:
    if i=='7' or i=='4':
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")


"""
n= int(input())
s=str(n)
l=list(s)
x=0
for i in range(len(l)):
    if(l[i]=='4' or l[i]=='7'):
        x+=1
    else:
        x=0
m=l.count('4')
n=l.count('7')
sum=m+n
if(len(l)==1):
    print('NO')
elif(sum==4 or sum==7):
    print('YES')
elif(x==len(l)):
    print('YES')
else:
    print('NO')


"""
