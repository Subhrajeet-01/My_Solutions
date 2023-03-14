s=input()
s1=input()
l=list(s)
L=list(s1)
r=[]
for i in range(len(l)):
    if(l[i]==L[i]):
        r+='0'
    else:
        r+='1'
for j in range(len(r)):
    print(r[j],end='')