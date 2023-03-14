s=input()
l=list(s)
l.pop(0)
l.pop(len(l)-1)
L=[]
for element in l:
    if element not in L:
        L.append(element)
if(len(L)==0):
    print(0)
elif(len(L)==1):
    print(1)
else:
    print(len(L)-2)
