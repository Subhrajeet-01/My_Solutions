import math
for i in range(int(input())):
    n=int(input())
    print(pow(2, int(math.log(n,2)))-1)