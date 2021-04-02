# 1535번
import sys
input=sys.stdin.readline

def func(k,hp,joy):
    global res
    if k==n:
        res=max(res,joy)
        return
    func(k+1,hp,joy)
    if hp-l[k]>0:
        func(k+1,hp-l[k],joy+j[k])

n=int(input())
l=[*map(int,input().split())]
j=[*map(int,input().split())]
res=0
func(0,100,0)
print(res)