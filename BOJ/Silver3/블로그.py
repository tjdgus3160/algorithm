import sys
input=sys.stdin.readline

n,x=map(int,input().split())
arr=[*map(int,input().split())]
cur=sum(arr[:x])
cnt=1
res=cur
for i in range(x,n):
    cur-=arr[i-x]
    cur+=arr[i]
    if cur == res:
        cnt+=1
    elif cur>res:
        res=cur
        cnt=1
if res:
    print(res)
    print(cnt)
else:
    print('SAD')
