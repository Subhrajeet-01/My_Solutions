n=int(input())
l=[]
count=0
for i in range(n):
    s=input()
    l+=[s]
for j in range(len(l)):
    if(l[j]=="Tetrahedron" ):
        count+=4
    elif(l[j]=="Cube"):
        count+=6
    elif(l[j]=="Octahedron" ):
        count+=8
    elif(l[j]=="Icosahedron"):
        count+=20
    else:
        count+=12
print(count)