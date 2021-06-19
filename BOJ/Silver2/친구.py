# 1058번
import sys
input=sys.stdin.readline

n=int(input())
arr=[input() for _ in range(n)]

res=0
for i in range(n):
    cnt=0
    for j in range(n):
        if i == j:
            continue
        if arr[i][j]=='Y':
            cnt += 1
        else:
            for k in range(n):
                if arr[i][k] == 'Y' and arr[k][j] == 'Y':
                    cnt+=1
                    break
    res=max(res,cnt)
print(res)
