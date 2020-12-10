import copy
from collections import deque
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
a=[str(i) for i in range(1,n+1)]
dq=deque([" ","+","-"])
cnt=1
res=[]
while cnt<n-1:
    size=len(dq)
    for i in range(size):
        t=dq.popleft()
        dq.append(t+" ")
        dq.append(t+ "+")
        dq.append(t+ "-")
    cnt+=1
for i in dq:
    tmp=copy.deepcopy(a)
    for loc,j in enumerate(i):
        tmp.insert(tmp.index(str(loc+1))+1,j)
    if eval("".join(tmp).replace(" ",""))==0:
        res.append(tmp)
for i in res:
    print("".join(i))
