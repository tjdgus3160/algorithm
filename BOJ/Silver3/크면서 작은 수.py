# 2992번
import sys
input=sys.stdin.readline

def func(k,v):
    if k==n:
        if int(v) not in arr:
            arr.append(int(v))
        return
    for i in range(n):
        if not isused[i]:
            isused[i]=True
            func(k+1,v+x[i])
            isused[i]=False

x=input().rstrip('\n')
n=len(x)
isused=[False]*len(x)
arr=[]
func(0,"")
arr.sort()
idx=arr.index(int(x))
print(arr[idx+1] if idx<len(arr)-1 else 0)