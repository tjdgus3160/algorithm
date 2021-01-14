# 1051번
import sys
input=sys.stdin.readline

arr=[]
n,m=map(int,input().split())
for i in range(n):
    arr.append(input().rstrip('\n'))
res=0
for i in range(1,min(n,m)):
    for y in range(n):
        for x in range(m):
            if y+i<n and x+i<m and arr[y][x]==arr[y][x+i]==arr[y+i][x]==arr[y+i][x+i]:
                res=i
res+=1
print(res**2)