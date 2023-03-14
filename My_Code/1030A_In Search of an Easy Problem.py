n=int(input())
l=[]
count=0
for i in range(n):
    x=map(int,input().split())
    l+=x
    break
for j in range(len(l)):
    if(int(l[j])!=0):
        count+=1
if(count>=1):
    print('HARD')
else:
    print('EASY')