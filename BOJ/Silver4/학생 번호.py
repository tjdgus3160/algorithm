# 1235번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(input().rstrip())
tmp=[0]*n
for k in range(1,len(arr[0])+1):
    for i in range(n):
        if arr[i][-k:] in tmp:
            break
        tmp[i]=arr[i][-k:]
    else:
        print(k)
        break