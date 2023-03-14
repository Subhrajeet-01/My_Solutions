
import collections
for j in range(int(input())):
    n,c=map(int,input().split())
    l=collections.Counter(map(int,input().split()))
    count=0
    for i in l:
        count += c if l[i]>=c else l[i]

    print(count)



    """
     l1=[]
    count = 0
    x=l.count(c)
    if(c==1 or n==1):
        for i in l:
            if i not in l1:
                l1.append(i)
        count=len(l1)
    else:
        if(n!=2):
            if(x>=c):
                y = len(l) - x
                count = c + y
            else:
                count=len(l)
        else:
            count=2
    """