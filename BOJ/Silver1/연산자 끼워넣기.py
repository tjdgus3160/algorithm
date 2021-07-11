# 14888번
import sys
input=sys.stdin.readline

def func(k,cur):
    if k==n:
        res[0]=max(res[0],cur)
        res[1]=min(res[1],cur)
        return
    for i in range(4):
        if op[i]:
            if i==0:
                op[i]-=1
                func(k+1,cur+arr[k])
                op[i]+=1
            elif i==1:
                op[i]-=1
                func(k+1,cur-arr[k])
                op[i]+=1
            elif i==2:
                op[i]-=1
                func(k+1,cur*arr[k])
                op[i]+=1
            elif i==3:
                op[i]-=1
                if cur>0:
                    func(k+1,cur//arr[k])
                else:
                    func(k+1,-1*(-1*cur//arr[k]))
                op[i]+=1

n=int(input())
arr=[*map(int,input().split())]
op=[*map(int,input().split())]
res=[-float('inf'),float('inf')]

func(1,arr[0])
for i in res:
    print(i)