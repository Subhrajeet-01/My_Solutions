for i in range(int(input())):
    odd=0
    even=0
    arraysize=int(input())
    array=list(map(int,input().split()))
    for j in range(arraysize):
        if array[j]%2==0 and j%2!=0:
            even+=1
        elif(array[j]%2!=0 and j%2==0):
            odd+=1
    if(odd==even):
        print(odd)
    else:
        print(-1)



"""
t=int(input())
count=0
j=0
for i in range(t):
    x=int(input())
    l=list(map(int,input().split()))
    while(j<x):
        if(x!=1):
            if (l[j] % 2 != j % 2):
                if (l[j + 1] % 2 != (j + 1) % 2):
                    l[j],l[j+1]=l[j+1],l[j]
                    count += 1
                else:
                    count = -1
            j = j + 1
        else:
            if(l[j]%2==0):
                count=0
            else:
                count=-1
        print(count)
        l = []
        count = 0
        j = 0
"""