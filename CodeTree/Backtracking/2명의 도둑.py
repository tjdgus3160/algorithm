from itertools import combinations
import sys
input=sys.stdin.readline

def cal(tmp,c):
    k=0
    for i in range(len(tmp),0,-1):
        for sub in combinations(tmp,i):
            if sum(sub)<=c:
                k=max(k,sum([pow(v,2) for v in sub]))
    return k

def func(sx,sy,k,c):
    global res
    if sx+m>n:
        sx=0
        sy+=1
    for y in range(sy,n):
        for x in range(n-m+1):
            if y==sy and sx>x:
                continue
            res=max(res,k+cal(arr[y][x:x+m],c))

n,m,c=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
res=0
for y in range(n):
    for x in range(n-m+1):
        k=cal(arr[y][x:x+m], c)
        func(x+m,y,k,c)
print(res)