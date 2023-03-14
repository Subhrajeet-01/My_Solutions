for i in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    move=[]
    min_a=min(a)
    min_b=min(b)
    i=0
    while i<n :
        move.append(max((a[i]-min_a),(b[i]-min_b)))
        i+=1
    print(sum(move))