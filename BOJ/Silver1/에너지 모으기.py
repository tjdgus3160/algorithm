# 16198번
import sys
input=sys.stdin.readline

def func(cur,tmp):
    global res
    if len(tmp)==2:
        res=max(res,cur)
        return
    for i in range(1,len(tmp)-1):
        k=tmp[i]
        del tmp[i]
        func(cur+tmp[i-1]*tmp[i],tmp)
        tmp.insert(i,k)

n=int(input())
arr=[*map(int,input().split())]
res=0

func(0,arr)
print(res)