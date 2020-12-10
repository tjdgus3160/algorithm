# 1439번
import sys
input=sys.stdin.readline

n=input()
arr=[]
for i in n:
    if i=='\n':
        continue
    if not arr:
        arr.append(i)
        continue
    if arr[-1]!=i:
        arr.append(i)
print(min(arr.count('0'),arr.count('1')))