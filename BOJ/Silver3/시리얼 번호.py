# 1431번
import sys
n=int(input())
l=[]
for i in range(n):
    l.append(sys.stdin.readline().rstrip())
l.sort(key=lambda x:(len(x), sum([(int(x[i]) if x[i].isdigit() else 0) for i in range(len(x))]),x))
for i in l:
    print(i)