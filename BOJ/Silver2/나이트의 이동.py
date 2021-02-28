# 7562번
from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    a,b=map(int,input().split())
    x,y=map(int,input().split())
    dq=deque([(a,b)])
    dic=set()
    dic.add((a,b))
    k=0
    res=0
    while dq:
        cnt=len(dq)
        for _ in range(cnt):
            a,b=dq.popleft()
            if a==x and b==y:
                res=k
                break
            for na,nb in [[a+2,b-1],[a+2,b+1],[a+1,b-2],[a+1,b+2],[a-2,b-1],[a-2,b+1],[a-1,b-2],[a-1,b+2]]:
                if 0<=na<n and 0<=nb<n and (na,nb) not in dic:
                    dq.append((na,nb))
                    dic.add((na,nb))
        else:
            k+=1
            continue
        break
    print(res)