# 10451번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    visited=[False]*(n+1)
    arr=[0]+[*map(int,input().split())]
    res=0
    for i in range(1,n+1):
        if not visited[i]:
            cur=i
            visited[cur]=True
            while True:
                cur=arr[cur]
                if visited[cur]:
                    break
                visited[cur]=True
            res+=1
    print(res)