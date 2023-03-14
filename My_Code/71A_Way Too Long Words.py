n=int(input())
S=""
l=[]

for i in range(n):
    s=input()
    if(len(s)>10):
        S+=s[0]+str(len(s)-2)+s[len(s)-1]
        S+=','
    else:
        S+=s+','

x=S.split(',')
for j in range(len(x)-1):
    print(x[j])

