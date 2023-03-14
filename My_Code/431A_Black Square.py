l=list(map(int,input().split()))
s=str(input())
add=0
for i in s:
    if(i=='1'):
        add+=l[0]
    elif(i=='2'):
        add+=l[1]
    elif(i=='3'):
        add+=l[2]
    elif(i=='4'):
        add+=l[3]
print(add)