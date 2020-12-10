# 1181번
import sys
n=int(input())
a=[sys.stdin.readline().rstrip() for i in range(n)]
a=sorted(a,key=lambda x:(len(x),x))
before=None
for i in a:
    if i==before:
        continue
    before=i
    print(i)