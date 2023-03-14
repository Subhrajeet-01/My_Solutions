for i in range(int(input())):
    x,y,n=map(int,input().split())
    print(n-((n - y)%x))



"""

t=int(input())
l=[]
for i in range(t):
    x,y,n=map(int,input().split())
    a = True
    while(a):
        if(n%x==y):
            l+=[n]
            a=False
        else:
            n=n-1
            a=True
for j in range(len(l)):
    print(l[j])
    
"""