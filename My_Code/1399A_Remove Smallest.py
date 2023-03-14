test = int(input())

while(test):
    length=int(input())
    arr = [int (x) for x in input().split()]
    sarr=sorted(arr)
    flag=True
    for i in range(len(sarr)-1):
        if abs(sarr[i]-sarr[i+1])>1 :
            flag=False
    if(flag==False):
        print("NO")
    else:
        print("YES")
    test=test-1