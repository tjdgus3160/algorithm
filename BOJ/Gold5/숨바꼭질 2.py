# 12851번
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())

visited=[0]*100001
dq=deque([(n,0)])
res=0
minCnt=None
while dq:
    loc,cnt=dq.popleft()
    if loc==k:
        if not minCnt or minCnt==cnt:
            minCnt=cnt
            res+=1
        else:
            break
    for v in [loc+1,loc-1,loc*2]:
        if 0<=v<=100000 and (not visited[v] or visited[v]==cnt+1) and v!=n:
            dq.append((v,cnt+1))
            visited[v]=cnt+1
print(minCnt)
print(res)