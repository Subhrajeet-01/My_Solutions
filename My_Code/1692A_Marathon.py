t=int(input())
L=[]
count, i = 0 ,1
for i in range(t):
    l=list(map(int,input().split()))
    for j in range(1,4):
        if(l[0]<l[j]):
            count+=1
    L+=[count]
    count=0
for k in range(len(L)):
    print(L[k])