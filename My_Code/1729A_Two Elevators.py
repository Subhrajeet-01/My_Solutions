for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=abs(c-b)+c
    if(x>a):
        print(1)
    elif(x<a):
        print(2)
    else:
        print(3)






"""
    if(a<=b and a<c):
        print(1)
    elif(a>b and a<c):
        print(1)
    elif(a>b and b>=c):
        print(2)
    else:
        print(3)
"""
