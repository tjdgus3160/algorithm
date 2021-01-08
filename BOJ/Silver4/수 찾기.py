# 1920번
import sys
input=sys.stdin.readline

dic={}
input()
for i in [*map(int,input().split())]:
    dic[i]=1
input()
for i in [*map(int,input().split())]:
    if i in dic:
        print(1)
    else:
        print(0)