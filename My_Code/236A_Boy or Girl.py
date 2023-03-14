s=input()
l=list(s)
t=[]
for element in l:
    if element not in t:
        t.append(element)
x=len(t)
if(x%2==0):
    print( "CHAT WITH HER!")
else:
    print("IGNORE HIM!")