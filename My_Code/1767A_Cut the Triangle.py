test = int(input(""))
for i in range(test):
    l=[]
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if(x1==x2 or x2==x3 or x3==x1 and y1==y2 or y2==y3 or y3==y1):
        print("NO")
    else:
        print("YES")
