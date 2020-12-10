# 2751번
import sys
l=[]
n=int(input())
for i in range(n):
    l.append(int(sys.stdin.readline()))
l=sorted(l)
for i in l:
    print(i)