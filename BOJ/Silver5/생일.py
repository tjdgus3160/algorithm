# 5635번
from datetime import datetime
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    s,d,m,y=input().split()
    arr.append([datetime(year=int(y),month=int(m),day=int(d)),s])
arr.sort()
print(arr[-1][1])
print(arr[0][1])