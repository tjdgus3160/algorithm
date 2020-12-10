# 1531번
import sys
input=sys.stdin.readline

arr=[[0 for _ in range(101)] for _ in range(101)]
n,m=map(int,input().split())
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(min(y1,y2),max(y1,y2)+1):
        for j in range(min(x1,x2),max(x1,x2)+1):
            arr[i][j]+=1
res=0
for a in arr:
    res+=len([i for i in a if i>m])
print(res)