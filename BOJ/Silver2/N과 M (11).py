# 15665번
import sys
input=sys.stdin.readline

def func(k,tmp):
    if k==m:
        tmp=tuple(tmp)
        if tmp not in s:
            print(*tmp)
            s.add(tmp)
        return
    for i in range(len(arr)):
        func(k+1,tmp+[arr[i]])

s=set()
n,m=map(int,input().split())
arr=sorted(list(set([*map(int,input().split())])))
func(0,[])

