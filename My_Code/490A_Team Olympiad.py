n=int(input())
l=[]
R,R1,R2,R3=[],[],[],[]
x = map(int, input().split())
l += x
r1=l.count(1)
r2=l.count(2)
r3=l.count(3)
r=min(r1,r2,r3)
print(r)
for i in range(n):
    if l[i]==1 :
        R1+=[i]
    elif l[i]==2 :
        R2+=[i]                     #new line else re case 3
    else:
        R3+=[i]
for j in range(r):
    print(R1[j]+1,R2[j]+1,R3[j]+1)
