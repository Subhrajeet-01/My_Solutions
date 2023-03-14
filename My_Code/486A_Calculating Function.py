n=int(input())
if(n%2):
    print(-(n//2 +1))
else:
    print(n//2)

                     #Time Limit Exided Error(Time Complexity)
"""
for i in range(n+1):              
    if(i%2==0):
        x=1*i
        result+=x
    else:
        y=(-1)*i
        result+=y
print(result)           """