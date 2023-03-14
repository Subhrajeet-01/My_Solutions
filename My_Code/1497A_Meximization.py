for j in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    result=[]
    remove=[]
    for i in l:
        if i not in result:
            result.append(i)
        else:
            remove.append(i)
    r=result.__add__(remove)
    for k in range(len(r)):
        print(r[k],end=' ')
    print()