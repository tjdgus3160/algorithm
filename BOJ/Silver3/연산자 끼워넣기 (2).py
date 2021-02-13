# 15658번
import sys
input=sys.stdin.readline

def func(k,cur):
    global big,small
    if k==n:
        big=max(big,cur)
        small=min(small,cur)
        return
    for i in range(4):
        if isused[i]:
            isused[i]-=1
            if i==0:
                func(k+1,cur+arr[k])
            elif i==1:
                func(k+1,cur-arr[k])
            elif i==2:
                func(k+1,cur*arr[k])
            else:
                if cur>0:
                    func(k+1,cur//arr[k])
                else:
                    func(k+1,(abs(cur)//arr[k])*(-1))
            isused[i]+=1

n=int(input())
arr=[*map(int,input().split())]
big=-1*float('inf')
small=float('inf')
isused=[*map(int,input().split())]
func(1,arr[0])
print(big)
print(small)