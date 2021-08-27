import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[*map(int,input().split())]
prefix=[0]
for v in arr:
    prefix.append(prefix[-1]+v)
for _ in range(m):
    a,b=map(int,input().split())
    print(prefix[b]-prefix[a-1])

