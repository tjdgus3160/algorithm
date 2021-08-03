import sys
input=sys.stdin.readline

def func(k,cur):
    if k==n:
        res[0]=min(res[0],cur)
        res[1]=max(res[1],cur)
        return
    if op[0]:
        op[0]-=1
        func(k+1,cur+arr[k])
        op[0]+=1
    if op[1]:
        op[1]-=1
        func(k+1,cur-arr[k])
        op[1]+=1
    if op[2]:
        op[2]-=1
        func(k+1,cur*arr[k])
        op[2]+=1

n=int(input())
arr=[*map(int,input().split())]
op=[*map(int,input().split())]
res=[float('inf'),-float('inf')]
func(1,arr[0])
print(*res)