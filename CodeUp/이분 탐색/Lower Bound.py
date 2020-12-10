import bisect
import sys
input=sys.stdin.readline


n,k=map(int,input().split())
arr=[*map(int,input().split())]
print(bisect.bisect_left(arr,k)+1)