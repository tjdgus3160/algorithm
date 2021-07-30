from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
home=[]
store=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(n):
        if tmp[x]==1:
            home.append([x,y])
        elif tmp[x]==2:
            store.append([x,y])
res=float('inf')
for sub in combinations(store,m):
    total=0
    for hx,hy in home:
        dist=float('inf')
        for sx,sy in sub:
            dist=min(dist,abs(hx-sx)+abs(hy-sy))
        total+=dist
    res=min(res,total)
print(res)