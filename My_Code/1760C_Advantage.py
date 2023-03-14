for j in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    lst=sorted(l)
    for i in range(len(l)):
        if(l[i]==lst[-1]):
            print(l[i]-lst[-2],end=' ')
        else:
            print(l[i]-lst[-1],end=' ')
    print()



"""
if(maxi!=l[i]):
            x=l[i]-maxi
            result.append(x)
        else:
            if(l.count(maxi)==n):
                x=l[i]-maxi
                result.append(x)
            else:
                lst.remove(maxi)
                x=l[i]-max(lst)
                result.append(x)
"""