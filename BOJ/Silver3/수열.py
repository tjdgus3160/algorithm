import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[*map(int,input().split())]
prefix=[sum(arr[:k])]
for i in range(k,n):
    prefix.append(prefix[-1]+arr[i]-arr[i-k])
print(max(prefix))
