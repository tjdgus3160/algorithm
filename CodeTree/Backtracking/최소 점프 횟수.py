import sys
input=sys.stdin.readline

def func(loc,cnt):
    global res
    if cnt>res:
        return
    if loc==n-1:
        res=min(res,cnt)
        return
    for i in range(1,arr[loc]+1):
        if loc+i<n:
            func(loc+i,cnt+1)

n=int(input())
arr=[*map(int,input().split())]

res=float('inf')
func(0,0)
print(res if res != float('inf') else -1)