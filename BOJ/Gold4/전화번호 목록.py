# 5052번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=sorted([input().rstrip() for _ in range(n)])
    for i in range(1,n):
        if arr[i-1]==arr[i][:len(arr[i-1])]:
            print('NO')
            break
    else:
        print('YES')
