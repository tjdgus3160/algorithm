# 21278번
from itertools import combinations
import sys
input=sys.stdin.readline

def floydwarshall():
    n=len(graph)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])
    return graph

n,m=map(int,input().split())
graph=[[float('inf')]*n for _ in range(n)]
for i in range(n):
    graph[i][i]=0
for _ in range(m):
    a,b=map(lambda x:(int(x)-1),input().split())
    graph[a][b]=2
    graph[b][a]=2
arr=floydwarshall()
res=float('inf')
loc=None
for sub in combinations(range(n),2):
    tmp=0
    for idx,v in enumerate(arr):
        if idx not in sub:
            tmp+=min(v[sub[0]],v[sub[1]])
    if res>tmp:
        res=tmp
        loc=sub
print(*[i+1 for i in loc],res)