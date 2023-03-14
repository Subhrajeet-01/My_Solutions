t=int(input())
for i in range(t):
    x=int(input())
    if(x==1):
        print(1,0)
    elif(x==2):
        print(0,1)
    elif(x%3==0):
        y=x//3
        print(y,y)
    elif(x%3==1):
        y=x//3
        print(y+1,y)
    else:
        y=x//3
        print(y,y+1)
