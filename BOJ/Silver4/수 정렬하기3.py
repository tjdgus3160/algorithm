# 10989번
import sys
n=int(input())
l=[0]*10000
for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    l[a-1]+=1
for i in range(10000):
    while l[i]>0:
        sys.stdout.write("{}\n".format(i+1))
        l[i]-=1