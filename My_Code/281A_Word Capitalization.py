s= input()
l=list(s)
if(ord(l[0])>90):
    x=ord(l[0])-32
else:
    x=ord(l[0])
l.pop(0)
l.insert(0,chr(x))
for i in range(len(l)):
    print(l[i],end='')
