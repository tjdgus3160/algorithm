import itertools
import sys
input=sys.stdin.readline

n=int(input())
arr=[0,0,0]
for i in map(int,input().split()):
    arr[i%3]+=1
print(arr[1]*arr[2]+arr[0]*(arr[0]-1)//2)
