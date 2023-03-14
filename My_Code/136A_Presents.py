n=int(input())
p=list(map(int,input().split()))
gift=[None for y in range (n)]
for i in range(n):
    gift[p[i]-1]=i+1
print(*gift,sep=' ')
