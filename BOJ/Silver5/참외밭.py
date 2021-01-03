# 2477번
# hint: 정육각형, 변들이 이어져서 주어짐
import sys
input=sys.stdin.readline

k=int(input())
arr=[]
h,w=0,0
for _ in range(6):
    d,v=map(int,input().split())
    if d in [1,2]:
        arr.append((0, v))
        w=max(w,v)
    else:
        arr.append((1, v))
        h=max(h,v)
arr*=2
for i in range(1,7):
    if arr[i-1][0]==arr[i+1][0] and arr[i][0]==arr[i+2][0] and arr[i-1][1]+arr[i+1][1] in [w,h] and arr[i][1]+arr[i+2][1] in [w,h]:
        print(k*(w*h-arr[i][1]*arr[i+1][1]))
        break