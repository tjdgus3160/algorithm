# 11536번
import sys
input=sys.stdin.readline

arr=[input().rstrip('\n') for _ in range(int(input()))]
if arr==sorted(arr):
    print('INCREASING')
elif arr==sorted(arr,reverse=True):
    print('DECREASING')
else:
    print('NEITHER')