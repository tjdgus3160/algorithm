# 2635번
import sys
input=sys.stdin.readline

def func(n,i):
    tmp=[n,i]
    a,b=n,i
    k=2
    while True:
        if a-b<0:
            break
        tmp.append(a-b)
        k+=1
        a,b=b,a-b
    return k,tmp

n=int(input())
res=[]
cnt=0
for i in range(1,n+1):
    k,tmp=func(n,i)
    if cnt<k:
        cnt=k
        res=tmp
print(cnt)
print(*res)