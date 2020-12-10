from collections import deque
import copy
import sys
input=sys.stdin.readline

def view(l):
    for i in l:
        for j in i:
            print(*j)
        print()
    print()

m,n=map(int,input().split())
l=[]
q=deque()
cnt=0
total=0

l=[]
for j in range(n):
    t=[*map(int,input().split())]
    l+=[t]
    total+=t.count(1)
    total+=t.count(0)
    for k in range(m):
        if t[k]==1:
            q.append([k,j])
            cnt+=1

day=-1
com=0
while q:
    if cnt==0:
        break
    ccnt=copy.deepcopy(cnt)
    com+=ccnt
    day+=1
    cnt=0
    while ccnt>0:
        x,y=q.popleft()
        ccnt-=1
        if x>0 and l[y][x-1]==0:
            l[y][x-1]=1
            q.append([x-1,y])
            cnt+=1
        if x<m-1 and l[y][x+1]==0:
            l[y][x+1]=1
            q.append([x+1,y])
            cnt+=1
        if y>0 and l[y-1][x]==0:
            l[y-1][x]=1
            q.append([x,y-1])
            cnt+=1
        if y<n-1 and l[y+1][x]==0:
            l[y+1][x]=1
            q.append([x,y+1])
            cnt+=1
if total!=com:
    print(-1)
else:
    print(day)
