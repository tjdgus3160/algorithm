from itertools import combinations
import sys
input=sys.stdin.readline

a=[]
for i in range(9):
    a.append(int(input()))
for v in combinations(a,7):
    if sum(v)==100:
        v=list(v)
        v.sort()
        for i in v:
            print(i)
        break
