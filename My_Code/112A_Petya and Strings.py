s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()

if(s1==s2):
    print("0")
elif(s1>s2):
    print("1")
elif(s2>s1):
    print("-1")

"""
s1=input()
s2=input()
l1=list(s1)
l2=list(s2)
t1=0
t2=0
for i in range(len(l1)):
    x=(ord(l1[i])-ord(l2[i]))!=32
    y=(ord(l1[i])-ord(l2[i]))!=-32
    z=(ord(l1[i])-ord(l2[i]))!=0
    if(x and y and z):
        t1=ord(l1[i])
        t2=ord(l2[i])
        break
    else:
        None
if (t1 > t2):
    print(1)
elif(t2 > t1):
    print(-1)
else:
 print(0)
"""