# 2597번
import sys
input=sys.stdin.readline

start=0
end=int(input())
r=[*map(int,input().split())]
b=[*map(int,input().split())]
y=[*map(int,input().split())]
if r[0] != r[1]:
    mid = sum(r) / 2
    if b[0]<mid:
        b[0]=2*mid-b[0]
    if b[1]<mid:
        b[1]=2*mid-b[1]
    if y[0]<mid:
        y[0]=2*mid-y[0]
    if y[1]<mid:
        y[1]=2*mid-y[1]
    end = max(end, 2 * mid - start)
    start=mid
if b[0] != b[1]:
    mid = sum(b) / 2
    if y[0] < mid:
        y[0] = 2 * mid - y[0]
    if y[1] < mid:
        y[1] = 2 * mid - y[1]
    end = max(end, 2 * mid - start)
    start = mid
if y[0] != y[1]:
    mid = sum(y)/2
    end=max(end,2*mid-start)
    start = mid
print("%.1f"%(end-start))