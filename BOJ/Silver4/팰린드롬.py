# 8892번
from itertools import permutations
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=[]
    for _ in range(int(input())):
        arr.append(input().rstrip())
    for s1,s2 in permutations(arr,2):
        k=s1+s2
        if k==k[::-1]:
            print(k)
            break
    else:
        print(0)
