for j in range(int(input())):
    n=int(input())
    l1=list(map(str,input().split()))
    l2=list(map(str,input().split()))
    l3=list(map(str,input().split()))
    n1,n2,n3=0,0,0
    for i in range(n):
        if(l1[i] in l2 or l1[i] in l3):
            if(l1[i] in l2 and l1[i] in l3):
                None
            else:
                n1+=1
        else:
            n1+=3
        if(l2[i] in l1 or l2[i] in l3):
            if(l2[i] in l1 and l2[i] in l3):
                None
            else:
                n2+=1
        else:
            n2+=3
        if(l3[i] in l1 or l3[i] in l2):
            if(l3[i] in l1 and l3[i] in l2):
                None
            else:
                n3+=1
        else:
            n3+=3
    print(n1,n2,n3)




