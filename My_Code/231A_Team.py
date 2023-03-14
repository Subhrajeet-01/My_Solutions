problem=int(input())
count=0
for i in range(problem):
    Petya,Vasya,Tonya =map(int,input().split())
    if (Petya + Vasya + Tonya == 2):
        count += 1
    elif(Petya + Vasya + Tonya == 3):
        count+=1
    else:
       count+=0
print(count)