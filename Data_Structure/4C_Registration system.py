n=int(input())
name={}
for i in range(n):
    n=input()
    x=name.get(n)
    if(x==None):
        name.update({n:0})
        print("OK")
    else:
        x+=1
        name.update({n:x})
        print(n,x,sep="")

"""

n=int(input())
l=[]
for i in range(n):
    l+=[str(input())]
for element in l:

    if(l.count(element)==1):
        x=l.index(element)
        l[x]="OK"
    else:
        l.reverse()
        y=l.count(element)
        for j in range(y,0,-1):
            result=element+str(j)
            x=l.index(element)
            l[x]=result
        l.reverse()


"""
