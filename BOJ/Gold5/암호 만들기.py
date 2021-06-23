# 1759번
import sys
input=sys.stdin.readline

def func(k,idx,res,mo,ja):
    if k==l:
        if mo>=1 and ja>=2:
            print(res)
        return
    for i in range(idx+1,c):
        if arr[i] in 'aeiou':
            func(k+1,i,res+arr[i],mo+1,ja)
        else:
            func(k+1,i,res+arr[i],mo,ja+1)
l,c=map(int,input().split())
arr=list(input().split())
arr.sort()

func(0,-1,'',0,0)