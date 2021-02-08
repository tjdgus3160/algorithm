# 11292번
import sys
input=sys.stdin.readline

while True:
    n=int(input())
    if n==0:
        break
    arr=[]
    for _ in range(n):
        arr.append(input().split())
    arr.sort(key=lambda x:float(x[1]),reverse=True)
    k=float(arr[0][1])
    for v in arr:
        if float(v[1])==k:
            print(v[0], end=' ')
    print()