# 10819번
import sys
input=sys.stdin.readline

def func(k,tmp):
    global res
    if k>=n:
        v=sum([abs(tmp[i]-tmp[i+1]) for i in range(n-1)])
        res=max(res,v)
        return
    for i in range(n):
        if not isused[i]:
            isused[i]=True
            tmp.append(arr[i])
            func(k+1,tmp)
            tmp.pop()
            isused[i]=False
res=0
n=int(input())
arr=[*map(int,input().split())]
isused=[False]*n
func(0,[])
print(res)
