n=int(input())
s=input()
S=s.lower()
l=list(S)
L=[]
for i in l:
    if i not in L:
        L.append(i)

if(len(L)==26):
    print('YES')
else:
    print('NO')