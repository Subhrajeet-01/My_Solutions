s=input()
l=[]
for i in range(0,len(s),2):
    l+=s[i]
l.sort()
t=[]
S='+'
for j in range(0,len(l)):
    t+=l[j]+S
for k in range(len(t)-1):
    print(t[k],end='')