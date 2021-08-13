import sys
input=sys.stdin.readline

n=int(input())
arr=[[*map(int,input().split())]for _ in range(n)]
for y in range(n):
    for x in range(n):
        tmp=[]
        if 0<=x-1<n:
            tmp.append(arr[y][x-1])
        if 0<=y-1<n:
            tmp.append(arr[y-1][x])
        if tmp and arr[y][x]>max(tmp):
            arr[y][x]=max(tmp)
print(arr[-1][-1])