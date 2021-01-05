# 10867번
import sys
input=sys.stdin.readline

input()
arr=[*map(int,input().split())]
print(*sorted(set(arr)))