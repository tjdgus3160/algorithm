# 18352번
from collections import deque
import sys
input=sys.stdin.readline

def dfs(start):
    v=set()
    v.add(start)
    dq=deque([start])
    t=0
    while dq:
        if t==k:
            break
        cnt=len(dq)
        for _ in range(cnt):
            node=dq.popleft()
            if node not in table:
                continue
            for i in table[node]:
                if i not in v:
                    v.add(i)
                    dq.append(i)
        t+=1
    return dq

n,m,k,x=map(int,input().split())
table={}
for _ in range(m):
    a,b=map(int,input().split())
    table.setdefault(a,[])
    table[a].append(b)
res=dfs(x)
if res:
    for i in sorted(res):
        print(i)
else:
    print(-1)