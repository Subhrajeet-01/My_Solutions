i=1
l=[]
while True:
    if i%3!=0 and str(i)[-1]!='3':
        l.append(i)
    if(len(l)==1000):
        break
    i+=1
t=int(input())
for i in range(t):
    num=int(input())
    print(l[num-1])




"""


for j in range(t):
    x=int(input())
for i in range(x):
    if(i%3!=0):
        s=str(i)
        if(s[len(s)-1]!='3'):
            l+=[i]
print(i)



"""
