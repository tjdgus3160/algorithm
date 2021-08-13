n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
res=[]
for i in range(n):
    tmp=[]
    for j in range(n-1,-1,-1):
        tmp.append(arr[j][i])
    res.append(tmp)
for i in res:
    print(*i)