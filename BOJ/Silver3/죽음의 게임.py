# 17204번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[0]*n
selected=[False]*n
for i in range(n):
    arr[i]=int(input())
selected[0]=True
m=0
cur=0
while True:
    if cur==k:
        print(m)
        break
    cur=arr[cur]
    if selected[cur]:
        print(-1)
        break
    selected[cur]=True
    m+=1