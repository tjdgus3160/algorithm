# 14753번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
arr.sort()
t1=arr[0]*arr[1]
t2=arr[0]*arr[1]*arr[-1]
t3=arr[-1]*arr[-2]
t4=arr[-1]*arr[-2]*arr[-3]
print(max(t1,t2,t3,t4))