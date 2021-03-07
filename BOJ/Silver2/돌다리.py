# 12761번
from collections import deque
import sys
input=sys.stdin.readline

a,b,n,m=map(int,input().split())
dq=deque([(n,0)])
dic=set()
dic.add(n)
while dq:
    cnt=len(dq)
    while cnt:
        loc,k=dq.popleft()
        for i in [loc+1,loc-1,loc-a,loc+a,loc-b,loc+b,loc*a,loc*b]:
            if 0<=i<=100000 and i not in dic:
                if i==m:
                    print(k+1)
                    exit()
                dq.append((i,k+1))
                dic.add(i)
        cnt-=1
