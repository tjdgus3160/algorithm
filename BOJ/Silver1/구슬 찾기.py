# 2617번
from collections import defaultdict,deque
import sys
input=sys.stdin.readline

def bfs(start,dic):
    dq=deque([start])
    res=0
    visited=set()
    while dq:
        k=dq.pop()
        if k in dic:
            for v in dic[k]:
                if v not in visited:
                    res+=1
                    dq.append(v)
                    visited.add(v)
    return res

n,m=map(int,input().split())
big=defaultdict(list)
small=defaultdict(list)

for _ in range(m):
    a,b=map(int,input().split())
    big[b].append(a)
    small[a].append(b)

res=0
for i in range(1,n+1):
    if i in big and bfs(i,big)>=(n+1)//2:
        res+=1
    if i in small and bfs(i,small)>=(n+1)//2:
        res+=1
print(res)