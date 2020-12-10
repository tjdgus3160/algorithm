# 11376번
import sys
input=sys.stdin.readline

def find(x):
    for i in a[x]:
        if c[i]:
            continue
        c[i]=1
        if d[i]==0 or find(d[i]):
            d[i]=x
            return True
    return False

n,m=map(int,input().split())
a=[[]]
for i in range(n):
    cnt, *h=map(int,input().split())
    a.append(h)
d=[0 for _ in range(m+1)]

cnt=0
for _ in range(2):
    for i in range(1,n+1):
        c=[0 for _ in range(m+1)]
        if find(i):
            cnt+=1
print(cnt)