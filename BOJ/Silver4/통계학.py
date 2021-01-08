# 2108번
import operator
from collections import Counter
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
tmp=sorted(Counter(arr).items(),key= lambda x:(-x[1],x[0]))
if len(tmp)>1:
    if tmp[0][1]>tmp[1][1]:
        print(tmp[0][0])
    else:
        print(tmp[1][0])
else:
    print(tmp[0][0])
print(arr[-1]-arr[0])