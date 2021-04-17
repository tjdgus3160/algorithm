# 2668번
import sys
input=sys.stdin.readline

def dfs(k,cur,tmp):
    global res
    if k==cur:
        res+=tmp
        return
    if arr[k] not in tmp:
        tmp.append(arr[k])
        dfs(arr[k],cur,tmp)

n=int(input())
arr=[0]
for _ in range(n):
    arr.append(int(input()))

res=[]
for i in range(1,n+1):
    if i in res:
        continue
    if i==arr[i]:
        res.append(i)
    else:
        dfs(arr[i],i,[arr[i]])
print(len(res))
for i in sorted(res):
    print(i)