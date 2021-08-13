n=int(input())
arr=sorted([*map(int,input().split())])
res=0
for i in range(n):
    res=max(res,arr[i]+arr[-1-i])
print(res)