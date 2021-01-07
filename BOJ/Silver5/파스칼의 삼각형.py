# 16395번
import sys
input=sys.stdin.readline

arr=[[1],[1,1],[1,2,1]]
for i in range(3,30):
    tmp=[]
    for j in range(i-1):
        tmp.append(arr[i-1][j]+arr[i-1][j+1])
    tmp=[1]+tmp+[1]
    arr.append(tmp)

n,k=map(int,input().split())
print(arr[n-1][k-1])