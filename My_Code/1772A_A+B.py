n=int(input())
L=[]
for i in range(n):
    s=input()
    l=list(s)
    #print(l)
    add=int(l[0])+int(l[2])
    L.append(add)
    #print(add)
for j in range(len(L)):
    print(L[j])