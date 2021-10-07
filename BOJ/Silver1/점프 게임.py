# 15558번
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
left=list(map(int,list(input().rstrip())))
right=list(map(int,list(input().rstrip())))

dq=deque([('left',0)])
lvisited=[False]*n
rvisited=[False]*n
lvisited[0]=True
time=0
while dq:
    l=len(dq)
    for _ in range(l):
        t,loc=dq.popleft()
        if loc==n-1 or loc+k>=n:
            print(1)
            exit()
        if t=='left':
            if left[loc+1] and not lvisited[loc+1]:
                lvisited[loc + 1]=True
                dq.append(('left',loc+1))
            if left[loc-1] and time<loc-1 and not lvisited[loc-1]:
                lvisited[loc - 1]=True
                dq.append(('left',loc-1))
            if loc+k<n and right[loc+k] and not rvisited[loc+k]:
                rvisited[loc + k]=True
                dq.append(('right',loc+k))
        else:
            if right[loc+1] and not rvisited[loc+1]:
                rvisited[loc + 1]=True
                dq.append(('right',loc+1))
            if right[loc-1] and time<loc-1 and not rvisited[loc-1]:
                rvisited[loc-1]=True
                dq.append(('right',loc-1))
            if loc+k<n and left[loc+k] and not lvisited[loc+k]:
                lvisited[loc+k]=True
                dq.append(('left',loc+k))
    left[time]=0
    right[time]=0
    time+=1
print(0)