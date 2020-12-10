# 11377번
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

n,m,k=map(int,input().split())
a=[[]]
b=[]
for i in range(n):
    cnt, *h=map(int,input().split())
    a.append(h)
    b.append([cnt, i])
b.sort(key=lambda x:x[0])

d=[0 for _ in range(m+1)]

cnt=0
for i in range(1,n+1):
    c=[0 for _ in range(m+1)]
    if find(i):
        cnt+=1

for i in range(1,n+1):
    c = [0 for _ in range(m + 1)]
    if find(i):
        cnt += 1
        k-=1
    if k==0:
        break

print(cnt)