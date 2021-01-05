# 11728번
import sys
input=sys.stdin.readline

arr=[]
input()
arr+=[*map(int,input().split())]
arr+=[*map(int,input().split())]
arr.sort()
print(*arr)
