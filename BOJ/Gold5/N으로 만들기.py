# 17255번
import sys
input=sys.stdin.readline

def func(k,n):
    global res
    if k==n:
        res+=1
        return
    s=set()
    for i in n:
        if i+k in n:
            s.add(i+k)
        if k+i in n:
            s.add(k+i)
    for i in s:
        func(i,n)

n=input().rstrip()
res=0
func('',n)
print(res)