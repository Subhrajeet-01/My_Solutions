for i in range(int(input())):
    l=[]
    n=int(input())
    x=n/2
    a=True
    if(x%2!=0):
        print("NO")
    else:
        print("YES")
        for j in range(int(x)):
            Even = 2 * (j + 1)
            l.append(Even)

        for k in range(int(x/2)):
            if a:
                Odd1=l[k]-1
                l.append(Odd1)
                a=False
            else:
                Odd2 = l[k] + 1
                l.append(Odd2)
                a=True


        for element in l:
            print(element,end=' ')
        print()



