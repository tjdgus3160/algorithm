# 2891번
import sys
input=sys.stdin.readline

n,s,r=map(int,input().split())
err=[*map(int,input().split())]
rest=[*map(int,input().split())]
for i in rest:
    if 1<=i-1<=n and i-1 in err:
        err.remove(i-1)
    elif 1<=i+1<=n and i+1 in err:
        err.remove(i+1)
print(len(err))