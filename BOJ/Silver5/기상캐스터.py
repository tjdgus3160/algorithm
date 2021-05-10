# 10709번
import sys
input=sys.stdin.readline

h,w=map(int,input().split())
res=[[-1]*w for _ in range(h)]
for i in range(h):
    s=input().rstrip()
    for idx,v in enumerate(s):
        if v=='c':
            res[i][idx]=0
        elif idx>0 and res[i][idx-1]!=-1:
            res[i][idx]=res[i][idx-1]+1
for i in res:
    print(*i)