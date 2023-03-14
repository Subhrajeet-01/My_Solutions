s1=input()
s2=input()
s=input()
s4=s1+s2
l1=list(s)
l2=list(s4)
l1.sort()
l2.sort()
if(l1==l2):
    print("YES")
else:
    print("NO")


