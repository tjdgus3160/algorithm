import sys
input=sys.stdin.readline

n,m=map(int,input().split())

arr=[]
res=0
for _ in range(n):
    s=[*map(int,input().split())]
    cur=None
    cnt=0
    for i in s:
        if not cur or cur !=i:
            cur=i
            cnt=1
        else:
            cnt+=1
        if cnt==m:
            res+=1
            break
    arr.append(s)

for x in range(n):
    cur=None
    cnt=0
    for y in range(n):
        if not cur or cur != arr[y][x]:
            cur=arr[y][x]
            cnt=1
        else:
            cnt+=1
        if cnt==m:
            res+=1
            break
print(res)