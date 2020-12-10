from itertools import combinations
import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
b=[*map(int,input().split())]

seq=[]
for i in range(1,101):
    if i in a:
        seq.append(0)
    elif i in b:
        seq.append(1)
if seq[0]==seq[2]:
    print("cross")
else:
    print("not cross")

