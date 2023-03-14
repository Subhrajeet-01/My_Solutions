t = int(input())
for i in range(t):
    num=list(input())
    print(len(num)-num.count("0"))
    for j in range(len(num)):
        if(num[j]!='0'):
            print(num[j]+"0"*(len(num)-j-1),end=' ')
    print()





"""
l=[]
result=[]
for i in range(t):
    x=int(input())
    l+=[x]
for j in range(len(l)):
    if(l[j] % 10 !=0):
          r=l[j]%10
"""





"""
for j in range(len(l)):
    s=str(l[j])
    z=len(s)-1
    if(s[z]!=0):
        r=int(s)%10
        result+=r
"""

