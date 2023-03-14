count=0
l=[]
for i in range(int(input())):
    s=input()
    l.append(s)
for j in range(len(l)-1):
    if(l[j]!=l[j+1]):
        count+=1
print(count+1)
