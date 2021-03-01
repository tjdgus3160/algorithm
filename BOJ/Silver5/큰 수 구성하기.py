# 18511번
from itertools import product
import sys
input=sys.stdin.readline

n,k=input().split()
arr=input().split()
arr.sort(reverse=True)
if arr[-1]>n[0]:
    print(arr[0]*(len(n)-1))
else:
    for sub in product(arr,repeat=len(n)):
        k="".join(sub)
        if int(k)<=int(n):
            print(k)
            break