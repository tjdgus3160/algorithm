from itertools import combinations,permutations
import sys
input=sys.stdin.readline

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
res=float('inf')
tmp=[]
for sub in combinations(range(n),n//2):
    k=0
    for i,j in permutations(sub,2):
        k+=arr[i][j]
    tmp.append(k)
for i in range(len(tmp)//2):
    res=min(res,abs(tmp[i]-tmp[-1-i]))
print(res)