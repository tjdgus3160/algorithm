# 15702번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
q=[*map(int,input().split())]
res=[]
for _ in range(m):
    i,*arr=input().split()
    res.append([int(i),sum([q[i] for i in range(n) if arr[i]=='O'])])
res.sort(key=lambda x:(-x[1],x[0]))
print(*res[0])