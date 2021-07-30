from itertools import combinations
import sys
input=sys.stdin.readline

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
res=float('inf')
for i in range(1,n+1):
    for sub in combinations(range(len(arr)),i):
        a=sum([arr[j][1] for j in sub])
        b=1
        for j in sub:
            b*=arr[j][0]
        res=min(res,abs(a-b))
print(res)