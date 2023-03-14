from collections import deque
n, q = map(int, input().split())
l = deque(map(int, input().split()))
m = list(map(int, input().split()))
for i in m:
    x=l.index(i)
    print(x+1,end=" ")
    l.remove(i)
    l.appendleft(i)
