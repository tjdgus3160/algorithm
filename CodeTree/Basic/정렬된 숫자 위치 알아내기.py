n=int(input())
arr=[*map(int,input().split())]
tmp=sorted([[v,idx] for idx,v in enumerate(arr)])
for idx,v in enumerate(tmp):
    arr[v[1]]=idx+1
print(*arr)