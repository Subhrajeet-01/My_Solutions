n=int(input())
result=0
for i in range(n):
    s=input()
    if (s=="X++" or s=="++X"):
        result+=1
    else:
        result-=1

print(result)