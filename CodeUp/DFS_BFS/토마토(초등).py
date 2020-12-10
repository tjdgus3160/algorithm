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

m,n,h=map(int,input().split())
l=[]
q=deque()
cnt=0
total=0
for i in range(h):
    tmp=[]
    for j in range(n):
        t=[*map(int,input().split())]
        tmp+=[t]
        total+=t.count(1)
        total+=t.count(0)
        for k in range(m):
            if t[k]==1:
                q.append([k,j,i])
                cnt+=1
    l+=[tmp]

day=-1
com=0
while q:
    ccnt=copy.deepcopy(cnt)
    com+=ccnt
    if ccnt==0:
        break
    day+=1
    cnt=0
    while ccnt>0:
        x,y,z=q.popleft()
        ccnt-=1
        if x>0 and l[z][y][x-1]==0:
            l[z][y][x-1]=1
            q.append([x-1,y,z])
            cnt+=1
        if x<m-1 and l[z][y][x+1]==0:
            l[z][y][x+1]=1
            q.append([x+1,y,z])
            cnt+=1
        if y>0 and l[z][y-1][x]==0:
            l[z][y-1][x]=1
            q.append([x,y-1,z])
            cnt+=1
        if y<n-1 and l[z][y+1][x]==0:
            l[z][y+1][x]=1
            q.append([x,y+1,z])
            cnt+=1
        if z>0 and l[z-1][y][x]==0:
            l[z-1][y][x]=1
            q.append([x,y,z-1])
            cnt+=1
        if z<h-1 and l[z+1][y][x]==0:
            l[z+1][y][x]=1
            q.append([x,y,z+1])
            cnt+=1
if total!=com:
    print(-1)
else:
    print(day)

