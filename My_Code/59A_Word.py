s=input()
l=list(s)
uc,lc=0,0
for i in range(len(l)):
    if(ord(l[i])<96):
        uc+=1
    else:
        lc+=1
if(uc>lc):
    L =[x.upper() for x in l]
else:
    L= [x.lower() for x in l]
for k in range(len(L)):
    print(L[k],end='')