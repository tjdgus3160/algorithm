from itertools import combinations
import sys
input=sys.stdin.readline

def func(dot1,dot2):
    return pow(abs(dot1[0]-dot2[0]),2)+pow(abs(dot1[1]-dot2[1]),2)

n,m=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]

res=float('inf')
for sub in combinations(range(n),m):
    k=0
    for i in range(len(sub)-1):
        for j in range(i+1,len(sub)):
            k=max(k,func(arr[sub[i]],arr[sub[j]]))
    res=min(res,k)
print(res)