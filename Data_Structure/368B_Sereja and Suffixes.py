def solution():
    k=int(input())
    print(ans[k-1])

n,m =map(int,input().split())
s = set()
ans=[0]*n
l=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    s.add(l[i])
    ans[i]=len(s)
while m:
    m-=1
    solution()
