# 1182번
import sys
input=sys.stdin.readline

cnt=0
def func(k,tot):
    global cnt
    if k==n:
        if tot==s:
            cnt+=1
        return
    func(k+1,tot)
    func(k+1,tot+arr[k])

n,s=map(int,input().split())
arr=[*map(int,input().split())]
func(0,0)
if s==0:
    cnt-=1
print(cnt)