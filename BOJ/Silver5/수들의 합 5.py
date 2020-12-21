# 2018번
import sys
input=sys.stdin.readline

n=int(input())
res=0
tmp=0
start=1
for i in range(1,n+1):
    tmp+=i
    if tmp==n:
        res+=1
        tmp-=start
        start+=1
    elif tmp>n:
        while tmp>n:
            tmp-=start
            start+=1
            if tmp==n:
                res+=1
print(res)