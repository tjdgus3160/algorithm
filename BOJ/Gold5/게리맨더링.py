# 17471번
from itertools import combinations
from collections import defaultdict,deque
import sys
input=sys.stdin.readline

def bfs(group):
    visited=set([group[0]])
    dq=deque([group[0]])
    while dq:
        v=dq.popleft()
        for i in dic[v]:
            if i in group and i not in visited:
                visited.add(i)
                dq.append(i)
    return len(visited)==len(group)

n=int(input())
p=[*map(int,input().split())]
dic=defaultdict(set)
for i in range(1,n+1):
    _,*tmp=map(int,input().split())
    for v in tmp:
        dic[i].add(v)
        dic[v].add(i)
res=float('inf')
for i in range(1,n//2+1):
    for sub in combinations(range(1,n+1),i):
        other=tuple({*range(1,n+1)}-set(sub))
        if bfs(sub) and bfs(other):
            res=min(res,abs(sum([p[i-1]for i in sub])-sum([p[i-1]for i in other])))
print(res if res!=float('inf') else -1)